#!/usr/bin/env python3
"""Generate the complete RSS mirror from canonical HTML news items."""
import argparse
import datetime as dt
import email.utils
import html
import hashlib
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class NewsParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items, self.item, self.field = [], None, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'article' and 'news-item' in a.get('class', '').split():
            self.item = {'title': '', 'description': '', 'published': '', 'link': '', 'id': a.get('id')}
        if self.item is None:
            return
        if tag == 'h3' and a.get('class') == 'news-title':
            self.field = 'title'
        elif tag == 'p' and a.get('class') == 'news-description':
            self.field = 'description'
        elif tag == 'span' and a.get('class') == 'news-date-published':
            self.field = 'published'
        elif tag == 'a' and self.field == 'title':
            self.item['link'] = a['href']

    def handle_endtag(self, tag):
        if self.item is None:
            return
        if (tag == 'h3' and self.field == 'title') or (tag == 'p' and self.field == 'description') or (tag == 'span' and self.field == 'published'):
            self.field = None
        if tag == 'article':
            self.item = {k: ' '.join(v.split()) if isinstance(v, str) else v for k, v in self.item.items()}
            if not self.item['link']:
                if not self.item['id']:
                    raise ValueError(f'Unlinked news item needs a stable id: {self.item["title"]}')
                self.item['link'] = 'https://ai101.health/ai-news.html#' + self.item['id']
            self.items.append(self.item)
            self.item, self.field = None, None

    def handle_data(self, data):
        if self.item is not None and self.field:
            self.item[self.field] += data


def parse_news(source):
    parser = NewsParser()
    parser.feed(source)
    return parser.items


def generate(source, existing, build_date):
    previous = ET.fromstring(existing)
    by_link = {x.findtext('link'): x.findtext('guid') for x in previous.findall('.//item')}
    by_title = {x.findtext('title'): x.findtext('guid') for x in previous.findall('.//item')}
    head = existing[:existing.index('    <item>')]
    head = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{build_date}</lastBuildDate>', head)
    entries, guids = [], set()
    items = parse_news(source)
    link_counts = Counter(x['link'] for x in items)
    for item in items:
        guid = by_title.get(item['title'])
        if not guid and link_counts[item['link']] == 1:
            guid = by_link.get(item['link']) or item['link']
        if not guid:
            digest = hashlib.sha256((item['title'] + item['published']).encode()).hexdigest()[:20]
            guid = 'urn:ai101:news:' + digest
        if guid in guids:
            raise ValueError(f'Duplicate news GUID: {guid}')
        guids.add(guid)
        lines = ['    <item>', f'      <title>{html.escape(item["title"])}</title>',
                 f'      <link>{html.escape(item["link"])}</link>',
                 f'      <description>{html.escape(item["description"])}</description>']
        # Do not invent a day for historical items dated only to a month.
        try:
            date = dt.datetime.strptime(item['published'].removeprefix('Published: '), '%b %d, %Y').replace(tzinfo=dt.timezone.utc)
            lines.append(f'      <pubDate>{email.utils.format_datetime(date, usegmt=True)}</pubDate>')
        except ValueError:
            pass
        attr = ' isPermaLink="false"' if guid != item['link'] else ''
        lines += [f'      <guid{attr}>{html.escape(guid)}</guid>', '    </item>']
        entries.append('\n'.join(lines))
    return head + '\n\n'.join(entries) + '\n\n  </channel>\n</rss>\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--build-date')
    args = parser.parse_args()
    source = (ROOT / 'ai-news.html').read_text()
    path = ROOT / 'ai-news-feed.xml'
    old = path.read_text()
    date = args.build_date or ET.fromstring(old).findtext('./channel/lastBuildDate')
    result = generate(source, old, date)
    if args.check:
        if result != old:
            raise SystemExit('RSS does not match canonical HTML. Run scripts/sync_news_feed.py.')
        print(f'RSS mirror verified: {len(parse_news(source))} items.')
    else:
        path.write_text(result)
        print(f'RSS synchronized: {len(parse_news(source))} items.')


if __name__ == '__main__':
    main()

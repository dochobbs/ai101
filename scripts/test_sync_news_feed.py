import unittest
import xml.etree.ElementTree as ET
from sync_news_feed import generate, parse_news

HEAD = '''<rss version="2.0"><channel><lastBuildDate>Sun, 01 Nov 2026 20:00:00 GMT</lastBuildDate>
    <item><title>Old</title><link>https://example.org/release</link><description>Old</description><guid>stable-old</guid></item></channel></rss>'''


def item(title, date, link='https://example.org/release'):
    return f'<article class="news-item"><span class="news-date-published">Published: {date}</span><h3 class="news-title"><a href="{link}">{title}</a></h3><p class="news-description">Useful <strong>evidence</strong> &amp; limits.</p></article>'


class FeedTest(unittest.TestCase):
    def test_shared_source_does_not_duplicate_story_identifiers(self):
        source = item('New', 'Nov 1, 2026') + item('Old', 'Apr 2026')
        result = generate(source, HEAD, 'Sun, 01 Nov 2026 20:00:00 GMT')
        rows = ET.fromstring(result).findall('.//item')
        self.assertEqual(len({x.findtext('guid') for x in rows}), 2)
        self.assertEqual(rows[1].findtext('guid'), 'stable-old')
        self.assertIsNone(rows[1].find('pubDate'))
        self.assertEqual(rows[0].findtext('description'), 'Useful evidence & limits.')
        self.assertEqual(generate(source, result, 'Sun, 01 Nov 2026 20:00:00 GMT'), result)

    def test_unlinked_story_has_a_real_local_permalink(self):
        source = '<article class="news-item warning" id="notice"><h3 class="news-title">Notice</h3><p class="news-description">Context</p></article>'
        self.assertEqual(parse_news(source)[0]['link'], 'https://ai101.health/ai-news.html#notice')
        with self.assertRaises(ValueError):
            parse_news(source.replace(' id="notice"', ''))


if __name__ == '__main__':
    unittest.main()

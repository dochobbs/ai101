# Custom Domain Setup: ai101.health

**Date:** 2026-02-04
**Status:** Plan — not yet implemented

---

## Architecture

```
ai101.health                → Landing page hub (new repo: ai101-hub)
clinicians.ai101.health     → Clinician site (existing repo: ai101)
patients.ai101.health       → Patient site (separate repo, TBD)
```

All three hosted on GitHub Pages (free). SSL provided automatically by GitHub via Let's Encrypt.

---

## Step 1: Create the Hub Repo

1. Create a new GitHub repo called `ai101-hub`
2. Add a single `index.html` — a simple landing page with:
   - AI 101 branding/logo
   - Brief description of the project
   - Two clear paths: "I'm a Clinician" and "I'm a Patient"
   - Links to `clinicians.ai101.health` and `patients.ai101.health`
3. Add a `CNAME` file containing: `ai101.health`
4. In repo **Settings > Pages**, set source to deploy from `main` branch

---

## Step 2: Configure DNS at Namecheap

Log in to Namecheap > Domain List > ai101.health > Advanced DNS.

Delete any default records (parking page, etc.), then add:

### A Records (for apex domain — ai101.health)

| Type | Host | Value           | TTL       |
|------|------|-----------------|-----------|
| A    | @    | 185.199.108.153 | Automatic |
| A    | @    | 185.199.109.153 | Automatic |
| A    | @    | 185.199.110.153 | Automatic |
| A    | @    | 185.199.111.153 | Automatic |

### CNAME Records (for subdomains)

| Type  | Host       | Value               | TTL       |
|-------|------------|---------------------|-----------|
| CNAME | www        | dochobbs.github.io. | Automatic |
| CNAME | clinicians | dochobbs.github.io. | Automatic |
| CNAME | patients   | dochobbs.github.io. | Automatic |

**Note:** The trailing dot after `dochobbs.github.io.` is standard DNS notation. Namecheap may or may not require it — add it if the form allows, omit if it complains.

---

## Step 3: Configure GitHub Pages for the Hub

1. Go to `github.com/dochobbs/ai101-hub` > Settings > Pages
2. Under "Custom domain", enter: `ai101.health`
3. Click Save
4. Wait for DNS check to pass (can take 15-60 minutes)
5. Once DNS is verified, check **"Enforce HTTPS"**

---

## Step 4: Configure GitHub Pages for the Clinician Site

1. Go to `github.com/dochobbs/ai101` > Settings > Pages
2. Under "Custom domain", enter: `clinicians.ai101.health`
3. Click Save
4. Wait for DNS check to pass
5. Check **"Enforce HTTPS"**
6. Add a `CNAME` file to the repo root containing: `clinicians.ai101.health`

**What happens to existing links:**
- `dochobbs.github.io/ai101/` will 301-redirect to `clinicians.ai101.health/`
- All deep links redirect too (e.g., `/ai101/prompting.html` → `/prompting.html`)
- Bookmarks and search rankings are preserved

---

## Step 5: Configure GitHub Pages for the Patient Site

1. Go to the patient site repo > Settings > Pages
2. Under "Custom domain", enter: `patients.ai101.health`
3. Click Save
4. Wait for DNS check to pass
5. Check **"Enforce HTTPS"**
6. Add a `CNAME` file to the repo root containing: `patients.ai101.health`

---

## Step 6: Verify Everything Works

Test each URL after DNS propagates:

- [ ] `ai101.health` loads the hub landing page
- [ ] `www.ai101.health` redirects to `ai101.health`
- [ ] `clinicians.ai101.health` loads the clinician site
- [ ] `patients.ai101.health` loads the patient site (when ready)
- [ ] `dochobbs.github.io/ai101/` redirects to `clinicians.ai101.health`
- [ ] HTTPS works on all domains (padlock icon in browser)
- [ ] Deep links work (e.g., `clinicians.ai101.health/prompting.html`)

**DNS propagation tool:** Use https://dnschecker.org to verify records are live worldwide.

---

## Order of Operations

Do these in order to minimize downtime:

1. **Create the hub repo** with CNAME file (no DNS change yet — nothing breaks)
2. **Add DNS records at Namecheap** (all at once)
3. **Configure GitHub Pages custom domain on ai101-hub** (hub goes live)
4. **Configure GitHub Pages custom domain on ai101** (clinician site goes live, old URL redirects)
5. **Configure patient repo** when ready

Between steps 2 and 4, there may be 15-60 minutes where the domain shows a GitHub 404. This is normal during DNS propagation.

---

## Costs

| Item | Cost |
|------|------|
| GitHub Pages hosting (x3 repos) | Free |
| SSL certificates (x3 domains) | Free (automatic) |
| Domain renewal (ai101.health) | ~$30-50/year (Namecheap) |

---

## Rollback

If anything goes wrong:
1. Remove the custom domain from GitHub Pages settings
2. Delete DNS records at Namecheap
3. The old `dochobbs.github.io/ai101/` URL will work again within minutes

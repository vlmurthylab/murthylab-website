# murthylab.org

Source for the Murthy Lab website. Static HTML, CSS, and JavaScript — no build
step and no framework.

    docs/          the published site (GitHub Pages serves from here)
      index.html         home: tagline, three theme cards, research sections
      people.html        PI bio, profile links, lab members, collaborators
      publications.html  all publications, filterable by theme
      join.html          open positions, linked to the U-M careers postings
      contact.html       routing page: research, trainees, patient care, address
      assets/css/        design tokens and styling
      assets/js/         hero canvas animation
      assets/img/        logo variants — see assets/img/README.md
      CNAME              custom domain for GitHub Pages

    tools/         not published; kept here for reproducibility
      Lab_Website.bib    Better BibTeX export from Zotero — source of truth
      build_pubs.py      regenerates docs/publications.html from the .bib
      README.md          how to run it

## Editing content

Home, people, join, and contact pages are hand-edited HTML. Open the file,
change the text, commit.

The top nav is duplicated in every page's `<head>`-adjacent `<nav>` block, and
`publications.html` gets its copy from the template inside
`tools/build_pubs.py`. Adding or renaming a nav item means editing all the
hand-written pages *and* that template, or the next regeneration will silently
drop the change from the publications page. Note that `404.html` uses absolute
paths (`/people.html`) because it can be served from any URL depth.

Internal links point at `/`, not `index.html`. Both work, but `index.html`
canonicalises to `/`, so linking to it sends search engines to the URL the site
itself declares non-canonical.

## Structured data

`index.html` carries a JSON-LD `@graph` describing the lab (`#lab`), the PI
(`#murthy`), and the site (`#website`). `people.html` carries a `ProfilePage`
whose `mainEntity` is the same `#murthy` person, written out in full.

Two things to keep straight:

- **One `@id` per entity.** The Person appears on both pages and must keep the
  identical `@id`; that is what says "same person" rather than "two people."
  Never give the PI a second `@id`. Equally, a bare `{"@id": ...}` reference
  only resolves *within one document* — Google will not follow it across pages,
  so anything referenced from another file must be written out with its
  `@type` and `name`.
- **`dateModified` on `people.html` is hand-maintained and will go stale.**
  It should carry the timestamp of the last human edit to the PI's titles or
  bio, as a full ISO 8601 datetime with a timezone offset
  (`2026-08-01T17:37:49+00:00`) — a date alone is rejected as invalid. **When
  you change the titles or bio on that page, update this value in the same
  commit.** Nothing enforces it.

After changing any of this, check the affected page in Google's Rich Results
Test, and watch Search Console for a week or so — errors surface there on a lag.

## Updating publications

Publications come from Zotero via Better BibTeX, not from hand-editing.

1. Add the paper in Zotero, in the **Lab Website** collection
2. Tag it with a theme if it belongs to one: `theme:vasomotor`,
   `theme:multiomics`, or `theme:ai`
3. Better BibTeX rewrites its auto-export
4. Copy that file over `tools/Lab_Website.bib`
5. Regenerate and commit:

       cd tools
       python3 build_pubs.py Lab_Website.bib -o ../docs/publications.html

Untagged papers still appear under "All" — they just won't show under a
theme filter.

## Deployment

GitHub Pages, publishing from the `docs/` folder on `main`. Commits go live in
under a minute. The custom domain and HTTPS are configured in
Settings → Pages.

## Theme colors

    amber   #D89550   coronary vasomotor and microvascular
    cyan    #77B6C6   multiomics
    violet  #A292B4   AI / ML
    ground  #161B22   page background; panels step up to #1E242D

Each theme's color appears on its card, its section statistics, and its dot in
the publications list. The logo carries all three.

## Not yet built

- Application form for the Join Us page (intended: a U-M Qualtrics or Google
  form, linked rather than embedded, so the site stays static)

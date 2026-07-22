# murthylab.org

Source for the Murthy Lab website. Static HTML, CSS, and JavaScript — no build
step and no framework.

    docs/          the published site (GitHub Pages serves from here)
      index.html         home: tagline, three theme cards, research sections
      people.html        PI bio, profile links, lab members, collaborators
      publications.html  all publications, filterable by theme
      assets/css/        design tokens and styling
      assets/js/         hero canvas animation
      assets/img/        logo variants — see assets/img/README.md
      CNAME              custom domain for GitHub Pages

    tools/         not published; kept here for reproducibility
      Lab_Website.bib    Better BibTeX export from Zotero — source of truth
      build_pubs.py      regenerates docs/publications.html from the .bib
      README.md          how to run it

## Editing content

Home and people pages are hand-edited HTML. Open the file, change the text,
commit.

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
    ground  #0B1220   page background; panels step up to #131C2E

Each theme's color appears on its card, its section statistics, and its dot in
the publications list. The logo carries all three.

## Not yet built

- Join Us (postings pending approval)
- Contact

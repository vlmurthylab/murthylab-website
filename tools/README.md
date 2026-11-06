# Updating the publications page

When you add papers in Zotero, Better BibTeX refreshes `Lab_Website.bib`. Copy it over the one in this directory, then regenerate.

Leave out Zotero's `file` field, which is the path of each PDF on your computer (with your user name); this repository is public. In Zotero, open Settings, Better BibTeX, Export, Fields, and add `file` to "Fields to omit from export". `build_pubs.py` warns if the field is there, the repository's commit hook (`hooks/pre-commit.local`) refuses to commit `Lab_Website.bib` while it holds `file` fields, and GitHub's check (`.github/workflows/bib-check.yml`) runs on every push and pull request; when `main`'s rules make it a required check, a pull request can't be merged while it fails. If the automatic export has its own copy of that setting (Settings, Better BibTeX, Automatic export), set it there too.

Regenerate the page from it:

    python3 build_pubs.py Lab_Website.bib -o ../docs/publications.html

Takes about a second. No dependencies beyond Python 3.8+.

It prints a summary so you can sanity-check the result:

    Wrote ../publications.html — 314 publications
    (vasomotor 67, multiomics 40, ai 12, untagged 195)

## Theme tags

Themes come from Zotero tags in the form:

    theme:vasomotor
    theme:multiomics
    theme:ai

Tag new papers in Zotero as you add them. Untagged papers still appear
under "All" — they just won't show under a theme filter.

## Changing the filter buttons

Edit `FILTER_LABELS` near the top of `build_pubs.py`. The first element of
each pair must match the tag suffix; the second is the visible label.

## Adding a fourth theme

1. Add `theme:yourtag` to papers in Zotero
2. Add `('yourtag', 'Your Label')` to `FILTER_LABELS`
3. Add a color rule to `assets/css/main.css`:

       .d-yourtag{background:#YOURHEX}

## Note on the header

`build_pubs.py` writes its own nav bar, including the inline logo. If you
change the header in `index.html` or `people.html`, make the same change to
the `NAV` string in this script or the next rebuild will revert it.

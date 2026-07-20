#!/usr/bin/env python3
"""
Regenerate publications.html from a Better BibTeX export.

Usage:
    python3 build_pubs.py Lab_Website.bib > ../publications.html

    # or write in place
    python3 build_pubs.py Lab_Website.bib -o ../publications.html

No dependencies beyond the Python standard library (3.8+).

Theme tags come from Zotero tags of the form  theme:vasomotor,
theme:multiomics, theme:ai.  Untagged papers still appear under "All".
"""

import argparse
import html
import json
import re
import sys
from collections import Counter

from journal_names import JOURNALS

_unmapped_journals = set()


def _journal(name):
    """Return the journal's masthead form; record anything unmapped."""
    name = ' '.join(name.split())
    if not name:
        return name
    for cand in (name,
                 name.replace('\\&', '&'),
                 name.replace('&', '\\&')):
        if cand in JOURNALS:
            return JOURNALS[cand]
    _unmapped_journals.add(name)
    return name


# --------------------------------------------------------------------------
# BibTeX parsing
# --------------------------------------------------------------------------

ACCENTS = {
    r'\{\\`e\}': 'è', r"\{\\'e\}": 'é', r'\{\\^e\}': 'ê', r'\{\\"e\}': 'ë',
    r"\{\\'a\}": 'á', r'\{\\`a\}': 'à', r'\{\\^a\}': 'â', r'\{\\"a\}': 'ä',
    r"\{\\'o\}": 'ó', r'\{\\`o\}': 'ò', r'\{\\^o\}': 'ô', r'\{\\"o\}': 'ö',
    r"\{\\'i\}": 'í', r'\{\\`i\}': 'ì', r'\{\\"i\}': 'ï',
    r"\{\\'u\}": 'ú', r'\{\\"u\}': 'ü',
    r'\{\\~n\}': 'ñ', r'\{\\c\{c\}\}': 'ç', r'\{\\v\{s\}\}': 'š',
    r'\{\\ss\}': 'ß', r'\{\\aa\}': 'å', r'\{\\o\}': 'ø',
}


# LaTeX escapes that stand for real characters.
# Zotero re-escapes these on every BibTeX export, so they must be translated
# here rather than fixed in the library.
LATEX_LITERALS = {
    r'\\textbar\s*':      '|',
    r'\\textemdash\s*':   '\u2014',
    r'\\textendash\s*':   '\u2013',
    r'\\textquotesingle\s*': "'",
    r'\\textasciitilde\s*':  '~',
    # \textbackslash is deliberately absent: it would yield a literal
    # backslash that the stray-command pass below would then re-consume.
    r'\\&':               '&',
    r'\\%':               '%',
    r'\\_':               '_',
    r'\\\$':              '$',
}


def _clean(value):
    for pattern, char in ACCENTS.items():
        value = re.sub(pattern, char, value)
    # Translate known literals before stripping unrecognised commands below,
    # which would otherwise swallow them along with the following space.
    # The replacement is passed as a function so that characters such as
    # a backslash are inserted literally rather than parsed as a template.
    for pattern, char in LATEX_LITERALS.items():
        value = re.sub(pattern, lambda _m, c=char: c, value)
    value = re.sub(r'\\[a-zA-Z]+\s*', '', value)   # stray commands
    return ' '.join(re.sub(r'[{}]', '', value).split())


def _field(body, key):
    """Pull one field out of an entry body."""
    m = re.search(
        r'\b' + key + r'\s*=\s*\{(.*?)\}\s*,?\s*(?=\n\s*\w+\s*=|\s*$)',
        body, re.S)
    if m:
        return _clean(m.group(1))
    m = re.search(r'\b' + key + r'\s*=\s*(\d+)', body)
    return m.group(1) if m else ''


def parse_bib(path):
    text = open(path, encoding='utf-8').read()
    entries = re.findall(r'@(\w+)\{([^,]+),(.*?)\n\}', text, re.S)
    out = []
    for _type, key, body in entries:
        tags = [t.strip() for t in _field(body, 'keywords').split(',') if t.strip()]
        out.append({
            'key': key,
            'title': _field(body, 'title'),
            'author': _field(body, 'author'),
            'year': _field(body, 'year'),
            'journal': _journal(_field(body, 'journal') or _field(body, 'booktitle')),
            'volume': _field(body, 'volume'),
            'pages': _field(body, 'pages'),
            'doi': _field(body, 'doi'),
            'themes': [t.split(':', 1)[1] for t in tags if t.startswith('theme:')],
        })
    return out


# --------------------------------------------------------------------------
# Formatting
# --------------------------------------------------------------------------

def format_authors(raw, highlight='Murthy'):
    """`Last, First M and Last, First` -> `Last FM, Last F`, PI bolded."""
    if not raw:
        return ''
    names = []
    for n in raw.split(' and '):
        n = n.strip()
        if ',' in n:
            last, first = n.split(',', 1)
            initials = ''.join(w[0] for w in first.split() if w[:1].isalpha())
            names.append('{} {}'.format(last.strip(), initials))
        else:
            names.append(n)
    if len(names) > 7:
        names = names[:6] + ['&hellip;', names[-1]]
    joined = ', '.join(names).replace(', &hellip;,', ' &hellip;')
    return re.sub(r'\b(' + highlight + r' \w*)', r'<strong>\1</strong>', joined)


def format_meta(pub):
    bits = []
    if pub['journal']:
        bits.append('<span class="jr">{}</span>'.format(html.escape(pub['journal'])))
    if pub['year']:
        bits.append(pub['year'])
    if pub['volume']:
        v = pub['volume']
        if pub['pages']:
            v += ':' + pub['pages']
        bits.append(v)
    return ' &middot; '.join(bits)


# --------------------------------------------------------------------------
# Page assembly
# --------------------------------------------------------------------------

NAV = '''<nav class="nav"><div class="wrap">
<a class="brand" href="index.html"><svg class="mark" viewBox="0 0 120 120" aria-hidden="true" focusable="false"><g fill="none" stroke-linecap="round"><path d="M60 24 C60 48 60 56 42 70 C26 82 20 93 20 110" stroke="currentColor" stroke-width="6"/><path d="M60 50 C75 60 83 72 91 91" stroke="currentColor" stroke-width="4.3"/><path d="M42 70 C54 80 57 91 59 108" stroke="var(--mark-amber)" stroke-width="3.1"/></g><g fill="var(--mark-cyan)"><circle cx="18" cy="112" r="4.6"/><circle cx="48" cy="114" r="4.6"/><circle cx="86" cy="100" r="4.6"/></g><g fill="var(--mark-cyan)" fill-opacity=".7"><circle cx="72" cy="113" r="3.3"/><circle cx="99" cy="106" r="3.3"/></g><g fill="var(--mark-violet)"><circle cx="59" cy="110" r="4.6"/><circle cx="30" cy="118" r="3.3" fill-opacity=".7"/></g></svg><span class="brand-name">Murthy Lab</span><span class="brand-inst">University of Michigan</span></a>
<a class="lnk" href="index.html#research">Research</a>
<a class="lnk" href="people.html">People</a>
<a class="lnk" href="publications.html" aria-current="page">Publications</a>
<a class="lnk" href="join.html">Join Us</a>
</div></nav>'''

FOOTER = '''<footer><div class="wrap">
<span>Murthy Lab &middot; Division of Cardiovascular Medicine &middot; University of Michigan</span>
</div></footer>'''

PROFILES = ('<p class="pub-profiles">Also on '
            '<a href="https://scholar.google.com/citations?user=nNET6osAAAAJ&amp;hl=en">'
            'Google Scholar</a> and '
            '<a href="https://orcid.org/0000-0002-7901-1321">ORCID</a>.</p>')

FILTER_LABELS = [
    ('all',        'All'),
    ('vasomotor',  'Coronary Microvascular &amp; Vasomotor'),
    ('multiomics', 'Multiomics'),
    ('ai',         'AI &amp; ML'),
]

SCRIPT = '''<script>
(function(){
  var btns=document.querySelectorAll('.fb'),
      pubs=document.querySelectorAll('.pub'),
      yrs=document.querySelectorAll('.yr'),
      cnt=document.getElementById('count');
  function apply(f){
    var n=0;
    pubs.forEach(function(p){
      var ok = f==='all' || (' '+p.dataset.themes+' ').indexOf(' '+f+' ')>-1;
      p.style.display = ok?'':'none'; if(ok) n++;
    });
    yrs.forEach(function(y){
      var el=y.nextElementSibling, any=false;
      while(el && !el.classList.contains('yr')){
        if(el.classList.contains('pub') && el.style.display!=='none'){any=true;break;}
        el=el.nextElementSibling;
      }
      y.style.display=any?'':'none';
    });
    cnt.textContent = n + (n===1?' publication':' publications');
    btns.forEach(function(b){b.setAttribute('aria-pressed', b.dataset.f===f?'true':'false');});
  }
  btns.forEach(function(b){b.addEventListener('click',function(){apply(b.dataset.f);});});
})();
</script>'''


def build(pubs):
    pubs.sort(key=lambda p: (-(int(p['year']) if p['year'].isdigit() else 0),
                             p['title'].lower()))

    counts = Counter(t for p in pubs for t in p['themes'])
    counts['all'] = len(pubs)

    buttons = ''.join(
        '<button class="fb" data-f="{k}" aria-pressed="{a}">{label}'
        '<span class="n">{n}</span></button>'.format(
            k=key, label=label, n=counts.get(key, 0),
            a='true' if key == 'all' else 'false')
        for key, label in FILTER_LABELS)

    rows, current_year = [], None
    for p in pubs:
        if p['year'] != current_year:
            rows.append('<p class="yr">{}</p>'.format(p['year'] or 'n.d.'))
            current_year = p['year']
        dots = ''.join(
            '<span class="dot d-{t}" title="{t}"></span>'.format(t=t)
            for t in p['themes'])
        title = html.escape(p['title'])
        if p['doi']:
            title_html = ('<a class="ti" href="https://doi.org/{doi}">{dots}{t}</a>'
                          .format(doi=html.escape(p['doi']), dots=dots, t=title))
        else:
            title_html = '<span class="ti">{dots}{t}</span>'.format(dots=dots, t=title)
        rows.append(
            '<div class="pub" data-themes="{themes}">{title}'
            '<div class="meta">{authors}<br>{meta}</div></div>'.format(
                themes=' '.join(p['themes']),
                title=title_html,
                authors=format_authors(p['author']),
                meta=format_meta(p)))

    body = '''<section class="sec" style="border-top:0"><div class="wrap">
<h2 class="sec-h">Publications</h2>
{profiles}
<div class="filters">{buttons}</div>
<p class="count" id="count">{n} publications</p>
<div id="pubs">{rows}</div>
</div></section>'''.format(profiles=PROFILES, buttons=buttons,
                           n=len(pubs), rows=''.join(rows))

    return '''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Publications &middot; Murthy Lab</title>
<meta name="description" content="Publications from the Murthy Lab: cardiac PET, microvascular dysfunction, multiomics, and machine learning.">
<link rel="canonical" href="https://murthylab.org/publications.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Murthy Lab">
<meta property="og:title" content="Publications &middot; Murthy Lab">
<meta property="og:description" content="Cardiac PET, coronary microvascular dysfunction, multiomic biomarkers, and machine learning.">
<meta property="og:url" content="https://murthylab.org/publications.html">
<meta property="og:image" content="https://murthylab.org/assets/img/og-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Murthy Lab, University of Michigan">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Publications &middot; Murthy Lab">
<meta name="twitter:description" content="Cardiac PET, coronary microvascular dysfunction, multiomic biomarkers, and machine learning.">
<meta name="twitter:image" content="https://murthylab.org/assets/img/og-card.png">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/main.css">
</head><body>{nav}{body}{footer}{script}</body></html>'''.format(
        nav=NAV, body=body, footer=FOOTER, script=SCRIPT)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('bib', help='path to Lab_Website.bib')
    ap.add_argument('-o', '--out', help='write here instead of stdout')
    args = ap.parse_args()

    pubs = parse_bib(args.bib)
    if not pubs:
        sys.exit('No entries parsed from {} — is it a BibTeX file?'.format(args.bib))

    page = build(pubs)

    if args.out:
        open(args.out, 'w', encoding='utf-8').write(page)
        counts = Counter(t for p in pubs for t in p['themes'])
        print('Wrote {} — {} publications '
              '(vasomotor {}, multiomics {}, ai {}, untagged {})'.format(
                  args.out, len(pubs),
                  counts['vasomotor'], counts['multiomics'], counts['ai'],
                  sum(1 for p in pubs if not p['themes'])),
              file=sys.stderr)
    else:
        sys.stdout.write(page)


if __name__ == '__main__':
    main()

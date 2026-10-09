# Expression-of-interest form

A form for people who want to be considered for roles that are not currently
posted. It collects a CV and free-text research experience, then asks about
skills on one of two tracks, chosen by the applicant:

- **Data and computation** — a novice-to-expert grid for R, Python, SQL,
  Git/GitHub, the Unix command line and deep learning frameworks, then
  checkboxes for AI/ML libraries, infrastructure, methods and data types.
- **Sample collection and clinical research** — the same novice-to-expert
  grid for consent, study visits, phlebotomy, biospecimen processing, REDCap
  and IRB work, then checkboxes for lab, biobanking and shipping experience
  and certifications.

Applicants who pick "Both" see both sections.

The site is static (GitHub Pages), so it cannot receive form submissions or
file uploads itself. The form lives in **U-M Qualtrics** and the Join Us page
links to it.

Why Qualtrics rather than the alternatives:

- **U-M licensed**, so CVs and contact details stay on a university-approved
  platform instead of a third-party form service.
- **File upload without a login.** Google Forms only allows uploads from
  respondents signed in to a Google account, which turns away many applicants.
- Responses export to CSV/Excel, and uploaded files download in bulk.

## Building it (about 15 minutes)

1. Sign in at <https://umich.qualtrics.com> and create a new project →
   Survey → *From a file*. Upload `qualtrics-import.txt` from this folder.
   That creates every block and question except the file upload.
2. In the **CV and submission** block, directly after the "Please upload your
   CV or resume below" text, add a question of type **File Upload**. Restrict
   it to PDF, DOC and DOCX, and make it required.
3. Mark as required (*Response requirements → Force response*): name, email,
   current position, degree, track, position type, research experience,
   onsite, both proficiency grids, the CV upload, and the confirmation box.
4. On the email question, add validation → *Email address*.
5. On "If other, please describe" (under position type), add display logic
   so it only shows when *Other* is selected.
6. **Route each applicant to their track.** Open *Survey flow* and, before
   the **Data skills** block, add a *Branch*: show it if the track question is
   "Data and computation…" *or* "Both". Put the **Sample collection skills**
   block under a second branch: "Sample collection…" *or* "Both". The other
   blocks stay outside any branch. (The import file cannot express this, so
   until it is done every applicant sees both sections.)
7. Survey options:
   - *Security → Prevent multiple submissions*: off (people may legitimately
     resubmit an updated CV).
   - *Responses → Anonymize responses*: off — you need the contact details.
   - *Survey termination*: a custom end-of-survey message, e.g. "Thank you.
     We read every submission and will be in touch if a suitable role opens."
8. *Workflows → Email task*: send a notification to the lab inbox on each
   submission, so nothing sits unread.
9. Under *Look and feel*, choose a U-M theme if available.
10. Publish, then copy the anonymous link (it looks like
   `https://umich.qualtrics.com/jfe/form/SV_xxxxxxxxxxxxxxx`).

## Linking it from the site

`docs/join.html` has an "Expressing interest" section whose link is the
placeholder `QUALTRICS_FORM_URL`. Replace it with the anonymous link from
step 10 before that change is merged to `main`; until then the section must not
go live. `docs/contact.html` points readers to the Join Us page, so it needs no
link of its own.

To check nothing was missed:

    grep -rn QUALTRICS_FORM_URL docs/

should print nothing once the link is in.

## Changing the questions

Edit questions in Qualtrics directly; this file is only the starting point.
If you want this file to remain an accurate record, export the survey
afterwards (*Tools → Import/Export → Export survey*, which produces a `.qsf`)
and commit that here alongside it.

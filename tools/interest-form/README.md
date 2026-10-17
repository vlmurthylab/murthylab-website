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
2. In the **CV and submission** block, change the question type of the
   "Please upload your CV or resume" text to **File upload**, so the
   instruction becomes the upload question. Turn on *Force response*, then
   *Add validation → Content type → Extensions* with `doc, docx, odt, pdf`. (The
   ready-made *PDF* and *Document* types each cover only part of that list:
   *Document* is doc, docx, txt and odt, without PDF.) File upload is a paid
   Qualtrics add-on; if the question type is missing, ask U-M's Qualtrics
   support.
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
8. **Email notification.** *Workflows → Create a workflow → Started when an
   event is received → Survey response*, then add an **Email** task:
   - **Subject:** `[Murthy Lab interest] ` followed by the name and track
     answers. Insert both with the **{a}** piped-text button rather than
     typing `${q://...}` codes, because the question numbers depend on the
     import.
   - **Body:** the answers you want at a glance (email, position type,
     start date, research experience), again via **{a}**.
   - **CV link:** insert the File Upload question's file link with **{a}**
     *from inside the workflow*; links copied from the survey editor are
     temporary. Opening it asks for a U-M Qualtrics sign-in. Leave
     uploaded files requiring sign-in: making them viewable by anyone with
     the link would let a forwarded email expose an applicant's CV.
   - Qualtrics cannot attach the uploaded file itself to the email.
9. **Look and feel** (paintbrush icon), to match murthylab.org:
   - *Theme:* a blank/Qualtrics default theme rather than a U-M one, if U-M
     allows it (the U-M themes carry their own colours).
   - *Logo / header:* upload `qualtrics-header.png` from this folder, the site
     header's mark and name on the site background. Regenerate it from the
     inline SVG in any page's nav if the brand changes.
   - *Colours:* background `#161B22`, question text `#EFF1F4`, primary
     (buttons, selected answers) `#D89550`. If the layout has a foreground
     contrast setting, choose the light-on-dark option.
   - *Fonts:* a sans serif (Helvetica or Arial) for headings and Georgia for
     body text, the closest stock matches to the site's Inter and Iowan Old
     Style.
   - Preview on a phone, and check the matrix grids and the upload button are
     still readable on the dark background; if any control is hard to see,
     fall back to a white content area with the dark header.
10. Publish, then copy the anonymous link (it looks like
   `https://umich.qualtrics.com/jfe/form/SV_xxxxxxxxxxxxxxx`).

## Filing the emails in Outlook

Once the first test email arrives, right-click it → *Rules → Create rule*:
**Subject contains `[Murthy Lab interest]`** → **Move to folder** (e.g. "Lab
applicants"). Match the subject, not the sender: Qualtrics sends from a shared
no-reply address used by every U-M survey.

## Saving CVs to OneDrive (planned, not built)

Power Automate cannot do this here: the Michigan Medicine environment has no
Qualtrics connector, and the HTTP connector is premium. The Qualtrics API is
available, though (a personal API token can be generated under *Account
settings → Qualtrics IDs*), so the plan is a small script on a personal U-M
Mac that runs daily, downloads new CVs into a synced OneDrive folder with
readable names, and appends each applicant to a spreadsheet there. It can
also email each CV as an attachment (Qualtrics cannot), most likely by
scripting Apple Mail with the U-M account added; to be confirmed on the Mac,
since managed Macs may block adding the account or the automation prompt. Until it
exists, download uploaded files in bulk from *Data & Analysis* now and then.

The API token gives full access to the Qualtrics account. Keep it on the Mac
only, never in this repository, which is public.

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

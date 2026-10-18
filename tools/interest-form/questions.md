# Murthy Lab - Expression of Interest

Generated from `survey.qsf` by `qsf_to_md.py`. Do not edit by hand.

## Introduction

- **`intro`** (DB): Murthy Lab · Expression of interest Use this form if you would like to be considered for future roles in the Murthy Lab at the University of Michigan. It is not an application for a posted position: those must be submitted through the University of Michigan careers site linked from murthylab.org/join.html. We try to read every submission carefully, but we may not be able to reply to each one. We will contact you if a role opens that fits your background. The form takes about ten minutes; please have your CV or resume ready to upload as a PDF or Word file.

## About you

- **`name`** (TE, required): Full name
- **`email`** (TE, required, email): Email address
- **`phone`** (TE): Phone (optional)
- **`position`** (TE, required): Current position and institution or employer
- **`degree`** (MC, required): Highest degree completed or in progress
  - High school or equivalent
  - Bachelor's (in progress)
  - Bachelor's
  - Master's (in progress)
  - Master's
  - PhD (in progress)
  - PhD
  - MD or DO (in progress)
  - MD or DO
  - MD/PhD
  - Other doctoral degree
- **`field`** (TE): Field of study for that degree
- **`profile`** (TE): LinkedIn, GitHub, Google Scholar, or personal website (optional)

## Interest

- **`track`** (MC, required): Our work divides into two broad areas. Which interests you?
  - Data and computation: data science, machine learning, data management, biostatistics
  - Sample collection and clinical research: participant recruitment, study visits, biospecimen collection and processing, regulatory work
  - Both
- **`stage`** (MC, required): What kind of position are you looking for?
  - Staff position
  - Postdoctoral fellowship
  - Graduate student research
  - Medical student or resident research
  - Undergraduate research
  - Other
- **`stage_other`** (TE): If other, please describe
  - *Shown only: If What kind of position are you looking for? Other Is Selected*
- **`availability`** (MC, required): Time commitment
  - Full-time
  - Part-time
  - Summer or other fixed term
  - Flexible
- **`start`** (TE): Earliest date you could start (month and year)
- **`onsite`** (MC, required): Our positions are onsite in Ann Arbor, Michigan. Are you able to work onsite?
  - Yes
  - Yes, after relocating
  - No
  - Not sure

## Research experience

- **`research_exp`** (TE, required): Describe your prior research experience. For each project: the question, your specific role, the methods you used, and how long you worked on it.
- **`research_best`** (TE): Which piece of work are you proudest of, and what did you personally contribute to it?
- **`pubs`** (TE): Publications, preprints, abstracts, or presentations (optional). Citations or links are fine.
- **`why`** (TE): What draws you to this lab's work, and what would you hope to learn or do here?

## Data skills

*Shown only: If Our work divides into two broad areas. Which interests you? Data and computation: data science, machine learning, data management, biostatistics Is Selected Or Our work divides into two broad areas. Which interests you? Both Is Selected*

- **`data_intro`** (DB): Data and computation skills. Check anything you have used in real work (a project, thesis, job, or publication), not only in coursework. Leave boxes unchecked if unsure; we will ask about specifics in conversation.
- **`data_level`** (Matrix, required): Rate your proficiency with each of these.
  - R
  - Python
  - SQL
  - Git / GitHub
  - Unix command line
  - Deep learning frameworks (PyTorch, TensorFlow, JAX)
  - Scale: Not used / Novice: coursework or short scripts / Intermediate: used regularly in a project / Advanced: built pipelines or analyses others rely on / Expert: wrote packages or production code, or teach it to others
- **`lang`** (MC): Other programming languages
  - SAS
  - Stata
  - MATLAB
  - Julia
  - C / C++
  - Java or Scala
- **`ai_libs`** (MC): AI and machine learning libraries
  - PyTorch
  - TensorFlow / Keras
  - JAX
  - scikit-learn
  - Hugging Face Transformers
  - XGBoost / LightGBM
  - PyTorch Lightning
  - tidymodels or caret (R)
  - LLM APIs or frameworks (e.g. OpenAI, Anthropic, LangChain)
- **`data_tools`** (MC): Data and computing infrastructure
  - High-performance computing cluster (e.g. Slurm)
  - Cloud computing (AWS, Google Cloud, Azure)
  - Docker or other containers
  - Spark, Dask, or Polars for large data
  - Relational databases (PostgreSQL, MySQL, SQL Server)
  - Workflow managers (Snakemake, Nextflow, Airflow)
  - Data visualization (ggplot2, matplotlib, plotly)
- **`methods`** (MC): Analytic methods
  - Regression modeling
  - Survival / time-to-event analysis
  - Causal inference
  - Mendelian randomization or other genetic epidemiology
  - Mixed-effects or longitudinal models
  - Deep learning model training
  - Self-supervised or foundation-model pretraining
  - Signal or time-series processing
- **`domain`** (MC): Data types you have worked with
  - Proteomics (Olink, SomaScan, or mass spectrometry)
  - Metabolomics
  - Genomics / GWAS
  - Electrocardiogram (ECG) or other physiologic waveforms
  - Medical imaging (PET, CT, MRI, echocardiography)
  - Electronic health record data (Epic, OMOP, PCORnet)
  - Large cohorts or biobanks (UK Biobank, All of Us, MESA, Framingham, etc.)
  - Claims or registry data
- **`data_other`** (TE): Other data or computing experience we should know about (optional)

## Sample collection skills

*Shown only: If Our work divides into two broad areas. Which interests you? Sample collection and clinical research: participant recruitment, study visits, biospecimen collection and processing, regulatory work Is Selected Or Our work divides into two broad areas. Which interests you? Both Is Selected*

- **`sample_intro`** (DB): Sample collection and clinical research skills. Check anything you have done in real work, not only in training. Leave boxes unchecked if unsure; we will ask about specifics in conversation.
- **`sample_level`** (Matrix, required): Rate your experience with each of these.
  - Participant recruitment and informed consent
  - Study visits and data collection with participants
  - Phlebotomy or other biospecimen collection
  - Biospecimen processing (centrifugation, aliquoting)
  - REDCap
  - IRB submissions and regulatory management
  - Scale: Not done / Novice: trained or observed / Intermediate: done independently on a study / Advanced: responsible for it across a study / Expert: trained others or set up the process
- **`sample_exp`** (MC): Other experience
  - Biobanking and freezer inventory systems (e.g. FreezerPro, OpenSpecimen)
  - Laboratory assays (ELISA, PCR, or similar)
  - Shipping biological samples (IATA / dangerous goods)
  - Standard operating procedure (SOP) writing
  - Quality control and sample tracking
  - Vendor or core facility coordination
  - Clinical trial or multicenter study operations
  - Electronic health record chart review
  - Working in a hospital or clinic setting
  - Spanish or another language used with participants
- **`certs`** (MC): Current certifications or training
  - Human subjects research (CITI or PEERRS)
  - Good Clinical Practice (GCP)
  - Phlebotomy certification
  - IATA / dangerous goods shipping
  - Bloodborne pathogens
  - Clinical research professional (ACRP or SOCRA)
- **`sample_other`** (TE): Other clinical or laboratory experience we should know about (optional)

## CV and submission

- **`cv_upload`** (FileUpload, required, files: doc, docx, pdf, odt): Please upload your CV or resume below (PDF preferred though Word documents are also accepted, 10 MB maximum).
- **`source`** (MC): How did you hear about the lab?
  - Lab website
  - A current or former lab member
  - A publication or presentation
  - Faculty member or mentor
  - Social media
  - Other
- **`consent`** (MC, required): Confirmation
  - I confirm the information above is accurate, and I understand this form is an expression of interest, not an application for a posted University of Michigan position.

## Options

- Back button: true
- Survey title: Murthy Lab – Expression of interest
- Theme: *simple, background #161b22, primary #77b6c6
- Uploaded files require sign-in: true

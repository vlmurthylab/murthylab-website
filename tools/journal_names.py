"""Canonical display names for journals appearing in Lab_Website.bib.

Keys are the raw strings as stored by Zotero (PubMed's form: sentence case,
with ' : official publication of ...' subtitles appended).  Values are the
journal's own title-cased name as it appears on its masthead.

Anything not in this map is left untouched and reported by build_pubs.py so it
can be added here rather than guessed at.
"""

JOURNALS = {
 # --- most frequent ---
 "Journal of nuclear cardiology : official publication of the American Society of Nuclear Cardiology":
     "Journal of Nuclear Cardiology",
 "Circulation": "Circulation",
 "Circulation. Cardiovascular imaging": "Circulation: Cardiovascular Imaging",
 "Journal of nuclear medicine : official publication, Society of Nuclear Medicine":
     "Journal of Nuclear Medicine",
 "Journal of the American College of Cardiology": "Journal of the American College of Cardiology",
 "JACC. Cardiovascular imaging": "JACC: Cardiovascular Imaging",
 "JAMA cardiology": "JAMA Cardiology",
 "medRxiv : the preprint server for health sciences": "medRxiv",
 "Journal of the American Heart Association": "Journal of the American Heart Association",
 "European journal of nuclear medicine and molecular imaging":
     "European Journal of Nuclear Medicine and Molecular Imaging",
 "Nutrition, metabolism, and cardiovascular diseases : NMCD":
     "Nutrition, Metabolism & Cardiovascular Diseases",
 "Circulation research": "Circulation Research",
 "Journal of cardiac failure": "Journal of Cardiac Failure",
 "The American journal of cardiology": "The American Journal of Cardiology",
 "European heart journal": "European Heart Journal",
 "NEJM AI": "NEJM AI",
 "GeroScience": "GeroScience",
 "JAMA internal medicine": "JAMA Internal Medicine",
 "Aging cell": "Aging Cell",

 # --- cardiology / vascular ---
 "Atherosclerosis": "Atherosclerosis",
 "Circulation. Heart failure": "Circulation: Heart Failure",
 "Current cardiology reports": "Current Cardiology Reports",
 "Current Cardiology Reports": "Current Cardiology Reports",
 "European journal of preventive cardiology": "European Journal of Preventive Cardiology",
 "Arteriosclerosis, thrombosis, and vascular biology":
     "Arteriosclerosis, Thrombosis, and Vascular Biology",
 "Cardiovascular research": "Cardiovascular Research",
 "International journal of cardiology": "International Journal of Cardiology",
 "JACC. Cardiovascular interventions": "JACC: Cardiovascular Interventions",
 "Circulation. Genomic and precision medicine": "Circulation: Genomic and Precision Medicine",
 "Circulation. Arrhythmia and electrophysiology": "Circulation: Arrhythmia and Electrophysiology",
 "Circulation. Population health and outcomes": "Circulation: Population Health and Outcomes",
 "JACC. Advances": "JACC: Advances",
 "JACC. Asia": "JACC: Asia",
 "JACC": "JACC",
 "Coronary artery disease": "Coronary Artery Disease",
 "Cardiology in review": "Cardiology in Review",
 "The Canadian journal of cardiology": "Canadian Journal of Cardiology",
 "Cardiovascular journal of Africa": "Cardiovascular Journal of Africa",
 "Clinical cardiology": "Clinical Cardiology",
 "American heart journal": "American Heart Journal",
 "Open heart": "Open Heart",
 "ESC heart failure": "ESC Heart Failure",
 "Heart (British Cardiac Society)": "Heart",
 "Heart, lung & circulation": "Heart, Lung and Circulation",
 "Stroke": "Stroke",
 "Hypertension (Dallas, Tex. : 1979)": "Hypertension",
 "American journal of hypertension": "American Journal of Hypertension",
 "Vascular medicine (London, England)": "Vascular Medicine",
 "Circulation journal : official journal of the Japanese Circulation Society":
     "Circulation Journal",
 "The Journal of heart and lung transplantation : the official publication of the International Society for Heart Transplantation":
     "The Journal of Heart and Lung Transplantation",

 # --- imaging ---
 "The international journal of cardiovascular imaging":
     "The International Journal of Cardiovascular Imaging",
 "Journal of cardiovascular computed tomography": "Journal of Cardiovascular Computed Tomography",
 "Journal of cardiovascular magnetic resonance : official journal of the Society for Cardiovascular Magnetic Resonance":
     "Journal of Cardiovascular Magnetic Resonance",
 "Journal of the American Society of Echocardiography : official publication of the American Society of Echocardiography":
     "Journal of the American Society of Echocardiography",
 "Journal of magnetic resonance imaging : JMRI": "Journal of Magnetic Resonance Imaging",
 "Magnetic resonance in medicine": "Magnetic Resonance in Medicine",
 "Radiology. Cardiothoracic imaging": "Radiology: Cardiothoracic Imaging",
 "Radiographics : a review publication of the Radiological Society of North America, Inc":
     "RadioGraphics",
 "European heart journal. Cardiovascular Imaging": "European Heart Journal: Cardiovascular Imaging",
 "IEEE transactions on medical imaging": "IEEE Transactions on Medical Imaging",
 "Molecular imaging and biology": "Molecular Imaging and Biology",
 "Clinical nuclear medicine": "Clinical Nuclear Medicine",
 "Journal of nuclear medicine technology": "Journal of Nuclear Medicine Technology",
 "BJRtextbar Open": "BJR|Open",
 "BJRtextbarOpen": "BJR|Open",
 "BJR|Open": "BJR|Open",

 # --- general medicine ---
 "JAMA": "JAMA",
 "Annals of internal medicine": "Annals of Internal Medicine",
 "Lancet (London, England)": "The Lancet",
 "The Lancet. Digital health": "The Lancet Digital Health",
 "European heart journal. Digital health": "European Heart Journal: Digital Health",
 "European heart journal. Quality of care & clinical outcomes":
     "European Heart Journal: Quality of Care and Clinical Outcomes",
 "Journal of general internal medicine": "Journal of General Internal Medicine",
 "BMJ open": "BMJ Open",
 "PloS one": "PLOS ONE",
 "Nature communications": "Nature Communications",
 "Nature medicine": "Nature Medicine",
 "Cell": "Cell",
 "Cell reports. Medicine": "Cell Reports Medicine",
 "Innovation Medicine": "Innovation Medicine",

 # --- metabolism / endocrine / nutrition ---
 "Diabetes care": "Diabetes Care",
 "Diabetologia": "Diabetologia",
 "Journal of diabetes": "Journal of Diabetes",
 "Obesity (Silver Spring, Md.)": "Obesity",
 "Metabolites": "Metabolites",
 "The Journal of clinical endocrinology and metabolism":
     "The Journal of Clinical Endocrinology & Metabolism",
 "The American journal of clinical nutrition": "The American Journal of Clinical Nutrition",
 "Journal of lipid research": "Journal of Lipid Research",

 # --- basic science / other ---
 "The Journal of clinical investigation": "The Journal of Clinical Investigation",
 "JCI insight": "JCI Insight",
 "Journal of molecular biology": "Journal of Molecular Biology",
 "Biochemistry": "Biochemistry",
 "Structure (London, England : 1993)": "Structure",
 "Nucleic acids research": "Nucleic Acids Research",
 "BMC genomics": "BMC Genomics",
 "Frontiers in genetics": "Frontiers in Genetics",
 "Pharmacology & therapeutics": "Pharmacology & Therapeutics",
 "The journals of gerontology. Series A, Biological sciences and medical sciences":
     "The Journals of Gerontology: Series A",
 "Kidney international": "Kidney International",
 "Journal of nephrology": "Journal of Nephrology",
 "Journal of the American Society of Nephrology : JASN":
     "Journal of the American Society of Nephrology",
 "Journal of clinical oncology : official journal of the American Society of Clinical Oncology":
     "Journal of Clinical Oncology",
 "International journal of radiation oncology, biology, physics":
     "International Journal of Radiation Oncology, Biology, Physics",
 "Journal of medical virology": "Journal of Medical Virology",
 "The Science of the total environment": "Science of The Total Environment",
 "Research square": "Research Square",

 # PubMed strings that arrive with LaTeX-escaped ampersands
 "European heart journal. Quality of care \\& clinical outcomes":
     "European Heart Journal: Quality of Care and Clinical Outcomes",
 "Heart, lung \\& circulation": "Heart, Lung and Circulation",
 "Pharmacology \\& therapeutics": "Pharmacology & Therapeutics",
}

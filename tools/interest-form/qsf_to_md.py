"""Write a readable summary of a Qualtrics .qsf export as Markdown.

    python3 qsf_to_md.py survey.qsf -o questions.md

The .qsf is the record of the live survey; this summary exists so changes
to it can be read in a diff.
"""
import argparse
import html
import json
import re


def clean(text):
    text = re.sub(r"<br\s*/?>", " ", text or "")
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def logic(cond):
    parts = []
    for key in sorted(k for k in cond if k.isdigit()):
        expr = cond[key]
        parts.append(clean(expr.get("Description", "")))
    return " ".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("qsf")
    ap.add_argument("-o", "--out", required=True)
    args = ap.parse_args()

    with open(args.qsf, encoding="utf-8") as f:
        survey = json.load(f)
    elements = survey["SurveyElements"]
    blocks = next(e["Payload"] for e in elements if e["Element"] == "BL")
    flow = next(e["Payload"] for e in elements if e["Element"] == "FL")
    options = next(e["Payload"] for e in elements if e["Element"] == "SO")
    questions = {e["PrimaryAttribute"]: e["Payload"]
                 for e in elements if e["Element"] == "SQ"}
    blocks = {b["ID"]: b for b in blocks.values() if b.get("Type") != "Trash"}

    out = [f"# {survey['SurveyEntry']['SurveyName']}", "",
           "Generated from `survey.qsf` by `qsf_to_md.py`. Do not edit by hand.", ""]

    def write_block(block_id, condition=None):
        block = blocks[block_id]
        name = re.sub(r" - \w{3} \d+, \d{4}$", "", block["Description"])
        out.append(f"## {name}")
        out.append("")
        if condition:
            out.append(f"*Shown only: {condition}*")
            out.append("")
        for el in block.get("BlockElements", []):
            if el["Type"] != "Question":
                continue
            q = questions[el["QuestionID"]]
            v = q.get("Validation", {}).get("Settings", {})
            tags = [q["QuestionType"]]
            if v.get("ForceResponse") == "ON":
                tags.append("required")
            if v.get("ContentType") == "ValidEmail":
                tags.append("email")
            if v.get("Extension"):
                tags.append("files: " + v["Extension"])
            out.append(f"- **`{q['DataExportTag']}`** ({', '.join(tags)}): "
                       f"{clean(q['QuestionText'])}")
            for key, when in (("DisplayLogic", "Shown only"),
                              ("InPageDisplayLogic", "Shown in page only")):
                if key in q:
                    out.append(f"  - *{when}: {logic(q[key]['0'])}*")
            for cid in q.get("ChoiceOrder", []):
                out.append(f"  - {clean(q['Choices'][str(cid)]['Display'])}")
            if q.get("Answers"):
                out.append("  - Scale: " + " / ".join(
                    clean(q["Answers"][str(a)]["Display"]) for a in q["AnswerOrder"]))
        out.append("")

    for item in flow["Flow"]:
        if item["Type"] == "Standard":
            write_block(item["ID"])
        elif item["Type"] == "Branch":
            cond = logic(item["BranchLogic"]["0"])
            for sub in item["Flow"]:
                write_block(sub["ID"], cond)

    skin = options.get("Skin", {}).get("overrides", {})
    out += ["## Options", "",
            f"- Back button: {options.get('BackButton')}",
            f"- Survey title: {options.get('SurveyTitle')}",
            f"- Theme: {options.get('Skin', {}).get('templateId')}, "
            f"background {skin.get('background', {}).get('color')}, "
            f"primary {skin.get('colors', {}).get('primary')}",
            f"- Uploaded files require sign-in: {options.get('SecureResponseFiles')}",
            f"- Bot detection (reCAPTCHA v3): {options.get('RecaptchaV3')}",
            ""]
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()

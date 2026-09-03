#!/usr/bin/env python3
"""Build polished PDF attachments for the KBA editorial enquiry."""

from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    ListFlowable,
    ListItem,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
)


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
OUTPUT_ROOT = REPO_ROOT / "output" / "pdf"

AUTHOR = "Neville Maloba"
EMAIL = "nevillemaloba@gmail.com"

DEEP_BLUE = colors.HexColor("#173B57")
MID_BLUE = colors.HexColor("#2D668C")
TEAL = colors.HexColor("#1B7F83")
GOLD = colors.HexColor("#C99A3D")
INK = colors.HexColor("#263746")
MUTED = colors.HexColor("#607383")
PALE_BLUE = colors.HexColor("#EEF5F8")
RULE = colors.HexColor("#B8C8D2")


def register_fonts() -> tuple[str, str, str, str]:
    candidates = [
        (
            Path("C:/Windows/Fonts/georgia.ttf"),
            Path("C:/Windows/Fonts/georgiab.ttf"),
            Path("C:/Windows/Fonts/arial.ttf"),
            Path("C:/Windows/Fonts/arialbd.ttf"),
        ),
    ]
    for regular, bold, sans, sans_bold in candidates:
        if all(path.exists() for path in (regular, bold, sans, sans_bold)):
            pdfmetrics.registerFont(TTFont("GeorgiaMP", str(regular)))
            pdfmetrics.registerFont(TTFont("GeorgiaMP-Bold", str(bold)))
            pdfmetrics.registerFont(TTFont("ArialMP", str(sans)))
            pdfmetrics.registerFont(TTFont("ArialMP-Bold", str(sans_bold)))
            return "GeorgiaMP", "GeorgiaMP-Bold", "ArialMP", "ArialMP-Bold"
    return "Times-Roman", "Times-Bold", "Helvetica", "Helvetica-Bold"


SERIF, SERIF_BOLD, SANS, SANS_BOLD = register_fonts()


def inline_markup(text: str) -> str:
    protected: dict[str, str] = {}

    def protect(value: str) -> str:
        key = f"TOKEN{len(protected)}TOKEN"
        protected[key] = value
        return key

    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda match: protect(
            f'<link href="{html.escape(match.group(2), quote=True)}" '
            f'color="#2D668C">{html.escape(match.group(1))}</link>'
        ),
        text,
    )
    text = re.sub(
        r"https?://[^\s]+",
        lambda match: protect(
            f'<link href="{html.escape(match.group(0), quote=True)}" '
            f'color="#2D668C">{html.escape(match.group(0))}</link>'
        ),
        text,
    )
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", rf'<font name="{SANS}">\1</font>', text)
    for key, value in protected.items():
        text = text.replace(key, value)
    return text


def make_styles(compact: bool = False) -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    body_size = 8.65 if compact else 9.2
    body_leading = 10.75 if compact else 11.55
    styles = {
        "title": ParagraphStyle(
            "KbaTitle",
            parent=base["Title"],
            fontName=SANS_BOLD,
            fontSize=18 if compact else 20,
            leading=21 if compact else 23,
            textColor=DEEP_BLUE,
            alignment=TA_LEFT,
            spaceAfter=3 * mm,
        ),
        "h2": ParagraphStyle(
            "KbaH2",
            parent=base["Heading2"],
            fontName=SANS_BOLD,
            fontSize=10.3 if compact else 11,
            leading=12.2 if compact else 13.2,
            textColor=DEEP_BLUE,
            spaceBefore=2.1 * mm,
            spaceAfter=1.0 * mm,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "KbaH3",
            parent=base["Heading3"],
            fontName=SANS_BOLD,
            fontSize=9.2 if compact else 9.8,
            leading=11 if compact else 11.8,
            textColor=TEAL,
            spaceBefore=1.5 * mm,
            spaceAfter=0.7 * mm,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "KbaBody",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=body_size,
            leading=body_leading,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=1.5 * mm if compact else 1.8 * mm,
            allowWidows=0,
            allowOrphans=0,
        ),
        "meta": ParagraphStyle(
            "KbaMeta",
            parent=base["BodyText"],
            fontName=SANS,
            fontSize=7.7 if compact else 8.2,
            leading=9.2 if compact else 9.8,
            textColor=MUTED,
            spaceAfter=0.5 * mm,
        ),
        "quote": ParagraphStyle(
            "KbaQuote",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=body_size,
            leading=body_leading,
            textColor=DEEP_BLUE,
            leftIndent=5 * mm,
            rightIndent=3 * mm,
            borderColor=GOLD,
            borderWidth=1.4,
            borderPadding=(2 * mm, 2.5 * mm, 2 * mm, 3.5 * mm),
            backColor=PALE_BLUE,
            spaceBefore=1.5 * mm,
            spaceAfter=2.3 * mm,
        ),
        "bullet": ParagraphStyle(
            "KbaBullet",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=body_size,
            leading=body_leading,
            textColor=INK,
            leftIndent=0,
            firstLineIndent=0,
            spaceAfter=0.5 * mm,
        ),
        "numbered": ParagraphStyle(
            "KbaNumbered",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=body_size,
            leading=body_leading,
            textColor=INK,
            leftIndent=5 * mm,
            firstLineIndent=-5 * mm,
            spaceAfter=0.8 * mm,
        ),
        "code": ParagraphStyle(
            "KbaCode",
            parent=base["Code"],
            fontName="Courier",
            fontSize=7.6 if compact else 8,
            leading=9.4 if compact else 10,
            textColor=DEEP_BLUE,
            leftIndent=4 * mm,
            rightIndent=4 * mm,
            borderColor=RULE,
            borderWidth=0.5,
            borderPadding=2.5 * mm,
            backColor=colors.HexColor("#F6F8FA"),
            spaceBefore=1 * mm,
            spaceAfter=2 * mm,
        ),
        "reference": ParagraphStyle(
            "KbaReference",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=7.3 if compact else 7.7,
            leading=9.2 if compact else 9.6,
            textColor=INK,
            leftIndent=4.5 * mm,
            firstLineIndent=-4.5 * mm,
            spaceAfter=1.1 * mm,
            wordWrap="CJK",
        ),
    }
    return styles


def markdown_to_story(path: Path, compact: bool = False) -> list:
    styles = make_styles(compact)
    lines = path.read_text(encoding="utf-8").splitlines()
    story: list = []
    paragraph_lines: list[str] = []
    bullet_lines: list[str] = []
    quote_lines: list[str] = []
    code_lines: list[str] = []
    in_code = False
    in_references = False

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if paragraph_lines:
            text = " ".join(line.strip() for line in paragraph_lines)
            style = styles["reference"] if in_references else styles["body"]
            story.append(Paragraph(inline_markup(text), style))
            paragraph_lines = []

    def flush_bullets() -> None:
        nonlocal bullet_lines
        if bullet_lines:
            items = [
                ListItem(
                    Paragraph(inline_markup(item), styles["bullet"]),
                    leftIndent=3 * mm,
                )
                for item in bullet_lines
            ]
            story.append(
                ListFlowable(
                    items,
                    bulletType="bullet",
                    bulletFontName=SANS,
                    bulletFontSize=6,
                    bulletColor=TEAL,
                    leftIndent=5 * mm,
                    bulletOffsetY=1,
                    spaceAfter=1.5 * mm,
                )
            )
            bullet_lines = []

    def flush_quote() -> None:
        nonlocal quote_lines
        if quote_lines:
            story.append(
                Paragraph(inline_markup(" ".join(quote_lines)), styles["quote"])
            )
            quote_lines = []

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            flush_paragraph()
            flush_bullets()
            flush_quote()
            if in_code:
                story.append(Preformatted("\n".join(code_lines), styles["code"]))
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_paragraph()
            flush_bullets()
            flush_quote()
            continue
        if line.startswith("# "):
            flush_paragraph()
            story.append(Spacer(1, 2 * mm))
            story.append(Paragraph(inline_markup(line[2:].strip()), styles["title"]))
            story.append(HRFlowable(width="100%", thickness=1.3, color=GOLD))
            story.append(Spacer(1, 2.2 * mm))
            continue
        if line.startswith("## "):
            flush_paragraph()
            flush_bullets()
            heading = line[3:].strip()
            if heading.lower() in {"selected references", "references"}:
                in_references = True
            story.append(Paragraph(inline_markup(heading), styles["h2"]))
            continue
        if line.startswith("### "):
            flush_paragraph()
            flush_bullets()
            story.append(Paragraph(inline_markup(line[4:].strip()), styles["h3"]))
            continue
        if line.startswith("> "):
            flush_paragraph()
            flush_bullets()
            quote_lines.append(line[2:].strip())
            continue
        if re.match(r"^[-*] ", line):
            flush_paragraph()
            flush_quote()
            bullet_lines.append(re.sub(r"^[-*] ", "", line).strip())
            continue
        if re.match(
            r"^\*\*(Author|Affiliation|Email|Proposed KBA theme|Secondary track|"
            r"Proposed audience|Candidate article|Draft date):\*\*",
            line,
        ):
            flush_paragraph()
            flush_bullets()
            flush_quote()
            story.append(Paragraph(inline_markup(line.strip()), styles["meta"]))
            continue
        if re.match(r"^\d+\.\s+", line):
            flush_paragraph()
            flush_bullets()
            flush_quote()
            story.append(Paragraph(inline_markup(line.strip()), styles["numbered"]))
            continue
        paragraph_lines.append(line)

    flush_paragraph()
    flush_bullets()
    flush_quote()
    if code_lines:
        story.append(Preformatted("\n".join(code_lines), styles["code"]))
    return story


def make_page_callback(short_title: str):
    def draw_page(canvas, doc) -> None:
        width, height = A4
        canvas.saveState()
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.45)
        canvas.line(doc.leftMargin, height - 13 * mm, width - doc.rightMargin, height - 13 * mm)
        canvas.setFont(SANS, 7)
        canvas.setFillColor(MUTED)
        canvas.drawString(doc.leftMargin, height - 10.2 * mm, short_title)
        canvas.drawRightString(width - doc.rightMargin, height - 10.2 * mm, "KBA research enquiry")
        canvas.line(doc.leftMargin, 12 * mm, width - doc.rightMargin, 12 * mm)
        canvas.drawString(doc.leftMargin, 8.5 * mm, f"{AUTHOR} | {EMAIL}")
        canvas.drawRightString(width - doc.rightMargin, 8.5 * mm, f"Page {doc.page}")
        canvas.restoreState()

    return draw_page


class MetadataDocTemplate(BaseDocTemplate):
    def __init__(self, *args, pdf_title: str, pdf_subject: str, **kwargs):
        self.pdf_title = pdf_title
        self.pdf_subject = pdf_subject
        super().__init__(*args, **kwargs)

    def beforeDocument(self) -> None:
        self.canv.setTitle(self.pdf_title)
        self.canv.setAuthor(f"{AUTHOR} <{EMAIL}>")
        self.canv.setSubject(f"{self.pdf_subject} | Contact: {EMAIL}")
        self.canv.setCreator(f"{AUTHOR} | KBA lifecycle-credit research package")
        self.canv.setKeywords(
            "Neville Maloba, nevillemaloba@gmail.com, KESONIA, MSME, "
            "credit risk, lifecycle underwriting, collections"
        )


def build_pdf(
    source: Path,
    destination: Path,
    title: str,
    subject: str,
    short_title: str,
    compact: bool,
) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    left = 15.5 * mm if compact else 17 * mm
    right = 15.5 * mm if compact else 17 * mm
    top = 17 * mm
    bottom = 16 * mm
    doc = MetadataDocTemplate(
        str(destination),
        pagesize=A4,
        leftMargin=left,
        rightMargin=right,
        topMargin=top,
        bottomMargin=bottom,
        title=title,
        author=f"{AUTHOR} <{EMAIL}>",
        pdf_title=title,
        pdf_subject=subject,
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="body",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc.addPageTemplates(
        [PageTemplate(id="KBA", frames=[frame], onPage=make_page_callback(short_title))]
    )
    doc.build(markdown_to_story(source, compact=compact))


def main() -> None:
    build_pdf(
        PACKAGE_ROOT / "02_ONE_PAGE_CONCEPT_NOTE.md",
        OUTPUT_ROOT / "KBA_KESONIA_LIFECYCLE_CREDIT_CONCEPT_NOTE.pdf",
        "From KESONIA to Sustainable Collection: Concept Note",
        "One-page concept note for the Kenya Bankers Association Research Centre",
        "KESONIA to Sustainable Collection",
        compact=True,
    )
    build_pdf(
        PACKAGE_ROOT / "03_FIVE_PAGE_RESEARCH_PROPOSAL.md",
        OUTPUT_ROOT / "KBA_KESONIA_LIFECYCLE_CREDIT_RESEARCH_PROPOSAL.pdf",
        "From KESONIA to Sustainable Collection: Research Proposal",
        "Research proposal for the Kenya Bankers Association Research Centre",
        "KESONIA Lifecycle Credit Research Proposal",
        compact=False,
    )


if __name__ == "__main__":
    main()

"""
Generate concise, plain academic Response to Reviewers' Comments PDF in Times New Roman.
Matches user requirement:
- Plain styling (black & white on white paper, no boxes, no colors)
- Top heading: 16pt bold (Times-Bold)
- Subheadings: 14pt bold (Times-Bold)
- Content: 12pt (Times-Roman / Times-Bold)
- Short, simple 1-2 sentence responses at max
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.pdfgen import canvas

PDF_OUTPUT_PATH = "Response_to_Reviewers_Comments_ALAS.pdf"

class PlainNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.saveState()
            self.setFont("Times-Roman", 10)
            self.setFillColor(colors.black)
            page_text = f"{self._pageNumber}"
            self.drawCentredString(306, 36, page_text)
            self.restoreState()
            super().showPage()
        super().save()


def generate_concise_response_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=46,
        bottomMargin=46,
    )

    title_style = ParagraphStyle(
        "TopHeading",
        fontName="Times-Bold",
        fontSize=16,
        leading=22,
        textColor=colors.black,
        spaceAfter=14,
    )

    subheading_style = ParagraphStyle(
        "SubHeading",
        fontName="Times-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.black,
        spaceBefore=10,
        spaceAfter=6,
    )

    body_style = ParagraphStyle(
        "BodyText12",
        fontName="Times-Roman",
        fontSize=12,
        leading=16,
        textColor=colors.black,
        spaceAfter=10,
    )

    comment_style = ParagraphStyle(
        "CommentStyle",
        fontName="Times-Roman",
        fontSize=12,
        leading=16,
        textColor=colors.black,
        spaceBefore=5,
        spaceAfter=2,
    )

    response_style = ParagraphStyle(
        "ResponseStyle",
        fontName="Times-Roman",
        fontSize=12,
        leading=16,
        textColor=colors.black,
        spaceBefore=0,
        spaceAfter=6,
    )

    story = []

    # Title
    story.append(Paragraph("Response to Reviewers' Comments", title_style))

    # Paper Title
    story.append(Paragraph("<b>Paper ID:</b> 1271", body_style))
    story.append(Paragraph("<b>Paper Title:</b> AI Legal Assistant Suite (ALAS): Legal Intelligence Framework", body_style))

    # Opening acknowledgment
    intro_text = (
        "We extend our sincere gratitude to the reviewers for their insightful feedback and constructive "
        "comments. We have thoroughly revised the manuscript to address all the points raised. Below is a "
        "point-by-point response detailing the changes made."
    )
    story.append(Paragraph(intro_text, body_style))
    story.append(Spacer(1, 4))

    def add_pair(cnum, ctext, rtext):
        story.append(Paragraph(f"<b>Comment {cnum}:</b> {ctext}", comment_style))
        story.append(Paragraph(f"<b>Response:</b> {rtext}", response_style))

    # =========================================================================
    # Reviewer 1
    # =========================================================================
    story.append(Paragraph("Reviewer #1 Comments and Author Responses", subheading_style))

    add_pair(
        "1.1",
        "No quantification of results is provided in the abstract although there is description of system design. Results from prototype need to be provided.",
        "We agree and have added quantitative evaluation results to the Abstract on page 1, including our Macro F1-score of 0.824 on contract clauses, 0.887 on case documents, and 100% verified citation authenticity."
    )

    add_pair(
        "1.2",
        "Multi-agent legal assistant for SMEs and human-in-the-loop escalation is a concrete contribution.",
        "Thank you for this positive observation. We have highlighted this contribution in Section 1 (page 2) and detailed the confidence-based escalation mechanism in Section 4.4 (page 4)."
    )

    add_pair(
        "1.3",
        "Novelty relative to other legal AI assistants and contract review tools needs to be explicitly stated.",
        "We have clearly stated the novelty of ALAS in Section 1 (page 2) and added a comprehensive feature comparison with commercial legal platforms in Table IV (page 8)."
    )

    add_pair(
        "1.4",
        "Agent architecture, models used, and retrieval approach need to be explicitly described.",
        "We have expanded Section 3 (page 3) and Section 4 (pages 3&ndash;4) to explicitly describe the tiered model setup (Mistral Medium, Ministral 14B, Pixtral 12B), hybrid semantic chunking, and the LangGraph multi-agent workflow."
    )

    add_pair(
        "1.5",
        "Evaluation on public benchmarks like CUAD or ContractNLI, which are mentioned, is required.",
        "We have added an empirical evaluation across 99 authentic contract clauses from the CUAD and LEDGAR benchmarks in Table II (page 7), where ALAS achieved a Macro F1-score of 0.824."
    )

    add_pair(
        "1.6",
        "Conclusion needs to state results rather than design features.",
        "The Conclusion in Section 7 (page 8) has been rewritten to directly summarize our concrete empirical evaluation results rather than general design features."
    )

    # =========================================================================
    # Reviewer 2
    # =========================================================================
    story.append(Paragraph("Reviewer #2 Comments and Author Responses", subheading_style))

    add_pair(
        "2.1",
        "Abstract must indicate which LLMs and jurisdictions are included.",
        "The Abstract on page 1 has been updated to explicitly state the models used (Mistral Medium, Ministral 14B, Pixtral 12B) and the Indian legal jurisdiction."
    )

    add_pair(
        "2.2",
        "User evaluation by legal professionals would be useful for the contribution.",
        "We agree and have outlined our planned structured user evaluation study with practicing advocates and legal clinics in Section 7 (page 8)."
    )

    add_pair(
        "2.3",
        "Methodology for risk scoring must be indicated.",
        "We have added Section 5.4 (page 5) defining the quantitative formula for the Overall Risk Score and describing the five standardized statutory risk tiers."
    )

    add_pair(
        "2.4",
        "Mechanism for hallucination control and citation verification needs to be mentioned.",
        "We have described our hallucination control measures in Section 3.3 and Section 4, including isolated vector namespaces and live precedent verification via the Indian Kanoon API."
    )

    add_pair(
        "2.5",
        "Comparison with InLegalBERT-based baselines would be helpful.",
        "We added a comparative baseline against fine-tuned InLegalBERT in Section 6.4 (page 7), where ALAS outperformed the baseline by +4.8 percentage points in Macro F1."
    )

    add_pair(
        "2.6",
        "Legal liability and data security aspects should be discussed in the conclusion.",
        "We have added a dedicated discussion on non-delegable legal liability, assistive co-pilot boundaries, and vector namespace privacy in Section 7 (page 8)."
    )

    # =========================================================================
    # Reviewer 3
    # =========================================================================
    story.append(Paragraph("Reviewer #3 Comments and Author Responses", subheading_style))

    add_pair(
        "3.1",
        "The phrases like 'legal DevOps' should be defined or removed.",
        "We agree and have completely removed all occurrences of 'legal DevOps' and 'LegalOps' from the manuscript, replacing them with standard legal terminology."
    )

    add_pair(
        "3.2",
        "Screenshots of the prototype can be reduced to make space for results.",
        "The prototype figures (Figure 3 and Figure 4 on page 6) have been reduced in size to make room for empirical benchmark tables while maintaining readability."
    )

    add_pair(
        "3.3",
        "References to recent legal LLM studies should be included.",
        "We have added recent 2024&ndash;2026 legal AI papers (including Lawma, SaulLM, and LegalBench-RAG) to Section 2 (pages 2&ndash;3) and the References section."
    )

    add_pair(
        "3.4",
        "Latency and cost per document should be reported.",
        "We have added Section 6.7 (page 8) reporting an average contract analysis latency of 21.4 seconds and an operational cost of approximately $0.05 per document."
    )

    add_pair(
        "3.5",
        "Comparison table with commercial systems would be useful.",
        "We have included Table IV in Section 6.6 (page 8), comparing ALAS with commercial platforms like Harvey AI, Ironclad, and Casetext CoCounsel across key feature dimensions."
    )

    doc.build(story, canvasmaker=PlainNumberedCanvas)
    print(f"SUCCESS: Generated concise plain academic PDF -> {PDF_OUTPUT_PATH}")

if __name__ == "__main__":
    generate_concise_response_pdf()

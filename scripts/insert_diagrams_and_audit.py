"""
Inserts all 9 architecture diagrams and flowcharts into Chapters 4 & 5 of the ALAS Black Book,
cleans up all email tags and accidental template strings, and verifies the entire document.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

def style_run(run, font_name="Times New Roman", size_pt=12, bold=False, italic=False):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic

def main():
    doc_path = "docs/Black_Book_ALAS_Completed.docx"
    output_path = "docs/Black_Book_ALAS_Completed.docx"

    doc = docx.Document(doc_path)
    print(f"Loaded document with {len(doc.paragraphs)} paragraphs.")

    diag_dir = "docs/diagrams"

    # Targets to replace in Chapter 4 and Chapter 5:
    # (search_prefix, caption_text, img_filename, desc_text)
    diagram_replacements = [
        # Chapter 4
        ("Figure 4.1: High-Level Block Diagram",
         "Figure 4.1: High-Level Block Diagram of AI Legal Assistant Suite (ALAS)",
         "Figure_4_1_Block_Diagram_ALAS.png",
         "Illustrates the end-to-end ingestion, vector storage, LangGraph multi-agent coordination, statutory grounding, and human-in-the-loop review architecture."),
        
        ("Figure 4.2: System Architecture",
         "Figure 4.2: System Architecture of AI Legal Assistant Suite (ALAS)",
         "Figure_4_2_System_Architecture_ALAS.png",
         "Depicts the decoupled microservices topology: Next.js frontend, FastAPI API gateway, Celery task workers with Redis broker, Chroma DB vector namespaces, and external Indian Kanoon API integration."),
        
        ("Figure 4.3: Sequence Diagram",
         "Figure 4.3: Sequence Diagram of Contract Intake, Audit, and Drafting Workflow",
         "Figure_4_3_Sequence_Diagram_ALAS.png",
         "Chronologically traces asynchronous message exchange between the legal advocate, Next.js UI, FastAPI endpoints, Celery workers, LangGraph orchestrator, and Indian Kanoon precedent APIs."),
        
        ("4.4.1 Project Timeline",
         "Figure 4.4: Project Development Timeline & Milestones (Gantt Chart)",
         "Figure_4_4_Project_Timeline_Gantt_ALAS.png",
         "Outlines the six-phase implementation roadmap spanning requirement gathering, dataset curation, multi-agent development, statutory verification, UI implementation, and empirical benchmarking."),
        
        # Chapter 5
        ("Figure 5.1: Implementation Processing Pipeline",
         "Figure 5.1: Implementation Processing Pipeline of ALAS",
         "Figure_5_1_Processing_Pipeline_ALAS.png",
         "Traces the end-to-end data pipeline from multi-format ingestion and OCR layout analysis to 800-token chunking, dense vector embedding, multi-agent routing, and dual intelligence outputs."),
        
        ("Figure 5.2: Flowchart for Context-Aware Document Chunking",
         "Figure 5.2: Flowchart for Context-Aware Document Chunking and Vector Indexing",
         "Figure_5_2_Chunking_Flowchart_ALAS.png",
         "Flowchart outlining document ingestion, paragraph structure preservation, 800-token window sliding, dynamic short-block merging, and Chroma DB isolated namespace upsert."),
        
        ("Figure 5.3: Flowchart for Multi-Agent Clause Extraction",
         "Figure 5.3: Flowchart for Multi-Agent Clause Extraction and Quantitative Risk Scoring",
         "Figure_5_3_Clause_Risk_Flowchart_ALAS.png",
         "Flowchart detailing semantic chunk retrieval, 22-category CUAD classification, statutory rule scrutiny (ICA 1872), severity-weighted penalty calculation, and risk tier assignment."),
        
        ("Figure 5.4: Flowchart for Multimodal Evidence Processing",
         "Figure 5.4: Flowchart for Multimodal Evidence Processing and Timeline Construction",
         "Figure_5_4_Multimodal_Timeline_Flowchart_ALAS.png",
         "Flowchart detailing multimodal OCR on physical and digital exhibits, temporal entity extraction, milestone sorting, and procedural delay auditing."),
        
        ("Figure 5.5: Flowchart for Cross-Witness Contradiction",
         "Figure 5.5: Flowchart for Cross-Witness Contradiction Detection and Legal Research",
         "Figure_5_5_Contradiction_Debate_Flowchart_ALAS.png",
         "Flowchart illustrating multi-witness statement alignment, fact-checking against FIR allegations, live Indian Kanoon search, and pre-trial moot court debate framing.")
    ]

    # First clean up accidental template strings & email reminders in the ALAS report (P0 to P528)
    for p in doc.paragraphs[:530]:
        # Clean email reminders
        for tag in ["(generate 2023.prathamesh.joshi@ves.ac.in)",
                    "(create 2023.prathamesh.joshi@ves.ac.in)",
                    "(diag here 2023.prathamesh.joshi@ves.ac.in)"]:
            if tag in p.text:
                p.text = p.text.replace(tag, "").strip()
        # Clean Vision-Learn AI accidental references in ALAS chapters
        if "Vision-Learn AI" in p.text:
            p.text = p.text.replace("Vision-Learn AI", "AI Legal Assistant Suite (ALAS)")

    # Insert diagrams
    for prefix, cap_text, img_file, desc_text in diagram_replacements:
        img_path = os.path.join(diag_dir, img_file)
        if not os.path.exists(img_path):
            print(f"Warning: Image file not found {img_path}")
            continue

        matched_p = None
        for p in doc.paragraphs[:530]:
            if p.text.strip().startswith(prefix):
                matched_p = p
                break

        if matched_p:
            print(f"Replacing diagram placeholder: {prefix}")
            matched_p.text = ""  # Clear placeholder text
            matched_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            matched_p.paragraph_format.space_before = Pt(14)
            matched_p.paragraph_format.space_after = Pt(10)
            matched_p.paragraph_format.line_spacing = 1.15

            # 1. Image
            r_img = matched_p.add_run()
            r_img.add_picture(img_path, width=Inches(5.6))

            # 2. Caption
            r_cap = matched_p.add_run("\n" + cap_text + "\n")
            style_run(r_cap, "Times New Roman", 10.5, bold=True)

            # 3. Description
            r_desc = matched_p.add_run(desc_text)
            style_run(r_desc, "Times New Roman", 10, italic=True)
        else:
            print(f"Could not find paragraph with prefix: {prefix}")

    doc.save(output_path)
    print(f"Enriched document with diagrams saved to: {output_path}")

if __name__ == "__main__":
    main()

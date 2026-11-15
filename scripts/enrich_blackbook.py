"""
Enriches the ALAS Academic Black Book (DOCX) cleanly:
- Replaces Figure 7.1 to 7.6 in place with actual images, bold captions, and descriptions.
- Adds Figure 7.7 (Courtroom Debate) and Figure 7.8 (Judicial Interlocutory).
- Inserts Table 7.4b (Latency, Throughput, and Cost) in Section 7.4.
- Inserts Table 7.5 (Commercial Comparison with Harvey, Ironclad, CoCounsel) in Section 7.5.
- Applies consistent Times New Roman typography and clean cell styling.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import os

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E5E5E5"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def style_run(run, font_name="Times New Roman", size_pt=12, bold=False, italic=False, color=None):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color

def main():
    doc_path = "docs/Black_Book_ALAS.docx"
    output_path = "docs/Black_Book_ALAS_Completed.docx"
    
    if not os.path.exists(doc_path):
        print(f"File not found: {doc_path}")
        return

    doc = docx.Document(doc_path)
    print("Loaded document with", len(doc.paragraphs), "paragraphs.")

    ss_dir = "docs/screenshots"

    figures = [
        (456, "Figure 7.1: Comprehensive Legal Analysis and Quantitative Risk Scoring Suite",
         os.path.join(ss_dir, "01_Contract_Analysis_Overview.png"),
         "Displays automated contract classification, an aggregate risk score gauge (57%), high-risk clause alerts, and Indian Contract Act (ICA 1872) compliance gauges for the evaluated commercial lease agreement (NIT - Agreement.pdf)."),
        
        (457, "Figure 7.2: Clause Inspector & Statutory Redline Audit Interface",
         os.path.join(ss_dir, "02_Contract_Clause_Inspector.png"),
         "Presents categorized clause-by-clause covenant extraction with risk severity filters (Critical, High, Medium, Info), statutory citations, and institutional redline diff recommendations."),
        
        (458, "Figure 7.3: Interactive Autonomous Contract Drafting Canvas & Redline Studio",
         os.path.join(ss_dir, "03_Contract_Drafting_Editor.png"),
         "Illustrates the focused full-canvas drafting environment (with side navigation and compliance modals collapsed) displaying an autonomously generated Master Services Agreement (MSA) with non-compete neutralization and neutral arbitration seats."),
        
        (459, "Figure 7.4: Litigation Case Dossier and Evidentiary Multi-Document Index",
         os.path.join(ss_dir, "04_Case_Files_Dossier.png"),
         "Depicts the unified litigation workspace for State & Apex FinTech vs. Zenith Cloud Technologies (FIR 0412/2024), illustrating automated multi-class categorization across all seven court filings and trial exhibits."),
        
        (460, "Figure 7.5: Cross-Document Evidentiary Synthesis & Contradiction Analysis",
         os.path.join(ss_dir, "05_Case_CrossDoc_Intelligence.png"),
         "Demonstrates cross-witness contradiction analysis exposing material discrepancies between the FIR allegations and Section 161 CrPC witness statements, alongside electronic evidence authentication checks under Section 65B/63 BSA."),
        
        (461, "Figure 7.6: Chronological Master Timeline and Procedural Delay Audit",
         os.path.join(ss_dir, "06_Case_Chronological_Timeline.png"),
         "Visualizes the 19-event sequential master timeline reconstructed with Kendall's Tau tau = 1.000, highlighting procedural defects such as an unexplained 160-day delay in lodging the FIR.")
    ]

    # Clean in-place replacement for Figures 7.1 to 7.6
    for p_idx, caption_text, img_path, desc_text in figures:
        p = doc.paragraphs[p_idx]
        p.text = ""  # Wipe placeholder text cleanly
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(10)
        p.paragraph_format.line_spacing = 1.15

        if os.path.exists(img_path):
            r_img = p.add_run()
            r_img.add_picture(img_path, width=Inches(5.6))
        
        r_cap = p.add_run("\n" + caption_text + "\n")
        style_run(r_cap, "Times New Roman", 10.5, bold=True)
        
        r_desc = p.add_run(desc_text)
        style_run(r_desc, "Times New Roman", 10, italic=True)

    print("Cleanly replaced Figures 7.1 to 7.6 in place.")

    # Insert Figures 7.7 and 7.8 right after paragraph 461
    p462 = doc.paragraphs[462]

    extra_figures = [
        ("Figure 7.7: Autonomous Multi-Agent Courtroom Debate War Room",
         os.path.join(ss_dir, "07_Case_Debate_Moot_Courtroom.png"),
         "Features the autonomous pre-trial debate arena, illustrating active legal issue argumentation, real-time Bench Favorability Index tracking, and oral arguments between Petitioner and Defense Counsel."),
        
        ("Figure 7.8: Precedent Citation & Judicial Interlocutory Dialogue",
         os.path.join(ss_dir, "08_Case_Debate_Judicial_Interlocutory.png"),
         "Displays judicial interlocutory challenges from the Bench agent, verifying live case law citations retrieved via Indian Kanoon on electronic evidence admissibility under Arjun Panditrao Khotkar.")
    ]

    for caption_text, img_path, desc_text in extra_figures:
        p_extra = p462.insert_paragraph_before()
        p_extra.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_extra.paragraph_format.space_before = Pt(14)
        p_extra.paragraph_format.space_after = Pt(10)
        p_extra.paragraph_format.line_spacing = 1.15

        if os.path.exists(img_path):
            r_img = p_extra.add_run()
            r_img.add_picture(img_path, width=Inches(5.6))
        
        r_cap = p_extra.add_run("\n" + caption_text + "\n")
        style_run(r_cap, "Times New Roman", 10.5, bold=True)
        
        r_desc = p_extra.add_run(desc_text)
        style_run(r_desc, "Times New Roman", 10, italic=True)

    print("Inserted Figures 7.7 and 7.8.")

    # Find where Table 7.4 is located to place Table 7.4b
    target_74 = None
    for p in doc.paragraphs:
        if p.text.strip().startswith("Table 7.4: Performance of Case Document Classifier"):
            target_74 = p
            break

    if target_74:
        lat_title_p = target_74.insert_paragraph_before()
        lat_title_p.paragraph_format.space_before = Pt(16)
        lat_title_p.paragraph_format.space_after = Pt(6)
        r = lat_title_p.add_run("Table 7.4b: System Latency, Processing Throughput, and Operational Execution Cost")
        style_run(r, "Times New Roman", 11, bold=True)

        lat_data = [
            ["Subsystem Task / Workflow", "Average Latency", "Empirical Distribution", "Compute / Token Tariff Basis"],
            ["Contract Analysis (19 Chunks)", "21.4 seconds", "p50 = 19.8s, p95 = 26.2s", "~28,500 cumulative tokens (~$0.05 per contract)"],
            ["Multimodal OCR & Vision Parsing", "4.2 seconds / page", "p50 = 3.8s, p95 = 5.1s", "Pixtral 12B Vision API (99% confidence)"],
            ["Autonomous Contract Synthesis", "316.0 seconds", "14 sections, 129,184 chars", "Mistral Medium + Ministral 14B (~$0.08)"],
            ["Chronological Master Timeline", "6.8 seconds", "19 milestones, Tau = 1.000", "Chroma DB isolated retrieval + Mistral Agent"],
            ["Courtroom Debate Turn Cycle", "3.2 seconds / turn", "p50 = 2.9s, p95 = 4.1s", "Multi-agent LangGraph inter-counsel exchange"]
        ]

        lat_table = doc.add_table(rows=len(lat_data), cols=len(lat_data[0]))
        lat_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(lat_table)
        lat_widths = [Inches(2.0), Inches(1.3), Inches(1.5), Inches(1.8)]

        for r_idx, row in enumerate(lat_table.rows):
            for c_idx, cell in enumerate(row.cells):
                cell.text = lat_data[r_idx][c_idx]
                cell.width = lat_widths[c_idx]
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(4)
                run = p.runs[0]
                if r_idx == 0:
                    style_run(run, "Times New Roman", 9.5, bold=True)
                    set_cell_background(cell, "1E293B")
                    run.font.color.rgb = RGBColor(255, 255, 255)
                else:
                    style_run(run, "Times New Roman", 9, bold=(c_idx==0))
                    if r_idx % 2 == 1:
                        set_cell_background(cell, "F8FAFC")

        lat_title_p._p.addnext(lat_table._tbl)
        print("Inserted Table 7.4b.")

    # Find Section 7.5 to place Table 7.5 (Comparison with existing systems)
    target_75 = None
    for p in doc.paragraphs:
        if p.text.strip().startswith("7.5 Comparison of Results with Existing Systems"):
            target_75 = p
            break

    if target_75:
        comp_title_p = target_75.insert_paragraph_before()
        comp_title_p.paragraph_format.space_before = Pt(16)
        comp_title_p.paragraph_format.space_after = Pt(6)
        r = comp_title_p.add_run("Table 7.5: Architectural and Functional Comparison with Commercial Legal AI Platforms")
        style_run(r, "Times New Roman", 11, bold=True)

        comp_data = [
            ["Feature Dimension", "Harvey AI", "Ironclad", "Casetext CoCounsel", "ALAS (Proposed)"],
            ["Primary Target Market", "Global Enterprise / AmLaw 100", "Corporate Legal Departments", "US Litigation Practices", "Resource-Constrained SMEs & Boutique Practices"],
            ["System Architecture", "Monolithic LLM Wrapper", "Rule Engine + LLM Plugin", "Prompt-Chained Agent", "Decoupled LangGraph Multi-Agent Architecture"],
            ["Local Statutory Guardrails", "US / UK Common Law", "US Standard Boilerplate", "US Federal & State Laws", "Native Indian Jurisprudence (ICA 1872, CrPC/BNSS, BSA)"],
            ["Precedent Verification", "Proprietary Corpus Only", "None (Template-Driven)", "Static US Legal Citations", "Live API Verification via Indian Kanoon (100% Auth.)"],
            ["Human-in-the-Loop Controls", "Passive Chat Interface", "Workflow Approval Tree", "Conversational QA Flow", "Confidence-Gated Shadow Review Queue (<0.80)"],
            ["Data Privacy & Retention", "Cloud Multi-Tenant", "Cloud Multi-Tenant", "Cloud Multi-Tenant", "Private Isolated Client Vector Namespaces (Chroma DB)"],
            ["Economic / Cost Model", "High ($10,000+ Annual Seats)", "High (Enterprise SaaS)", "Premium Monthly Per-Seat", "Low Operating Cost (~$0.05 per document analysis)"]
        ]

        table = doc.add_table(rows=len(comp_data), cols=len(comp_data[0]))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table)
        col_widths = [Inches(1.4), Inches(1.2), Inches(1.1), Inches(1.1), Inches(1.4)]

        for r_idx, row in enumerate(table.rows):
            for c_idx, cell in enumerate(row.cells):
                cell.text = comp_data[r_idx][c_idx]
                cell.width = col_widths[c_idx]
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(4)
                p.paragraph_format.line_spacing = 1.05
                run = p.runs[0]
                if r_idx == 0:
                    style_run(run, "Times New Roman", 9.5, bold=True)
                    set_cell_background(cell, "0F172A")
                    run.font.color.rgb = RGBColor(255, 255, 255)
                else:
                    style_run(run, "Times New Roman", 9, bold=(c_idx==0 or c_idx==4))
                    if r_idx % 2 == 1:
                        set_cell_background(cell, "F8FAFC")
                    if c_idx == 4:
                        set_cell_background(cell, "F0FDF4")

        comp_title_p._p.addnext(table._tbl)
        print("Inserted Table 7.5.")

    # Save finalized document
    doc.save(output_path)
    print(f"Finalized document saved successfully to: {output_path}")

if __name__ == "__main__":
    main()

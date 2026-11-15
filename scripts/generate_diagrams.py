"""
Generates clean, institutional, high-resolution architecture diagrams and flowcharts
for the ALAS Academic Black Book (Chapters 4 & 5).
"""

import os
os.environ['MPLCONFIGDIR'] = 'backend/storage'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Color palette: Institutional Legal Tech
BG_COLOR = "#FFFFFF"
CARD_BG = "#F8FAFC"
CARD_BORDER = "#CBD5E1"
PRIMARY = "#0F172A"       # Deep slate navy
ACCENT_BLUE = "#2563EB"   # Restrained legal blue
ACCENT_GREEN = "#059669"  # Statutory green
ACCENT_RED = "#DC2626"    # Defect red
TEXT_MAIN = "#0F172A"
TEXT_MUTED = "#64748B"
TEXT_LIGHT = "#FFFFFF"

OUT_DIR = "docs/diagrams"
os.makedirs(OUT_DIR, exist_ok=True)

def draw_box(ax, x, y, w, h, title, subtitle="", bg=CARD_BG, border=CARD_BORDER, title_color=PRIMARY, text_color=TEXT_MUTED, radius=0.03):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0.01,rounding_size={radius}",
                                linewidth=1.5, edgecolor=border, facecolor=bg)
    ax.add_patch(box)
    if subtitle:
        ax.text(x + w/2, y + h*0.62, title, ha="center", va="center", fontsize=9.5, fontweight="bold", color=title_color, family="DejaVu Sans")
        ax.text(x + w/2, y + h*0.30, subtitle, ha="center", va="center", fontsize=7.8, color=text_color, family="DejaVu Sans")
    else:
        ax.text(x + w/2, y + h*0.5, title, ha="center", va="center", fontsize=9, fontweight="bold", color=title_color, family="DejaVu Sans")

def draw_arrow(ax, x1, y1, x2, y2, label="", color=ACCENT_BLUE, style="->"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=1.6, shrinkA=3, shrinkB=3))
    if label:
        mx, my = (x1 + x2)/2, (y1 + y2)/2
        ax.text(mx, my + 0.02, label, ha="center", va="bottom", fontsize=7.5, color=TEXT_MUTED, fontweight="semibold",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))

# ==============================================================================
# 1. Figure 4.1: High-Level Block Diagram of ALAS
# ==============================================================================
def make_fig_4_1():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    ax.text(5, 5.6, "HIGH-LEVEL BLOCK DIAGRAM OF AI LEGAL ASSISTANT SUITE (ALAS)",
            ha="center", va="center", fontsize=11, fontweight="bold", color=PRIMARY, family="DejaVu Sans")

    # Ingestion Layer
    draw_box(ax, 0.5, 3.2, 2.2, 1.8, "DOCUMENT INGESTION", "PDF / DOCX / Scanned Records\nOCR & Layout Analysis (Pixtral 12B)\nContext-Aware 800-Token Chunking", bg="#F1F5F9", border=ACCENT_BLUE)
    
    # Vector & Storage Layer
    draw_box(ax, 0.5, 0.6, 2.2, 1.8, "SECURE DATA STORAGE", "Chroma DB (Isolated Vector Space)\nPostgreSQL (Relational Metadata)\nRedis & Celery Task Queue", bg="#F1F5F9", border=ACCENT_BLUE)

    # Multi-Agent Orchestrator
    draw_box(ax, 3.8, 1.6, 2.6, 3.2, "LANGGRAPH MULTI-AGENT LAYER", "Mistral Medium (Chief Orchestrator)\nMinistral 14B (Specialist)\n• Clause & Risk Analysis Agent\n• Autonomous Drafting Agent\n• Timeline Extraction Agent\n• Witness Contradiction Agent\n• Pre-Trial Moot Debate Agent", bg="#EFF6FF", border=ACCENT_BLUE)

    # Statutory Grounding
    draw_box(ax, 7.3, 3.2, 2.3, 1.8, "STATUTORY GROUNDING", "Indian Contract Act (ICA 1872)\nCrPC & BNSS Procedural Codes\nLive Indian Kanoon Verification\nEvidence Act (Sec 65B/63 BSA)", bg="#ECFDF5", border=ACCENT_GREEN)

    # Verification & UI
    draw_box(ax, 7.3, 0.6, 2.3, 1.8, "INSTITUTIONAL WORKSPACE", "Next.js Institutional Frontend\nInteractive Drafting & Redline Canvas\nConfidence Gating (<0.80 Queue)\nHuman-in-the-Loop Affirmation", bg="#FEF2F2", border=ACCENT_RED)

    # Connectors
    draw_arrow(ax, 2.7, 4.1, 3.8, 3.8, "Chunks")
    draw_arrow(ax, 1.6, 3.2, 1.6, 2.4, "Embeddings")
    draw_arrow(ax, 2.7, 1.5, 3.8, 2.2, "Context")
    draw_arrow(ax, 6.4, 4.1, 7.3, 4.1, "Statutory Query")
    draw_arrow(ax, 7.3, 3.6, 6.4, 3.6, "Precedents")
    draw_arrow(ax, 6.4, 2.2, 7.3, 1.8, "Draft & Review")
    draw_arrow(ax, 8.45, 2.4, 8.45, 3.2, "Compliance")

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/Figure_4_1_Block_Diagram_ALAS.png", bbox_inches="tight")
    plt.close()
    print("Generated Figure 4.1.")

# ==============================================================================
# 2. Figure 4.2: System Architecture Diagram of ALAS
# ==============================================================================
def make_fig_4_2():
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    ax.text(5.5, 6.65, "SYSTEM ARCHITECTURE OF AI LEGAL ASSISTANT SUITE (ALAS)",
            ha="center", va="center", fontsize=11, fontweight="bold", color=PRIMARY, family="DejaVu Sans")

    # Layer 1: Client
    draw_box(ax, 0.5, 4.8, 10, 1.5, "PRESENTATION LAYER (Next.js 16 / TypeScript / Shadcn UI)",
             "Executive Dashboard (/dashboard)   |   Contract Analysis Suite (/analysis)   |   Drafting Canvas (/drafting)   |   Litigation Intelligence (/cases)",
             bg="#F8FAFC", border="#94A3B8")

    # Layer 2: API Gateway & Service
    draw_box(ax, 0.5, 2.8, 4.7, 1.6, "API GATEWAY & WEB SERVICE",
             "FastAPI (RESTful Endpoints /api/v1)\nPydantic Data Validation & CORS\nSynchronous Session & Auth Middleware",
             bg="#EFF6FF", border=ACCENT_BLUE)

    draw_box(ax, 5.8, 2.8, 4.7, 1.6, "BACKGROUND ASYNCHRONOUS WORKERS",
             "Celery Distributed Task Queue\nRedis Message Broker & Cache (Port 6379)\nParallel Chunk Processing & OCR Tasks",
             bg="#F1F5F9", border=ACCENT_BLUE)

    # Layer 3: Storage & External
    draw_box(ax, 0.5, 0.5, 3.1, 1.8, "RELATIONAL DATA",
             "PostgreSQL / Supabase\nCase Metadata & Contracts\nAudit Trail & Version History",
             bg="#F0FDF4", border=ACCENT_GREEN)

    draw_box(ax, 3.95, 0.5, 3.1, 1.8, "VECTOR & CACHE",
             "Chroma DB (Isolated Namespaces)\nmistral-embed Dense Vectors\nLocal Storage (/storage/outputs)",
             bg="#F0FDF4", border=ACCENT_GREEN)

    draw_box(ax, 7.4, 0.5, 3.1, 1.8, "AI FOUNDATION & EXTERNAL",
             "Mistral API (Medium, Ministral 14B, Pixtral)\nIndian Kanoon Legal Precedent API\nHITL Confidence Escalation (<0.80)",
             bg="#FEF2F2", border=ACCENT_RED)

    # Connectors
    draw_arrow(ax, 2.85, 4.8, 2.85, 4.4, "HTTP/JSON")
    draw_arrow(ax, 8.15, 4.8, 8.15, 4.4, "Async Polling")
    draw_arrow(ax, 5.2, 3.6, 5.8, 3.6, "Enqueue Tasks")
    draw_arrow(ax, 2.05, 2.8, 2.05, 2.3, "SQLAlchemy")
    draw_arrow(ax, 5.5, 2.8, 5.5, 2.3, "Chroma Queries")
    draw_arrow(ax, 8.95, 2.8, 8.95, 2.3, "LLM Inference & APIs")

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/Figure_4_2_System_Architecture_ALAS.png", bbox_inches="tight")
    plt.close()
    print("Generated Figure 4.2.")

# ==============================================================================
# 3. Figure 4.3: Sequence Diagram of ALAS
# ==============================================================================
def make_fig_4_3():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    ax.text(5, 8.1, "SEQUENCE DIAGRAM: CONTRACT INTAKE, AUDIT, & DRAFTING WORKFLOW",
            ha="center", va="center", fontsize=11, fontweight="bold", color=PRIMARY, family="DejaVu Sans")

    actors = ["Legal Advocate", "Next.js UI", "FastAPI Server", "Celery Worker", "LangGraph Agent", "Kanoon API"]
    xs = [1.0, 2.6, 4.2, 5.8, 7.4, 9.0]

    for a, x in zip(actors, xs):
        box = patches.FancyBboxPatch((x-0.7, 7.3), 1.4, 0.5, boxstyle="round,pad=0.01",
                                    facecolor="#F1F5F9", edgecolor=ACCENT_BLUE, lw=1.2)
        ax.add_patch(box)
        ax.text(x, 7.55, a, ha="center", va="center", fontsize=8, fontweight="bold", color=PRIMARY)
        ax.plot([x, x], [1.0, 7.3], color="#94A3B8", lw=1.0, ls="--")

    # Sequence steps
    steps = [
        (1.0, 2.6, 6.7, "1. Upload Contract (PDF)"),
        (2.6, 4.2, 6.2, "2. POST /api/v1/contracts/upload"),
        (4.2, 5.8, 5.7, "3. Dispatch Async Task (task_id)"),
        (5.8, 7.4, 5.2, "4. Trigger LangGraph Analysis Workflow"),
        (7.4, 9.0, 4.7, "5. Query Precedents (ICA Sec 27/74)"),
        (9.0, 7.4, 4.2, "6. Verified Judgments (Doc IDs)"),
        (7.4, 5.8, 3.6, "7. Synthesize Clauses & Risk Score (R)"),
        (5.8, 4.2, 3.0, "8. Update DB & Task Status (SUCCESS)"),
        (2.6, 4.2, 2.4, "9. Poll Task Status GET /status"),
        (4.2, 2.6, 1.8, "10. Return Contract Analysis JSON"),
        (2.6, 1.0, 1.3, "11. Render Risk Gauges & Redline Canvas")
    ]

    for x1, x2, y, txt in steps:
        draw_arrow(ax, x1, y, x2, y, color=ACCENT_BLUE if x1 < x2 else ACCENT_GREEN)
        ax.text((x1+x2)/2, y+0.12, txt, ha="center", va="bottom", fontsize=7.2, color=TEXT_MAIN, fontweight="semibold")

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/Figure_4_3_Sequence_Diagram_ALAS.png", bbox_inches="tight")
    plt.close()
    print("Generated Figure 4.3.")

# ==============================================================================
# 4. Figure 4.4: Project Timeline & Gantt Chart
# ==============================================================================
def make_fig_4_4():
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    ax.text(5, 5.6, "PROJECT DEVELOPMENT TIMELINE & MILESTONES (GANTT CHART)",
            ha="center", va="center", fontsize=11, fontweight="bold", color=PRIMARY, family="DejaVu Sans")

    tasks = [
        ("Phase 1: SRS & Requirement Gathering", 0.5, 2.0, "#3B82F6"),
        ("Phase 2: Dataset Curation & Chunking Pipeline", 2.0, 3.5, "#60A5FA"),
        ("Phase 3: Multi-Agent LangGraph Orchestration", 3.2, 5.5, "#2563EB"),
        ("Phase 4: Statutory Compliance & Kanoon Engine", 5.0, 7.0, "#059669"),
        ("Phase 5: Next.js Frontend & Legal Studio UI", 6.5, 8.5, "#10B981"),
        ("Phase 6: Empirical Benchmarking & Black Book", 7.8, 9.5, "#0F172A"),
    ]

    # Time axis
    ax.plot([0.5, 9.5], [0.8, 0.8], color="#94A3B8", lw=1.2)
    months = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"]
    for i, m in enumerate(months):
        x = 0.5 + i * 1.8
        ax.plot([x, x], [0.75, 0.85], color="#94A3B8", lw=1.2)
        ax.text(x, 0.55, m, ha="center", va="center", fontsize=8, color=TEXT_MUTED)

    for idx, (t_name, start_x, end_x, col) in enumerate(tasks):
        y = 4.8 - idx * 0.65
        bar = patches.FancyBboxPatch((start_x, y-0.18), end_x - start_x, 0.36,
                                    boxstyle="round,pad=0.01", facecolor=col, edgecolor="none")
        ax.add_patch(bar)
        ax.text(0.4, y, t_name, ha="right", va="center", fontsize=8, fontweight="bold", color=PRIMARY)

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/Figure_4_4_Project_Timeline_Gantt_ALAS.png", bbox_inches="tight")
    plt.close()
    print("Generated Figure 4.4.")

# ==============================================================================
# 5. Figure 5.1: Implementation Processing Pipeline
# ==============================================================================
def make_fig_5_1():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.5)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    ax.text(5, 5.1, "ALAS IMPLEMENTATION PROCESSING PIPELINE",
            ha="center", va="center", fontsize=11, fontweight="bold", color=PRIMARY, family="DejaVu Sans")

    blocks = [
        ("1. Multi-Format Intake", "Native PDF / Scanned\nDOCX / Image Files", 0.5, 2.5),
        ("2. Layout & OCR", "Pixtral 12B Vision\nTextract / PyMuPDF", 2.4, 2.5),
        ("3. Context Chunking", "800-Token Windows\n100-Token Overlap", 4.3, 2.5),
        ("4. Vector Embedding", "mistral-embed API\nChroma DB Isolated", 6.2, 2.5),
        ("5. Multi-Agent Audit", "LangGraph Orchestrator\nKanoon & ICA Rules", 8.1, 2.5)
    ]

    for title, sub, x, y in blocks:
        draw_box(ax, x, y, 1.6, 1.6, title, sub, bg="#F8FAFC", border=ACCENT_BLUE)

    for i in range(len(blocks)-1):
        draw_arrow(ax, blocks[i][2] + 1.6, 3.3, blocks[i+1][2], 3.3)

    # Output boxes below
    draw_box(ax, 2.0, 0.6, 2.5, 1.2, "Contract Intelligence", "Risk Score | Redline Diff | Obligations", bg="#EFF6FF", border=ACCENT_BLUE)
    draw_box(ax, 5.5, 0.6, 2.5, 1.2, "Litigation Intelligence", "Master Timeline | Contradictions | Moot", bg="#ECFDF5", border=ACCENT_GREEN)

    draw_arrow(ax, 8.9, 2.5, 4.5, 1.2)
    draw_arrow(ax, 8.9, 2.5, 6.75, 1.2)

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/Figure_5_1_Processing_Pipeline_ALAS.png", bbox_inches="tight")
    plt.close()
    print("Generated Figure 5.1.")

# ==============================================================================
# 6. Figure 5.2: Flowchart for Chunking & Indexing
# ==============================================================================
def make_fig_5_2():
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    ax.text(4.5, 5.6, "CONTEXT-AWARE DOCUMENT CHUNKING & VECTOR INDEXING FLOWCHART",
            ha="center", va="center", fontsize=10.5, fontweight="bold", color=PRIMARY, family="DejaVu Sans")

    draw_box(ax, 3.2, 4.6, 2.6, 0.7, "Document File Received", "PDF / DOCX Upload", bg="#F1F5F9")
    draw_box(ax, 3.2, 3.5, 2.6, 0.7, "Layout Parsing & Cleaning", "Extract Paragraphs & Headers", bg="#EFF6FF")
    draw_box(ax, 3.2, 2.4, 2.6, 0.7, "Sliding Window Slicing", "800 Tokens, 100 Overlap", bg="#EFF6FF")
    draw_box(ax, 3.2, 1.3, 2.6, 0.7, "Generate Dense Vectors", "mistral-embed API", bg="#ECFDF5")
    draw_box(ax, 3.2, 0.2, 2.6, 0.7, "Chroma DB Upsert", "Org/Case Isolated Namespace", bg="#F0FDF4")

    draw_arrow(ax, 4.5, 4.6, 4.5, 4.2)
    draw_arrow(ax, 4.5, 3.5, 4.5, 3.1)
    draw_arrow(ax, 4.5, 2.4, 4.5, 2.0)
    draw_arrow(ax, 4.5, 1.3, 4.5, 0.9)

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/Figure_5_2_Chunking_Flowchart_ALAS.png", bbox_inches="tight")
    plt.close()
    print("Generated Figure 5.2.")

# ==============================================================================
# 7. Figure 5.3: Clause Extraction & Quantitative Risk Scoring Flowchart
# ==============================================================================
def make_fig_5_3():
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    ax.text(4.5, 5.6, "MULTI-AGENT CLAUSE EXTRACTION & RISK SCORING FLOWCHART",
            ha="center", va="center", fontsize=10.5, fontweight="bold", color=PRIMARY, family="DejaVu Sans")

    draw_box(ax, 3.0, 4.6, 3.0, 0.7, "Semantic Chunks Retrieved", "Top-K Chunks from Chroma", bg="#F1F5F9")
    draw_box(ax, 3.0, 3.5, 3.0, 0.7, "Clause Analysis Specialist", "22 CUAD Classes (Ministral 14B)", bg="#EFF6FF")
    draw_box(ax, 3.0, 2.4, 3.0, 0.7, "Statutory Rule Scrutiny", "ICA 1872 Sec 27/74/28 Validation", bg="#ECFDF5")
    draw_box(ax, 3.0, 1.3, 3.0, 0.7, "Penalty Weighted Scoring", "R = min(100, Σ w(s_i) · λ(c_i))", bg="#FEF2F2")
    draw_box(ax, 3.0, 0.2, 3.0, 0.7, "Risk Tier Classification", "Low / Moderate / High / Critical", bg="#F0FDF4")

    draw_arrow(ax, 4.5, 4.6, 4.5, 4.2)
    draw_arrow(ax, 4.5, 3.5, 4.5, 3.1)
    draw_arrow(ax, 4.5, 2.4, 4.5, 2.0)
    draw_arrow(ax, 4.5, 1.3, 4.5, 0.9)

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/Figure_5_3_Clause_Risk_Flowchart_ALAS.png", bbox_inches="tight")
    plt.close()
    print("Generated Figure 5.3.")

# ==============================================================================
# 8. Figure 5.4: Multimodal Evidence & Timeline Construction Flowchart
# ==============================================================================
def make_fig_5_4():
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    ax.text(4.5, 5.6, "MULTIMODAL EVIDENCE & TIMELINE CONSTRUCTION FLOWCHART",
            ha="center", va="center", fontsize=10.5, fontweight="bold", color=PRIMARY, family="DejaVu Sans")

    draw_box(ax, 3.0, 4.6, 3.0, 0.7, "Heterogeneous Case Exhibits", "FIR, MLC, Panchnama, Chat PNG", bg="#F1F5F9")
    draw_box(ax, 3.0, 3.5, 3.0, 0.7, "Visual Layout & Text Ingestion", "Pixtral 12B Multimodal OCR", bg="#EFF6FF")
    draw_box(ax, 3.0, 2.4, 3.0, 0.7, "Temporal Entity Extraction", "Extract Dates & Associated Actions", bg="#EFF6FF")
    draw_box(ax, 3.0, 1.3, 3.0, 0.7, "Sequential Milestones Sort", "Monotonic Order (Kendall's Tau = 1.0)", bg="#ECFDF5")
    draw_box(ax, 3.0, 0.2, 3.0, 0.7, "Procedural Delay Flagging", "Detect Unexplained Filing Lags", bg="#FEF2F2")

    draw_arrow(ax, 4.5, 4.6, 4.5, 4.2)
    draw_arrow(ax, 4.5, 3.5, 4.5, 3.1)
    draw_arrow(ax, 4.5, 2.4, 4.5, 2.0)
    draw_arrow(ax, 4.5, 1.3, 4.5, 0.9)

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/Figure_5_4_Multimodal_Timeline_Flowchart_ALAS.png", bbox_inches="tight")
    plt.close()
    print("Generated Figure 5.4.")

# ==============================================================================
# 9. Figure 5.5: Cross-Witness Contradiction & Moot Court Flowchart
# ==============================================================================
def make_fig_5_5():
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    ax.text(4.5, 5.6, "CROSS-WITNESS CONTRADICTION & PRE-TRIAL MOOT FLOWCHART",
            ha="center", va="center", fontsize=10.5, fontweight="bold", color=PRIMARY, family="DejaVu Sans")

    draw_box(ax, 3.0, 4.6, 3.0, 0.7, "Witness Statements (Sec 161/164)", "CFO, CTO, Complainant Depositions", bg="#F1F5F9")
    draw_box(ax, 3.0, 3.5, 3.0, 0.7, "Cross-Document Matrix Parsing", "Compare Facts vs FIR Allegations", bg="#EFF6FF")
    draw_box(ax, 3.0, 2.4, 3.0, 0.7, "Contradiction Flagging", "Assault vs Non-Assault, Tech Progress", bg="#FEF2F2")
    draw_box(ax, 3.0, 1.3, 3.0, 0.7, "Indian Kanoon Retrieval", "Live Case Law Precedents (100% Auth)", bg="#ECFDF5")
    draw_box(ax, 3.0, 0.2, 3.0, 0.7, "Moot Court Debate Simulation", "Petitioner vs Defense vs Judicial Bench", bg="#F0FDF4")

    draw_arrow(ax, 4.5, 4.6, 4.5, 4.2)
    draw_arrow(ax, 4.5, 3.5, 4.5, 3.1)
    draw_arrow(ax, 4.5, 2.4, 4.5, 2.0)
    draw_arrow(ax, 4.5, 1.3, 4.5, 0.9)

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/Figure_5_5_Contradiction_Debate_Flowchart_ALAS.png", bbox_inches="tight")
    plt.close()
    print("Generated Figure 5.5.")

if __name__ == "__main__":
    make_fig_4_1()
    make_fig_4_2()
    make_fig_4_3()
    make_fig_4_4()
    make_fig_5_1()
    make_fig_5_2()
    make_fig_5_3()
    make_fig_5_4()
    make_fig_5_5()
    print("All 9 diagrams generated successfully in docs/diagrams/")

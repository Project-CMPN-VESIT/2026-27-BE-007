import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
load_dotenv()
from backend.utils.llm_utils import get_specialist_model
from langchain_core.messages import HumanMessage

with open("evaluation/data_cache/CUAD_v1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find a real Cap on Liability clause
sample_clause = None
for doc in data["data"]:
    for p in doc["paragraphs"]:
        for qa in p["qas"]:
            if "Cap On Liability" in qa["question"]:
                for ans in qa.get("answers", []):
                    if len(ans.get("text", "")) > 50:
                        sample_clause = ans["text"]
                        break
            if sample_clause:
                break
        if sample_clause:
            break
    if sample_clause:
        break

print("Real CUAD Clause:\n", sample_clause[:200])

llm = get_specialist_model()
prompt = f"""You are the ALAS Clause Analysis Specialist.
Examine this contractual clause and classify it into EXACTLY ONE of the following 22 categories:
- Limitation of Liability
- Indemnification
- Governing Law
- Dispute Resolution
- Force Majeure
- Confidentiality
- Intellectual Property
- Payment
- Termination
- Non-Compete
- Non-Solicitation
- Warranties
- Representations
- Data Protection
- Assignment
- Notices
- Audit
- Compliance
- Service Levels
- Term
- Renewal
- Insurance

Clause Text:
\"\"\"{sample_clause}\"\"\"

Respond ONLY in valid JSON:
{{"predicted_category": "<one of the 22 categories>", "confidence": 0.95}}
"""

res = llm.invoke([HumanMessage(content=prompt)])
print("\nLive LLM Result:\n", res.content.strip())

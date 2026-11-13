"""
Script to generate expanded, realistic benchmark datasets for:
1. gold_contract_clauses.json (110 contract clauses across 22 CUAD classes, 5 per class)
2. gold_case_documents.json (45 litigation documents across 9 classes, 5 per class)
"""

import json
from pathlib import Path

BENCHMARKS_DIR = Path(__file__).resolve().parent

# 22 Canonical CUAD Classes: 5 diverse clauses each (110 total)
# Sourced from standard commercial contracts (NDAs, MSAs, SaaS, Leases, Employment, Licensing, Credit/Loan)
# Includes realistic drafting styles, nuances, and edge cases.

CONTRACT_CLAUSES_DATA = [
    # 1. Limitation of Liability
    {
        "id": "lim_liab_01",
        "gold_clause_type": "Limitation of Liability",
        "text": "IN NO EVENT SHALL EITHER PARTY BE LIABLE TO THE OTHER FOR ANY INDIRECT, INCIDENTAL, SPECIAL, PUNITIVE, EXEMPLARY, OR CONSEQUENTIAL DAMAGES, OR FOR ANY LOSS OF PROFITS, DATA, BUSINESS OPPORTUNITY, OR GOODWILL, ARISING OUT OF OR IN CONNECTION WITH THIS AGREEMENT, REGARDLESS OF THE THEORY OF LIABILITY (WHETHER IN CONTRACT, TORT, STRICT LIABILITY, OR OTHERWISE), EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. EACH PARTY'S AGGREGATE LIABILITY UNDER THIS AGREEMENT SHALL BE LIMITED TO THE TOTAL FEES PAID OR PAYABLE BY CUSTOMER IN THE TWELVE (12) MONTHS PRECEDING THE CLAIM.",
        "contract_type": "Master Services Agreement"
    },
    {
        "id": "lim_liab_02",
        "gold_clause_type": "Limitation of Liability",
        "text": "To the maximum extent permitted by applicable law, in no event shall Licensor or its suppliers be liable for any special, incidental, indirect, or consequential damages whatsoever (including, but not limited to, damages for loss of business profits, business interruption, loss of business information, or any other pecuniary loss) arising out of the use of or inability to use the Software product.",
        "contract_type": "End User License Agreement"
    },
    {
        "id": "lim_liab_03",
        "gold_clause_type": "Limitation of Liability",
        "text": "Except for liability arising from willful misconduct, gross negligence, or breaches of Section 8 (Confidentiality), neither party's cumulative liability under this Agreement shall exceed the total amount of fees received by Service Provider under the applicable Statement of Work during the six-month period immediately prior to the event giving rise to liability.",
        "contract_type": "Consulting Agreement"
    },
    {
        "id": "lim_liab_04",
        "gold_clause_type": "Limitation of Liability",
        "text": "Neither party excludes or limits liability to the other party for: (a) death or personal injury resulting from negligence; (b) fraud or fraudulent misrepresentation; or (c) any other liability to the extent the same cannot be excluded or limited by mandatory law. Subject to the foregoing sentence, Tenant's total aggregate liability under this Commercial Lease shall not exceed an amount equal to two times the annual base rent.",
        "contract_type": "Commercial Lease Agreement"
    },
    {
        "id": "lim_liab_05",
        "gold_clause_type": "Limitation of Liability",
        "text": "The aggregate liability of the Platform Operator with respect to any single occurrence or series of related occurrences arising out of this Agreement or the API Services shall be capped at the lesser of USD $50,000 or the total service charges paid by Developer in the calendar quarter preceding the incident.",
        "contract_type": "Developer API Terms"
    },

    # 2. Indemnification
    {
        "id": "indemn_01",
        "gold_clause_type": "Indemnification",
        "text": "Vendor agrees to defend, indemnify, and hold harmless Customer, its affiliates, directors, officers, employees, and agents from and against any and all claims, suits, actions, demands, liabilities, damages, losses, costs, and expenses (including reasonable attorneys' fees) arising out of or resulting from: (a) any breach of Vendor's representations or warranties herein; (b) any claim that the Deliverables or Services infringe or misappropriate any patent, copyright, trademark, trade secret, or other proprietary right of any third party; or (c) gross negligence or willful misconduct of Vendor or its personnel.",
        "contract_type": "Software Development Agreement"
    },
    {
        "id": "indemn_02",
        "gold_clause_type": "Indemnification",
        "text": "Supplier shall defend, indemnify and save harmless the Purchaser and its parent company from any loss, damage, liability, cost or expense suffered or incurred by reason of any claim made by a third party for bodily injury, death or property damage arising directly out of Supplier's negligent performance under this Purchase Order.",
        "contract_type": "Supply Chain Master Agreement"
    },
    {
        "id": "indemn_03",
        "gold_clause_type": "Indemnification",
        "text": "Each party (the 'Indemnifying Party') shall indemnify, defend, and hold harmless the other party and its officers, directors, and employees against any third-party claim, suit, or proceeding arising out of the Indemnifying Party's violation of applicable data privacy legislation or unauthorized transfer of personal data.",
        "contract_type": "Data Processing Agreement"
    },
    {
        "id": "indemn_04",
        "gold_clause_type": "Indemnification",
        "text": "The Contractor shall at all times keep the Principal indemnified against all penalties, damages, costs and expenses to which the Principal may be put by reason of any failure on the part of the Contractor to comply with the statutory obligations, building bye-laws, and labor safety regulations applicable to the Construction Works.",
        "contract_type": "EPC Construction Contract"
    },
    {
        "id": "indemn_05",
        "gold_clause_type": "Indemnification",
        "text": "Tenant covenants to hold Landlord harmless and indemnified against any claims, losses, fines, or damages incurred as a consequence of Tenant's default under this Lease, improper use of the demised premises, or toxic material discharge caused by Tenant's sub-lessees or invitees.",
        "contract_type": "Industrial Lease Agreement"
    },

    # 3. Governing Law
    {
        "id": "gov_law_01",
        "gold_clause_type": "Governing Law",
        "text": "This Agreement, and all claims or causes of action (whether in contract, tort, or statute) that may be based upon, arise out of, or relate to this Agreement, or the negotiation, execution, or performance of this Agreement, shall be governed by and construed in accordance with the substantive laws of India, without giving effect to any choice or conflict of law provision or rule. The courts situated at New Delhi shall have exclusive territorial jurisdiction over any proceedings arising hereunder.",
        "contract_type": "Commercial Lease Agreement"
    },
    {
        "id": "gov_law_02",
        "gold_clause_type": "Governing Law",
        "text": "This Agreement shall be governed by, and construed and enforced in accordance with, the laws of the State of New York without regard to its principles of conflicts of laws. The United Nations Convention on Contracts for the International Sale of Goods shall not apply.",
        "contract_type": "International Distribution Agreement"
    },
    {
        "id": "gov_law_03",
        "gold_clause_type": "Governing Law",
        "text": "The construction, validity and performance of this Agreement shall be governed in all respects by English law, and the parties agree to submit to the non-exclusive jurisdiction of the courts of England and Wales.",
        "contract_type": "Maritime Charter Agreement"
    },
    {
        "id": "gov_law_04",
        "gold_clause_type": "Governing Law",
        "text": "All rights, duties, and obligations arising out of or in connection with this Share Purchase Agreement shall be determined under the laws of the Republic of Singapore, without reference to choice of law rules.",
        "contract_type": "Share Purchase Agreement"
    },
    {
        "id": "gov_law_05",
        "gold_clause_type": "Governing Law",
        "text": "This Deed and any non-contractual obligations arising out of or in relation to it are governed by Indian law, and subject to the exclusive jurisdiction of the High Court of Judicature at Bombay.",
        "contract_type": "Debenture Trust Deed"
    },

    # 4. Dispute Resolution
    {
        "id": "disp_res_01",
        "gold_clause_type": "Dispute Resolution",
        "text": "Any dispute, controversy, difference, or claim arising out of or relating to this Agreement, including the existence, validity, interpretation, performance, breach, or termination thereof, shall be referred to and finally resolved by arbitration administered by the Delhi International Arbitration Centre (DIAC) in accordance with the Arbitration and Conciliation Act, 1996. The arbitral tribunal shall consist of a sole arbitrator appointed mutually by the parties. The seat and venue of arbitration shall be New Delhi, and the proceedings shall be conducted in English.",
        "contract_type": "Shareholders Agreement"
    },
    {
        "id": "disp_res_02",
        "gold_clause_type": "Dispute Resolution",
        "text": "In the event of any dispute arising out of this Contract, the parties shall first attempt to resolve the dispute through good faith executive negotiations between Senior Vice Presidents for a period of thirty (30) days. If unresolved, the dispute shall be submitted to the Singapore International Arbitration Centre (SIAC) under the SIAC Rules then in effect.",
        "contract_type": "Cross-Border Joint Venture"
    },
    {
        "id": "disp_res_03",
        "gold_clause_type": "Dispute Resolution",
        "text": "Any controversy or claim arising out of or relating to this contract, or the breach thereof, shall be settled by binding arbitration administered by the American Arbitration Association in accordance with its Commercial Arbitration Rules, and judgment on the award rendered by the arbitrator(s) may be entered in any court having jurisdiction thereof.",
        "contract_type": "Technology License Agreement"
    },
    {
        "id": "disp_res_04",
        "gold_clause_type": "Dispute Resolution",
        "text": "Before initiating arbitration, the parties agree to mediate any dispute under the Mediation Conciliation Rules of the Indian Council of Arbitration (ICA). If mediation fails to produce a settlement within 45 days, the dispute shall be adjudicated by an arbitral panel of three arbitrators seated in Mumbai.",
        "contract_type": "Infrastructure Concession Agreement"
    },
    {
        "id": "disp_res_05",
        "gold_clause_type": "Dispute Resolution",
        "text": "The parties irrevocably agree that any legal action, suit or proceeding arising out of or relating to this Agreement that is not subject to arbitration shall be instituted exclusively in the High Court of Delhi at New Delhi.",
        "contract_type": "Commercial Loan Agreement"
    },

    # 5. Force Majeure
    {
        "id": "force_maj_01",
        "gold_clause_type": "Force Majeure",
        "text": "Neither party shall be liable or responsible to the other party, nor be deemed to have defaulted under or breached this Agreement, for any failure or delay in fulfilling or performing any term of this Agreement (except for payment obligations), when and to the extent such failure or delay is caused by or results from acts of God, flood, fire, earthquake, explosion, war, invasion, hostilities, terrorist threats or acts, riot, civil unrest, government order, law, or action, embargoes, blockades, or national or regional emergency, provided that the affected party gives prompt written notice within five (5) business days and uses diligent efforts to end the failure or delay.",
        "contract_type": "Supply Chain Agreement"
    },
    {
        "id": "force_maj_02",
        "gold_clause_type": "Force Majeure",
        "text": "If performance of this contract by either party is prevented, hindered, or delayed by reason of any Event of Force Majeure including epidemic, quarantine restrictions, freight embargoes, or catastrophic power grid failure beyond reasonable control, the party so affected shall be excused from performance for the duration of the interruption.",
        "contract_type": "Power Purchase Agreement"
    },
    {
        "id": "force_maj_03",
        "gold_clause_type": "Force Majeure",
        "text": "A party shall not be in breach of this Agreement nor liable for delay in performing its obligations if such delay results from events, circumstances or causes beyond its reasonable control. In such circumstances the affected party shall be entitled to a reasonable extension of the time for performing such obligations. If the period of delay extends beyond 90 consecutive days, the unaffected party may terminate upon 14 days written notice.",
        "contract_type": "Manufacturing Agreement"
    },
    {
        "id": "force_maj_04",
        "gold_clause_type": "Force Majeure",
        "text": "Force Majeure Event means any event or circumstance beyond the reasonable control of the Affected Party, including acts of nature, volcanic eruption, armed conflict, civil strife, or unexpected governmental trade sanctions, provided that inability to satisfy financial obligations or economic hardship shall not constitute Force Majeure.",
        "contract_type": "Mining Concession Contract"
    },
    {
        "id": "force_maj_05",
        "gold_clause_type": "Force Majeure",
        "text": "Neither Borrower nor Lender shall be held in default for failure to perform any covenant herein due to an unavoidable casualty, cyber-warfare event affecting national clearing houses, or declaration of emergency by the Reserve Bank of India.",
        "contract_type": "Credit Facility Agreement"
    },

    # 6. Confidentiality
    {
        "id": "confid_01",
        "gold_clause_type": "Confidentiality",
        "text": "Each receiving party agrees to retain in strict confidence all non-public, confidential, or proprietary information disclosed by the disclosing party, whether disclosed orally or in writing, including without limitation technical specifications, source code, financial projections, business methodologies, customer lists, and pricing terms. The receiving party shall exercise the same degree of care to protect such Confidential Information as it uses to protect its own confidential materials of like nature, but in no event less than reasonable care, and shall not disclose Confidential Information to any third party without prior written consent.",
        "contract_type": "Non-Disclosure Agreement"
    },
    {
        "id": "confid_02",
        "gold_clause_type": "Confidentiality",
        "text": "'Proprietary Information' encompasses all confidential data, trade secrets, software algorithms, customer records, and corporate business plans disclosed by either party during the term. The recipient shall restrict disclosure solely to its officers and counsel who need to know such data and are bound by written non-disclosure covenants at least as restrictive as those contained herein.",
        "contract_type": "Merger Due Diligence Agreement"
    },
    {
        "id": "confid_03",
        "gold_clause_type": "Confidentiality",
        "text": "The obligations of confidentiality shall not apply to information which: (a) was already in the recipient's possession prior to disclosure; (b) is or becomes publicly known through no wrongful act of recipient; (c) is independently developed without reference to the Disclosing Party's Confidential Information; or (d) is required to be disclosed pursuant to a valid judicial subpoena or government order.",
        "contract_type": "Joint Venture Confidentiality Deed"
    },
    {
        "id": "confid_04",
        "gold_clause_type": "Confidentiality",
        "text": "Consultant acknowledges that during the course of providing advisory services, Consultant will have access to non-public financial modeling and proprietary client communications. Consultant agrees to hold all such confidential matter in fiduciary trust and shall not exploit or disseminate it following termination of this engagement.",
        "contract_type": "Financial Advisory Agreement"
    },
    {
        "id": "confid_05",
        "gold_clause_type": "Confidentiality",
        "text": "All documentation, technical diagrams, architectural blueprints, and source code modules delivered under this agreement constitute trade secrets and confidential information of Licensor. Licensee shall not reverse engineer, decompile, or reveal such confidential assets to any third party.",
        "contract_type": "Software Licensing Agreement"
    },

    # 7. Intellectual Property
    {
        "id": "ip_01",
        "gold_clause_type": "Intellectual Property",
        "text": "Customer shall own all right, title, and interest (including all patent, copyright, trademark, trade secret, and other intellectual property rights) in and to all Deliverables, software modifications, custom integrations, work products, and documentation developed or delivered by Service Provider under this Agreement. Service Provider hereby irrevocably assigns, transfers, and conveys to Customer all right, title, and interest in such Deliverables upon creation. Service Provider retains ownership of its pre-existing background intellectual property.",
        "contract_type": "Technology Services Agreement"
    },
    {
        "id": "ip_02",
        "gold_clause_type": "Intellectual Property",
        "text": "All inventions, innovations, software code, circuit designs, and proprietary formulas created or conceived by Employee solely or jointly during the term of employment that relate to the Company's current or demonstrably planned business shall be considered 'works made for hire' and remain the absolute property of the Employer.",
        "contract_type": "Employment Agreement"
    },
    {
        "id": "ip_03",
        "gold_clause_type": "Intellectual Property",
        "text": "Licensor grants to Licensee a non-exclusive, non-transferable, revocable license to use the Licensed Trademarks solely on marketing collateral approved in advance by Licensor. Licensee acknowledges Licensor's sole and exclusive ownership of the Trademarks and all associated goodwill.",
        "contract_type": "Trademark License Agreement"
    },
    {
        "id": "ip_04",
        "gold_clause_type": "Intellectual Property",
        "text": "No transfer of intellectual property rights is effected by this Agreement. Each party retains all right, title, and interest in its pre-existing background IP, patents, copyrights, and registered domain names, and neither party acquires any license or right except as expressly conferred herein.",
        "contract_type": "Strategic Alliance Agreement"
    },
    {
        "id": "ip_05",
        "gold_clause_type": "Intellectual Property",
        "text": "Vendor grants Client a perpetual, worldwide, royalty-free, fully paid-up license to use, reproduce, modify, and display the Documentation and Embedded Software integrated within the purchased capital equipment.",
        "contract_type": "Equipment Purchase Contract"
    },

    # 8. Payment
    {
        "id": "pay_01",
        "gold_clause_type": "Payment",
        "text": "Customer shall pay all undisputed invoiced amounts within thirty (30) calendar days of the date of Service Provider's invoice. All payments shall be made in Indian Rupees (INR) via electronic funds transfer (NEFT/RTGS) to the designated bank account of Service Provider. Any undisputed payments not received by the due date shall accrue simple interest at the rate of one percent (1.0%) per month or the highest rate permitted by applicable law, whichever is lower, calculated daily from the due date until paid in full.",
        "contract_type": "Vendor Master Agreement"
    },
    {
        "id": "pay_02",
        "gold_clause_type": "Payment",
        "text": "Client agrees to remit monthly subscription fees in advance on the first business day of each billing cycle. If payment fails or is overdue by more than fourteen (14) days, Company reserves the right to suspend API access until all outstanding arrears are satisfied in full.",
        "contract_type": "SaaS Subscription Agreement"
    },
    {
        "id": "pay_03",
        "gold_clause_type": "Payment",
        "text": "The Contract Price shall be paid in installments linked to verifiable construction milestones: 15% mobilization advance against bank guarantee, 60% in monthly running account bills, and 25% final retention released upon issuance of the Final Completion Certificate.",
        "contract_type": "Construction EPC Agreement"
    },
    {
        "id": "pay_04",
        "gold_clause_type": "Payment",
        "text": "All sums payable under this Agreement are exclusive of Value Added Tax, Goods and Services Tax (GST), and any local levies, which shall be added to invoices at the prevailing statutory rate and paid by the Lessee upon receipt of a valid tax invoice.",
        "contract_type": "Commercial Lease Agreement"
    },
    {
        "id": "pay_05",
        "gold_clause_type": "Payment",
        "text": "Borrower covenants to pay interest on the outstanding principal balance of the Term Loan at the Benchmark Rate plus an applicable margin of 2.75% per annum, payable quarterly in arrears on March 31, June 30, September 30, and December 31.",
        "contract_type": "Syndicated Loan Agreement"
    },

    # 9. Termination
    {
        "id": "term_01",
        "gold_clause_type": "Termination",
        "text": "Either party may terminate this Agreement without cause upon giving sixty (60) days prior written notice to the other party. Furthermore, either party may terminate this Agreement immediately upon written notice if: (a) the other party commits a material breach of this Agreement that is incurable, or, if curable, fails to cure such breach within thirty (30) days of receiving written notice thereof; or (b) the other party becomes insolvent, enters into receivership, liquidation, or bankruptcy, or ceases to conduct its business in the ordinary course.",
        "contract_type": "Employment Agreement"
    },
    {
        "id": "term_02",
        "gold_clause_type": "Termination",
        "text": "Company may terminate this Agreement for convenience, in whole or in part, at any time upon thirty (30) days advance written notice to Vendor, without incurring any penalty or liability other than payment for Services satisfactorily performed prior to the effective date of termination.",
        "contract_type": "Procurement Contract"
    },
    {
        "id": "term_03",
        "gold_clause_type": "Termination",
        "text": "Landlord shall have the right to immediately terminate this Lease and re-enter the Demised Premises upon the occurrence of: (i) default in the payment of Monthly Rent continuing for fifteen (15) days after written demand; or (ii) Tenant filing a voluntary petition under the Insolvency and Bankruptcy Code, 2016.",
        "contract_type": "Commercial Lease Agreement"
    },
    {
        "id": "term_04",
        "gold_clause_type": "Termination",
        "text": "Either party may terminate this Statement of Work immediately upon written notice if the other party breaches any representation or warranty in Section 9 or fails to maintain the mandatory cyber security certifications stipulated herein.",
        "contract_type": "IT Managed Services SOW"
    },
    {
        "id": "term_05",
        "gold_clause_type": "Termination",
        "text": "Upon termination or expiration of this Agreement for any reason, all licenses granted hereunder shall terminate immediately, and Licensee shall promptly destroy or return all copies of the Licensed Software and certify such destruction in writing within ten (10) business days.",
        "contract_type": "Software Distribution Agreement"
    },

    # 10. Non-Compete
    {
        "id": "non_comp_01",
        "gold_clause_type": "Non-Compete",
        "text": "During the term of employment and for a period of twenty-four (24) months following termination of employment for any reason, Employee shall not, directly or indirectly, engage in, own, manage, operate, consult for, or be employed by any enterprise or business entity that competes directly with the Company's SaaS business within the territory of India or globally.",
        "contract_type": "Employment Agreement"
    },
    {
        "id": "non_comp_02",
        "gold_clause_type": "Non-Compete",
        "text": "Founder covenants that for a period of three (3) years following the Closing Date, Founder shall not establish, invest in, or manage any business developing algorithmic high-frequency trading platforms in the United States or the European Union.",
        "contract_type": "Share Purchase Agreement"
    },
    {
        "id": "non_comp_03",
        "gold_clause_type": "Non-Compete",
        "text": "During the term of this Franchise Agreement and for twelve (12) months after its expiration, Franchisee shall not operate, license, or maintain any retail fast-food restaurant offering fried chicken products within a radius of ten (10) kilometers from the franchised location.",
        "contract_type": "Franchise Agreement"
    },
    {
        "id": "non_comp_04",
        "gold_clause_type": "Non-Compete",
        "text": "The Consultant agrees not to render competitive technical advisory services to any direct competitor of the Client listed in Exhibit B for the duration of this Consulting Agreement and for six months following project handover.",
        "contract_type": "Consulting Agreement"
    },
    {
        "id": "non_comp_05",
        "gold_clause_type": "Non-Compete",
        "text": "Partner undertakes that during the subsistence of the Partnership and for eighteen months thereafter, Partner will not engage in any competing partnership, business, or venture that mimics the primary logistics services offered by the Firm.",
        "contract_type": "Partnership Deed"
    },

    # 11. Non-Solicitation
    {
        "id": "non_sol_01",
        "gold_clause_type": "Non-Solicitation",
        "text": "During the term of this Agreement and for twelve (12) months thereafter, Consultant shall not solicit, recruit, induce, or encourage any employee, contractor, or customer of the Company to leave the Company's employ, terminate their engagement, or divert business away from the Company.",
        "contract_type": "Consulting Agreement"
    },
    {
        "id": "non_sol_02",
        "gold_clause_type": "Non-Solicitation",
        "text": "Neither party shall, during the term of this Agreement and for a period of one (1) year following its expiration or termination, actively recruit, solicit for employment, or hire any technical personnel of the other party who was directly involved in the provision of the Services without prior written authorization.",
        "contract_type": "Master Services Agreement"
    },
    {
        "id": "non_sol_03",
        "gold_clause_type": "Non-Solicitation",
        "text": "Executive agrees that during employment and for 18 months thereafter, Executive will not solicit, entice, or persuade any customer or account of Employer to transfer their account or patronage to any competing financial advisory firm.",
        "contract_type": "Executive Employment Agreement"
    },
    {
        "id": "non_sol_04",
        "gold_clause_type": "Non-Solicitation",
        "text": "Vendor agrees not to canvass, solicit, or accept business from any prospective client of Customer who was introduced to Vendor during the joint tender bidding process for a period of two years from the bid submission date.",
        "contract_type": "Teaming Agreement"
    },
    {
        "id": "non_sol_05",
        "gold_clause_type": "Non-Solicitation",
        "text": "Subcontractor covenants that it will not employ, entice away, or solicit any personnel of the Main Contractor engaged in the highway construction project during the contract lifecycle and for six months after final commissioning.",
        "contract_type": "Subcontract Agreement"
    },

    # 12. Warranties
    {
        "id": "war_01",
        "gold_clause_type": "Warranties",
        "text": "Licensor warrants that the Licensed Software will operate substantially in accordance with the published Documentation for a period of ninety (90) days from delivery. If Licensee notifies Licensor of a defect within the warranty period, Licensor's sole obligation and Licensee's exclusive remedy shall be for Licensor to use commercially reasonable efforts to correct the reproducible non-conformity or, at Licensor's option, refund the license fee paid.",
        "contract_type": "Software License Agreement"
    },
    {
        "id": "war_02",
        "gold_clause_type": "Warranties",
        "text": "EXCEPT AS EXPRESSLY STATED IN THIS SECTION, ALL SERVICES AND DELIVERABLES ARE PROVIDED 'AS IS' AND 'AS AVAILABLE'. PROVIDER DISCLAIMS ALL OTHER WARRANTIES, EXPRESS OR IMPLIED, STATUTORY OR OTHERWISE, INCLUDING WITHOUT LIMITATION WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.",
        "contract_type": "Cloud Platform Agreement"
    },
    {
        "id": "war_03",
        "gold_clause_type": "Warranties",
        "text": "Seller warrants to Buyer that the goods delivered shall be free from defects in material and workmanship, conform to agreed engineering specifications, and be new and unused for a warranty period of twelve (12) months from installation.",
        "contract_type": "Equipment Supply Agreement"
    },
    {
        "id": "war_04",
        "gold_clause_type": "Warranties",
        "text": "Service Provider warrants that it will perform all professional services in a timely, diligent, and professional manner, utilizing personnel possessing suitable expertise and in conformity with highest industry standards.",
        "contract_type": "Professional Services Contract"
    },
    {
        "id": "war_05",
        "gold_clause_type": "Warranties",
        "text": "Contractor warrants that all structural works completed under this contract shall remain structurally sound and free from water leakage or settlement defects for a defect liability warranty period of twenty-four (24) calendar months.",
        "contract_type": "Turnkey Construction Agreement"
    },

    # 13. Representations
    {
        "id": "rep_01",
        "gold_clause_type": "Representations",
        "text": "Each party represents and warrants to the other that: (i) it is a corporation duly organized, validly existing, and in good standing under the laws of its jurisdiction of incorporation; (ii) it has the full legal power, corporate authority, and authorizations necessary to execute, deliver, and perform this Agreement; and (iii) the execution and performance of this Agreement does not violate any applicable law, judicial decree, or third-party agreement.",
        "contract_type": "Joint Venture Agreement"
    },
    {
        "id": "rep_02",
        "gold_clause_type": "Representations",
        "text": "Borrower represents and warrants to Lenders that the financial statements delivered as of March 31, 2024 fairly present the financial condition of Borrower and its consolidated subsidiaries in accordance with GAAP, and there has been no material adverse change since said date.",
        "contract_type": "Credit Facility Agreement"
    },
    {
        "id": "rep_03",
        "gold_clause_type": "Representations",
        "text": "Target Company and Sellers hereby jointly represent that there are no pending litigations, administrative inquiries, arbitration proceedings, or governmental investigations against the Company that could reasonably be expected to impair its business operations.",
        "contract_type": "Share Purchase Agreement"
    },
    {
        "id": "rep_04",
        "gold_clause_type": "Representations",
        "text": "Issuer represents that all shares issued hereunder are fully paid, validly authorized, non-assessable, and free of preemptive rights, liens, pledges, or encumbrances of any kind.",
        "contract_type": "Stock Subscription Agreement"
    },
    {
        "id": "rep_05",
        "gold_clause_type": "Representations",
        "text": "Licensor represents that it is the sole and unencumbered legal and beneficial owner of all patent applications enumerated in Schedule A, and that no third party holds any adverse claim of title or ownership therein.",
        "contract_type": "Patent Assignment Agreement"
    },

    # 14. Data Protection
    {
        "id": "dp_01",
        "gold_clause_type": "Data Protection",
        "text": "To the extent Service Provider processes any Personal Data on behalf of Customer in performing the Services, Service Provider shall: (a) process such data solely in accordance with Customer's documented lawful instructions and the provisions of the Digital Personal Data Protection Act, 2023 (DPDPA); (b) implement robust technical and organizational security measures, including AES-256 encryption at rest and in transit; and (c) immediately notify Customer within twenty-four (24) hours of becoming aware of any suspected or confirmed personal data breach.",
        "contract_type": "Data Processing Addendum"
    },
    {
        "id": "dp_02",
        "gold_clause_type": "Data Protection",
        "text": "Both parties agree to comply with the European Union General Data Protection Regulation (GDPR) (Regulation (EU) 2016/679). Data Processor shall maintain comprehensive logs of data processing activities and shall not transfer personal data outside the European Economic Area without executing standard contractual clauses.",
        "contract_type": "International Data Transfer Agreement"
    },
    {
        "id": "dp_03",
        "gold_clause_type": "Data Protection",
        "text": "Customer Personal Data shall be stored exclusively in designated tier-4 data centers located within the Union of India. Service Provider shall ensure strict role-based access control, annual SOC-2 Type II audits, and prompt remediation of any detected vulnerabilities.",
        "contract_type": "Cloud Hosting Service Level Agreement"
    },
    {
        "id": "dp_04",
        "gold_clause_type": "Data Protection",
        "text": "Upon termination of the Services or upon Customer's written request, Vendor shall within thirty (30) days securely delete or return all Customer personal data and personally identifiable information, providing an officer certificate confirming sanitization.",
        "contract_type": "Enterprise SaaS Addendum"
    },
    {
        "id": "dp_05",
        "gold_clause_type": "Data Protection",
        "text": "Processor shall ensure that persons authorized to process personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality and undergo periodic security awareness training.",
        "contract_type": "Privacy & Data Security Schedule"
    },

    # 15. Assignment
    {
        "id": "assign_01",
        "gold_clause_type": "Assignment",
        "text": "Neither party may assign, transfer, delegate, or subcontract any of its rights or obligations under this Agreement, in whole or in part, without the prior written consent of the other party; provided, however, that either party may assign this Agreement without consent to a successor entity in connection with a merger, acquisition, corporate reorganization, or sale of substantially all assets, upon prompt written notice.",
        "contract_type": "Distribution Agreement"
    },
    {
        "id": "assign_02",
        "gold_clause_type": "Assignment",
        "text": "This Agreement shall be binding upon and inure to the benefit of the parties hereto and their respective permitted successors and assigns. Any attempted assignment in violation of this Section shall be null and void ab initio.",
        "contract_type": "Shareholders Agreement"
    },
    {
        "id": "assign_03",
        "gold_clause_type": "Assignment",
        "text": "Tenant shall not assign, mortgage, pledge, or encumber this Lease, nor sublet the premises or any part thereof, without obtaining the prior written consent of Landlord, which consent may be withheld in Landlord's sole and absolute discretion.",
        "contract_type": "Commercial Lease Agreement"
    },
    {
        "id": "assign_04",
        "gold_clause_type": "Assignment",
        "text": "Borrower shall not transfer or assign any of its obligations under the Credit Agreement. The Lender may at any time assign or syndicate all or a portion of its rights and commitments to one or more eligible financial institutions.",
        "contract_type": "Syndicated Loan Agreement"
    },
    {
        "id": "assign_05",
        "gold_clause_type": "Assignment",
        "text": "Contractor shall not subcontract the whole of the Works. Except where otherwise provided by the Contract, the Contractor shall not subcontract any part of the Works without the prior written consent of the Engineer.",
        "contract_type": "FIDIC Construction Contract"
    },

    # 16. Notices
    {
        "id": "notices_01",
        "gold_clause_type": "Notices",
        "text": "All notices, requests, consents, claims, demands, waivers, and other communications hereunder shall be in writing and addressed to the recipient at the registered office address specified in the preamble, and shall be delivered by hand, nationally recognized overnight courier with tracking, or sent by registered post with acknowledgment due, or sent via electronic mail with confirmed receipt.",
        "contract_type": "Franchise Agreement"
    },
    {
        "id": "notices_02",
        "gold_clause_type": "Notices",
        "text": "Any notice or formal communication given under or in connection with this Contract shall be in the English language, sent to the designated Legal Notices email address set forth in Schedule 1, and shall be deemed delivered at the time of email transmission if sent during regular business hours.",
        "contract_type": "Vendor Master Services Agreement"
    },
    {
        "id": "notices_03",
        "gold_clause_type": "Notices",
        "text": "Formal notices under this Lease shall be deemed duly given: (a) on the date of personal delivery; (b) three days after deposit in the India Post registered airmail; or (c) one business day after consignment with an express courier service (such as Blue Dart or DHL).",
        "contract_type": "Commercial Real Estate Lease"
    },
    {
        "id": "notices_04",
        "gold_clause_type": "Notices",
        "text": "All communications between Borrower and Administrative Agent shall be delivered to the physical and electronic addresses specified on the signatory pages, and any change of address must be notified ten (10) days in advance.",
        "contract_type": "Credit Agreement"
    },
    {
        "id": "notices_05",
        "gold_clause_type": "Notices",
        "text": "Every notice required under this insurance policy must be sent in writing to the Underwriter at its corporate headquarters or emailed to claims@underwriter.com referencing Policy Number.",
        "contract_type": "Commercial Insurance Policy"
    },

    # 17. Audit
    {
        "id": "audit_01",
        "gold_clause_type": "Audit",
        "text": "Upon thirty (30) days prior written notice, Company or its designated independent certified public accountants shall have the right, during normal business hours and without unreasonably disrupting Vendor's operations, to inspect and audit Vendor's books, records, systems, and facilities to verify compliance with the terms and billing calculations of this Agreement.",
        "contract_type": "Vendor Master Agreement"
    },
    {
        "id": "audit_02",
        "gold_clause_type": "Audit",
        "text": "Licensee shall maintain accurate books and records concerning its deployment of the Licensed Software. Licensor may, at its own expense and not more than once per calendar year, audit Licensee's software deployment metrics upon fourteen (14) days advance notice.",
        "contract_type": "Software License Agreement"
    },
    {
        "id": "audit_03",
        "gold_clause_type": "Audit",
        "text": "If an audit reveals that Licensee has underpaid royalty fees by more than five percent (5%) for any audited period, Licensee shall immediately remit such shortfall along with interest and reimburse Licensor for the full reasonable cost of the audit.",
        "contract_type": "Patent Royalty Agreement"
    },
    {
        "id": "audit_04",
        "gold_clause_type": "Audit",
        "text": "Client or its designated regulatory supervisory authorities shall have full access to Service Provider's operational premises, IT infrastructure, and audit logs to verify compliance with statutory banking standards and Reserve Bank guidelines.",
        "contract_type": "Banking Outsourcing Agreement"
    },
    {
        "id": "audit_05",
        "gold_clause_type": "Audit",
        "text": "The Employer reserves the right to engage an independent cost auditor to review the Contractor's project ledger, materials invoices, and labor muster rolls for all cost-plus billing items.",
        "contract_type": "Construction Management Contract"
    },

    # 18. Compliance
    {
        "id": "comp_01",
        "gold_clause_type": "Compliance",
        "text": "Both parties shall at all times comply with all applicable local, state, and central statutes, regulations, directives, and ordinances, including without limitation the Prevention of Corruption Act, 1988, the Foreign Corrupt Practices Act (FCPA), labor and environmental safety standards, and export control regulations.",
        "contract_type": "Procurement Contract"
    },
    {
        "id": "comp_02",
        "gold_clause_type": "Compliance",
        "text": "Distributor covenants that it has not offered, paid, promised to pay, or authorized the payment of any money or gift to any government official for the purpose of influencing any official act, in full adherence to the UK Bribery Act 2010.",
        "contract_type": "International Distribution Contract"
    },
    {
        "id": "comp_03",
        "gold_clause_type": "Compliance",
        "text": "Supplier represents and warrants that all mining operations and refining processes adhere to child labor prevention laws, environmental effluent discharge regulations, and the International Labour Organization (ILO) core conventions.",
        "contract_type": "Raw Materials Supply Contract"
    },
    {
        "id": "comp_04",
        "gold_clause_type": "Compliance",
        "text": "The Customer shall comply with all export and re-export restrictions and regulations administered by the U.S. Department of Commerce and shall not export the technology to embargoed territories.",
        "contract_type": "Technology Transfer Agreement"
    },
    {
        "id": "comp_05",
        "gold_clause_type": "Compliance",
        "text": "Borrower covenants that it and each of its subsidiaries is in compliance in all material respects with all applicable environmental protection, occupational safety, and money laundering prevention laws.",
        "contract_type": "Credit Facility Agreement"
    },

    # 19. Service Levels
    {
        "id": "sla_01",
        "gold_clause_type": "Service Levels",
        "text": "Provider commits that the Cloud Platform will achieve Monthly Uptime of at least 99.9% during each calendar month. In the event of failure to meet this availability threshold, Customer shall be entitled to receive service credits equal to 10% of the monthly subscription fee for each 0.5% drop in availability below 99.9%, up to a maximum credit of 50% of the monthly fee.",
        "contract_type": "SLA Agreement"
    },
    {
        "id": "sla_02",
        "gold_clause_type": "Service Levels",
        "text": "Service Provider will respond to Severity 1 (Critical Outage) incident tickets within fifteen (15) minutes and achieve workaround or full resolution within four (4) consecutive hours on a 24x7x365 basis.",
        "contract_type": "IT Managed Services Agreement"
    },
    {
        "id": "sla_03",
        "gold_clause_type": "Service Levels",
        "text": "The network availability target is 99.95% measured over a 30-day billing window, excluding emergency maintenance announced at least 48 hours in advance during scheduled weekend maintenance windows.",
        "contract_type": "Telecom Carrier Agreement"
    },
    {
        "id": "sla_04",
        "gold_clause_type": "Service Levels",
        "text": "Should the API error rate exceed 0.5% of total request volume over any consecutive two-hour period, Provider shall immediately initiate root-cause investigation and issue hourly status bulletins until restored.",
        "contract_type": "Fintech API Agreement"
    },
    {
        "id": "sla_05",
        "gold_clause_type": "Service Levels",
        "text": "Vendor agrees to maintain a Mean Time to Repair (MTTR) of less than 120 minutes for hardware component failures at the collocation datacenter.",
        "contract_type": "Datacenter Hosting SOW"
    },

    # 20. Term
    {
        "id": "term_len_01",
        "gold_clause_type": "Term",
        "text": "The term of this Agreement shall commence on the Effective Date and shall continue in full force and effect for an initial period of three (3) calendar years, unless terminated earlier in accordance with the express provisions of Section 12.",
        "contract_type": "Master Services Agreement"
    },
    {
        "id": "term_len_02",
        "gold_clause_type": "Term",
        "text": "The Initial Term of this Commercial Lease shall be five (5) years commencing on June 1, 2024 and terminating on May 31, 2029, unless extended by mutual written agreement of Landlord and Tenant.",
        "contract_type": "Commercial Lease Agreement"
    },
    {
        "id": "term_len_03",
        "gold_clause_type": "Term",
        "text": "This Agreement shall take effect on January 1st and shall endure for a fixed term of twelve (12) months, expiring automatically on December 31st without requirement of further notice.",
        "contract_type": "Annual Maintenance Contract"
    },
    {
        "id": "term_len_04",
        "gold_clause_type": "Term",
        "text": "The duration of the consulting engagement shall be six (6) months from the Project Kickoff Date, subject to extension upon mutual execution of an addendum.",
        "contract_type": "Consulting Agreement"
    },
    {
        "id": "term_len_05",
        "gold_clause_type": "Term",
        "text": "The Partnership hereby established shall commence as of the date of execution of these presents and shall continue for a period of ten (10) years.",
        "contract_type": "Partnership Deed"
    },

    # 21. Renewal
    {
        "id": "renew_01",
        "gold_clause_type": "Renewal",
        "text": "Upon expiration of the Initial Term, this Agreement shall automatically renew for successive one (1) year renewal terms, unless either party delivers written notice of its intention not to renew at least sixty (60) days prior to the expiration of the then-current term.",
        "contract_type": "Software Subscription Agreement"
    },
    {
        "id": "renew_02",
        "gold_clause_type": "Renewal",
        "text": "Tenant shall have the option to renew this Lease for two consecutive periods of three (3) years each by giving Landlord written notice of election to renew not less than six (6) months prior to lease expiration.",
        "contract_type": "Commercial Lease Agreement"
    },
    {
        "id": "renew_03",
        "gold_clause_type": "Renewal",
        "text": "This contract shall be renewed on an annual basis upon mutual agreement regarding revised fee schedules, provided notice requesting renewal is submitted at least 45 days prior to anniversary date.",
        "contract_type": "Security Services Agreement"
    },
    {
        "id": "renew_04",
        "gold_clause_type": "Renewal",
        "text": "Unless terminated in accordance with Section 8, the subscription term shall evergreen and renew automatically for monthly intervals at then-prevailing list price unless cancelled prior to billing cut-off.",
        "contract_type": "Cloud Services Terms"
    },
    {
        "id": "renew_05",
        "gold_clause_type": "Renewal",
        "text": "The Distributor's right of renewal is contingent upon achieving minimum annual purchase thresholds of $1,000,000 during the preceding contractual term.",
        "contract_type": "Distribution Agreement"
    },

    # 22. Insurance
    {
        "id": "insur_01",
        "gold_clause_type": "Insurance",
        "text": "Throughout the term of this Agreement and for one year thereafter, Contractor shall maintain at its own expense comprehensive commercial general liability insurance with limits not less than INR 10,000,000 per occurrence, professional indemnity (errors & omissions) insurance of INR 20,000,000, and statutory workers' compensation coverage.",
        "contract_type": "Construction Services Agreement"
    },
    {
        "id": "insur_02",
        "gold_clause_type": "Insurance",
        "text": "Vendor shall secure and maintain throughout the term: (a) Cyber Liability insurance with limits of $5,000,000 per claim covering privacy violations and data loss; and (b) Commercial General Liability insurance of $2,000,000 aggregate.",
        "contract_type": "Cloud Security Agreement"
    },
    {
        "id": "insur_03",
        "gold_clause_type": "Insurance",
        "text": "Tenant shall keep the demised premises insured against fire, lightning, earthquake, and standard perils under an all-risk commercial property insurance policy for full replacement value, naming Landlord as additional insured.",
        "contract_type": "Commercial Lease Agreement"
    },
    {
        "id": "insur_04",
        "gold_clause_type": "Insurance",
        "text": "The Consultant shall carry Professional Liability / Errors and Omissions insurance in an amount not less than $1,000,000 per claim and provide certificate of insurance prior to commencement of work.",
        "contract_type": "Advisory Services Contract"
    },
    {
        "id": "insur_05",
        "gold_clause_type": "Insurance",
        "text": "Transporter shall maintain comprehensive motor fleet insurance and transit cargo indemnity insurance protecting goods against damage or pilferage up to INR 50,00,000 per shipment.",
        "contract_type": "Logistics & Transport Agreement"
    }
]


# 9 Canonical Case Document Classes: 5 diverse documents each (45 total)
CASE_DOCUMENTS_DATA = [
    # 1. FIR (First Information Report)
    {
        "id": "doc_fir_01",
        "document_name": "01_FIRST_INFORMATION_REPORT_FIR_0412_2024.pdf",
        "gold_category": "FIR",
        "sample_text": "FIRST INFORMATION REPORT (Under Section 154 Cr.P.C. / Section 173 BNSS)\n1. District: New Delhi, Police Station: Mandir Marg, Year: 2024, FIR No: 0412/2024, Date: 12/08/2024.\n2. Acts and Sections: Indian Penal Code 1860, Sections 406, 420, 468, 471, 120-B IPC.\n3. Occurrence of Offence: Day: Saturday, Date: 10/08/2024, Time: 19:30 hrs.\n4. Type of Information: Written Complaint by Ramesh Gupta, Director of Apex FinTech Innovations Ltd.\nBrief Facts: The accused dishonestly induced complainant to disburse escrow funds based on forged security audit certificate."
    },
    {
        "id": "doc_fir_02",
        "document_name": "02_FIR_CYBER_CRIME_CELL_FIR_089_2024.pdf",
        "gold_category": "FIR",
        "sample_text": "FIRST INFORMATION REPORT under Section 154 Code of Criminal Procedure\nPolice Station: Special Cell (Cyber Crime), New Delhi\nFIR Number: 089/2024, Date: 04/03/2024\nSections: 66C, 66D Information Technology Act 2000 r/w 420, 120B IPC\nComplainant: Axis Digital Payments Pvt Ltd\nDetails: Unauthorized electronic funds siphon of INR 1.8 Crores through credential spoofing on banking gateway."
    },
    {
        "id": "doc_fir_03",
        "document_name": "03_FIR_ECONOMIC_OFFENCES_WING_EOW_2024.pdf",
        "gold_category": "FIR",
        "sample_text": "FORM I - FIRST INFORMATION REPORT (Section 154 CrPC)\nEconomic Offences Wing (EOW), Mandir Marg, Crime Branch\nFIR No: EOW/2024/0144, Dated: 19/05/2024\nMajor Offences: 409, 420, 467, 471 Indian Penal Code\nAllegation: Misappropriation of public investor deposits by directors of Horizon Realty Developers Ltd."
    },
    {
        "id": "doc_fir_04",
        "document_name": "04_FIR_ASSAULT_AND_TRESPASS_PS_HAUZ_KHAS.pdf",
        "gold_category": "FIR",
        "sample_text": "INTEGRATED POLICE REPORT / FIRST INFORMATION REPORT\nState: NCT of Delhi, PS Hauz Khas, FIR No: 0521/2024\nSections: 323, 341, 506, 34 IPC / Sec 115, 126, 351 BNSS\nTime of Occurrence: 22:15 hours, Location: Commercial Complex C-Block\nSummary: Complainant was physically intercepted and intimidated by recovery agents over commercial dispute."
    },
    {
        "id": "doc_fir_05",
        "document_name": "05_FIR_CORRUPTION_PREVENTION_ACB.pdf",
        "gold_category": "FIR",
        "sample_text": "FIRST INFORMATION REPORT - ANTI-CORRUPTION BRANCH\nACB Police Station, Old Secretariat, Delhi\nFIR No: ACB-2024-0012\nActs: Sections 7, 13(1)(b) Prevention of Corruption Act, 1988\nInformation: Trap case involving illegal gratification demanded by building inspector for issuing completion certificate."
    },

    # 2. COURT_ORDER
    {
        "id": "doc_order_01",
        "document_name": "01_BAIL_AND_SUMMONS_ORDER_CRL_MISC_342_2024.pdf",
        "gold_category": "COURT_ORDER",
        "sample_text": "IN THE COURT OF CHIEF METROPOLITAN MAGISTRATE, PATIALA HOUSE COURTS, NEW DELHI\nCrl. Misc. No. 342/2024\nIn the matter of: State v. Sameer Verma & Anr. (FIR No. 0412/2024, PS Mandir Marg)\nORDER ON REGULAR BAIL APPLICATION UNDER SECTION 437 CrPC / SECTION 480 BNSS\nHeard rival submissions. Considering dispute hinges upon commercial agreement dated 15/01/2024, custody is not required. Bail granted on bond of INR 1,00,000."
    },
    {
        "id": "doc_order_02",
        "document_name": "02_HIGH_COURT_ANTICIPATORY_BAIL_ORDER.pdf",
        "gold_category": "COURT_ORDER",
        "sample_text": "IN THE HIGH COURT OF DELHI AT NEW DELHI\nBAIL APPLN. NO. 1892/2024\nCORAM: HON'BLE MR. JUSTICE MANOJ KUMAR OHRI\nORDER DATED 14.07.2024\nApplication under Section 438 Cr.P.C. for grant of pre-arrest bail. In the event of arrest, petitioner shall be released on bail subject to joining investigation as and when directed."
    },
    {
        "id": "doc_order_03",
        "document_name": "03_DISTRICT_COURT_INTERIM_INJUNCTION_ORDER.pdf",
        "gold_category": "COURT_ORDER",
        "sample_text": "IN THE COURT OF ADDITIONAL DISTRICT JUDGE, SAKET COURTS, NEW DELHI\nCS (Comm) No. 420/2024\nORDER UNDER ORDER XXXIX RULES 1 & 2 CPC\nPlaintiff has made out a prima facie case for ad-interim ex-parte injunction. Defendants are restrained from alienating suit property until next date of hearing."
    },
    {
        "id": "doc_order_04",
        "document_name": "04_SUPREME_COURT_SLP_DISMISSAL_ORDER.pdf",
        "gold_category": "COURT_ORDER",
        "sample_text": "IN THE SUPREME COURT OF INDIA (RECORD OF PROCEEDINGS)\nSPECIAL LEAVE TO APPEAL (CRL.) NO. 8920/2024\nUPON hearing the counsel the Court made the following ORDER: We find no reason to interfere with the impugned order of the High Court. The Special Leave Petition is dismissed."
    },
    {
        "id": "doc_order_05",
        "document_name": "05_COMMERCIAL_COURT_SUMMARY_JUDGMENT_ORDER.pdf",
        "gold_category": "COURT_ORDER",
        "sample_text": "IN THE COURT OF DISTRICT JUDGE (COMMERCIAL COURT-02), NEW DELHI\nCOMMERCIAL SUIT NO. 55/2023\nORDER ON APPLICATION UNDER ORDER XIII-A CPC FOR SUMMARY JUDGMENT\nThe defendant having failed to raise any genuine triable issue, summary decree is hereby passed in favor of the plaintiff for INR 64,50,000 along with 9% interest."
    },

    # 3. CHARGE_SHEET
    {
        "id": "doc_cs_01",
        "document_name": "01_FINAL_POLICE_REPORT_CHARGE_SHEET_78_2024.pdf",
        "gold_category": "CHARGE_SHEET",
        "sample_text": "IN THE COURT OF METROPOLITAN MAGISTRATE, NEW DELHI\nFINAL REPORT / CHARGE SHEET UNDER SECTION 173(2) Cr.P.C. / SECTION 193(3) BNSS\nPolice Station: Mandir Marg, District: New Delhi, Charge Sheet No: 78/2024, Date: 24/09/2024\nFIR No: 0412/2024 Date: 12/08/2024\nName of Investigating Officer: Inspector Rajeshwar Singh, Badge #3812\nOffences Charged: Sections 406, 420, 468, 471, 120-B of Indian Penal Code."
    },
    {
        "id": "doc_cs_02",
        "document_name": "02_POLICE_REPORT_FINAL_CLOSURE_REPORT.pdf",
        "gold_category": "CHARGE_SHEET",
        "sample_text": "FINAL POLICE REPORT UNDER SECTION 173 Cr.P.C. (CLOSURE REPORT / UNTRACED REPORT)\nPS Cyber Cell, Rohini, New Delhi\nCharge Sheet / Final Form No: 12/2024 in FIR 340/2023\nInvestigation reveals that dispute is purely of civil nature arising from breach of software SLA. No criminal culpability substantiated."
    },
    {
        "id": "doc_cs_03",
        "document_name": "03_SUPPLEMENTARY_CHARGE_SHEET_EOW.pdf",
        "gold_category": "CHARGE_SHEET",
        "sample_text": "SUPPLEMENTARY CHARGE SHEET UNDER SECTION 173(8) Cr.P.C.\nCourt of Special Judge (PC Act), Rouse Avenue Courts, New Delhi\nState through CBI v. A.K. Sharma & Others\nSupplementary investigation incorporates CFSL handwriting analysis report confirming forged endorsement on vendor ledger."
    },
    {
        "id": "doc_cs_04",
        "document_name": "04_CHARGE_SHEET_NARCOTICS_CELL.pdf",
        "gold_category": "CHARGE_SHEET",
        "sample_text": "IN THE COURT OF SPECIAL JUDGE (NDPS), PATIALA HOUSE COURTS\nPOLICE REPORT UNDER SECTION 173(2) CrPC / FINAL CHARGE SHEET\nNarcotics Control Bureau (NCB), Crime No: 05/2024\nAccused persons sent for trial under Sections 8(c), 20(b)(ii)(C), 29 NDPS Act."
    },
    {
        "id": "doc_cs_05",
        "document_name": "05_FINAL_INVESTIGATION_REPORT_CRIME_BRANCH.pdf",
        "gold_category": "CHARGE_SHEET",
        "sample_text": "CRIME BRANCH INVESTIGATION REPORT / CHARGESHEET\nPolice Station Crime Branch (Central), Delhi\nFinal Report Form under Section 173 CrPC in FIR 98/2024\nDetails of evidence collected against Accused No. 1 and 2 demonstrating deceptive inducement under IPC 420."
    },

    # 4. WITNESS_STATEMENT
    {
        "id": "doc_ws_01",
        "gold_category": "WITNESS_STATEMENT",
        "document_name": "01_PW1_STATEMENT_RECORDED_SEC161_CRPC.pdf",
        "sample_text": "STATEMENT OF WITNESS UNDER SECTION 161 Cr.P.C. / SECTION 180 BNSS\nPolice Station: Mandir Marg, FIR No: 0412/2024\nName of Witness: Ramesh Gupta, Age: 48 years, Occupation: CFO, Apex FinTech Innovations Ltd.\nStatement recorded by: Sub-Inspector Amit Kumar.\nStatement: Questioned regarding negotiation meeting on 10/08/2024. Verbal argument took place regarding escrow reconciliation ledger. No weapon brandished."
    },
    {
        "id": "doc_ws_02",
        "gold_category": "WITNESS_STATEMENT",
        "document_name": "02_STATEMENT_BEFORE_MAGISTRATE_SEC164_CRPC.pdf",
        "sample_text": "CONFIDENTIAL RECORD OF WITNESS STATEMENT UNDER SECTION 164 Cr.P.C.\nIn the Court of Metropolitan Magistrate-03, Patiala House Courts\nWitnes: Ms. Neha Sharma, Lead QA Engineer, Zenith Cloud Technologies\nSolemn affirmation: I state that I was instructed by CFO Singhal to alter the deployment milestone timestamp on the Jira tracker."
    },
    {
        "id": "doc_ws_03",
        "gold_category": "WITNESS_STATEMENT",
        "document_name": "03_PW2_DEPOSITION_EXAMINATION_IN_CHIEF.pdf",
        "sample_text": "IN THE COURT OF DISTRICT & SESSIONS JUDGE, TIS HAZARI\nTESTIMONY OF PROSECUTION WITNESS NO. 2 (PW-2)\nName: Sh. Harish Chandra, Age 52, Bank Branch Manager\nExamination-in-Chief by Ld. Public Prosecutor: I identify Exhibit P-4 as the certified statement of account of the accused entity."
    },
    {
        "id": "doc_ws_04",
        "gold_category": "WITNESS_STATEMENT",
        "document_name": "04_CROSS_EXAMINATION_TRANSCRIPT_PW1.pdf",
        "sample_text": "CROSS-EXAMINATION OF PW-1 BY DEFENSE ADVOCATE\nQuestion: Did you inspect the server deployment logs on AWS before registering the FIR?\nAnswer: No, I relied upon the internal email report submitted by our finance controller."
    },
    {
        "id": "doc_ws_05",
        "gold_category": "WITNESS_STATEMENT",
        "document_name": "05_INDEPENDENT_PANCH_WITNESS_STATEMENT_161.pdf",
        "sample_text": "STATEMENT OF PANCH WITNESS UNDER SECTION 161 CrPC\nName: Mukesh Joshi, Shopkeeper, Okhla Industrial Area\nWitness explains that police asked him to attest the seizure memo of two hard drives seized from office premises."
    },

    # 5. FORENSIC_REPORT
    {
        "id": "doc_fr_01",
        "gold_category": "FORENSIC_REPORT",
        "document_name": "01_CENTRAL_FORENSIC_SCIENCE_REPORT_CFSL_DELHI.pdf",
        "sample_text": "GOVERNMENT OF INDIA, MINISTRY OF HOME AFFAIRS\nCENTRAL FORENSIC SCIENCE LABORATORY (CFSL), CBI, NEW DELHI\nReport No: CFSL-2024-DOC-8914, Date of Issue: 18/09/2024\nSubject: Forensic examination of questioned digital signature and stamp on Escrow Release Certificate #CG-8829.\nResults of Examination: Cryptographic analysis indicates digital signature hash does not match CCA public key."
    },
    {
        "id": "doc_fr_02",
        "gold_category": "FORENSIC_REPORT",
        "document_name": "02_FSL_DIGITAL_CYBER_MOBILE_EXTRACTION_REPORT.pdf",
        "sample_text": "FORENSIC SCIENCE LABORATORY (FSL), GOVT. OF NCT OF DELHI\nDigital Forensics Division Report No: FSL/2024/CYBER/4120\nDevice Analyzed: iPhone 14 Pro, IMEI: 359102849102910\nExtracted Artifacts: WhatsApp database extraction recovered deleted chats confirming discussions regarding escrow shortfall."
    },
    {
        "id": "doc_fr_03",
        "gold_category": "FORENSIC_REPORT",
        "document_name": "03_HANDWRITING_EXPERT_OPINION_SECTION_45_IEA.pdf",
        "sample_text": "OPINION OF GOVERNMENT EXAMINER OF QUESTIONED DOCUMENTS (GEQD)\nForensic Document Examination under Section 45 Indian Evidence Act / Section 39 BSA\nComparison of standard signatures (S1-S10) with questioned signature (Q1) on promissory note indicates simulated forgery."
    },
    {
        "id": "doc_fr_04",
        "gold_category": "FORENSIC_REPORT",
        "document_name": "04_MEDICO_LEGAL_CERTIFICATE_MLC_AIIMS.pdf",
        "sample_text": "ALL INDIA INSTITUTE OF MEDICAL SCIENCES (AIIMS), NEW DELHI\nDEPARTMENT OF FORENSIC MEDICINE & CASUALTY\nMEDICO-LEGAL CERTIFICATE (MLC) NO: 2024-MLC-7819\nExamination of: Ramesh Gupta, Date: 12/08/2024 at 05:30 AM\nInjuries: Linear abrasion of 1.2 cm over left forearm, simple in nature, caused by blunt impact. No bone fracture."
    },
    {
        "id": "doc_fr_05",
        "gold_category": "FORENSIC_REPORT",
        "document_name": "05_POST_MORTEM_FORENSIC_PATHOLOGY_REPORT.pdf",
        "sample_text": "DEPARTMENT OF FORENSIC PATHOLOGY, MAULANA AZAD MEDICAL COLLEGE\nPOST-MORTEM AUTOPSY REPORT NO: PM-412-2024\nTime since death: approximately 24 to 36 hours. Cause of death is respiratory arrest secondary to organophosphorus poisoning."
    },

    # 6. EVIDENCE_PHOTO
    {
        "id": "doc_ep_01",
        "gold_category": "EVIDENCE_PHOTO",
        "document_name": "01_SEIZURE_PANCHNAMA_AND_SPOT_EVIDENCE_PHOTO.pdf",
        "sample_text": "SEIZURE MEMORANDUM & SCENE OF CRIME PHOTOGRAPHIC LOG\nPS Mandir Marg, Case FIR No. 0412/2024.\nDate & Time of Seizure: 14/08/2024 at 14:15 hrs.\nLocation: Office cabin of Accused, Zenith Towers, Okhla Phase-III, New Delhi.\nPhysical Item Seized: One Apple MacBook Pro 16-inch, Space Grey.\nPhotographic Attachment: Photo Exhibit P-1 showing device on desk with AWS console."
    },
    {
        "id": "doc_ep_02",
        "gold_category": "EVIDENCE_PHOTO",
        "document_name": "02_CCTV_STILL_FRAME_PHOTOGRAPHIC_EXHIBIT.pdf",
        "sample_text": "CCTV FOOTAGE SCREENSHOT AND PHOTOGRAPHIC EVIDENCE LOG\nCamera Location: Elevator Lobby, 4th Floor, Tech Park\nTimestamp: 10/08/2024 19:42:10 hrs\nPhotographic Exhibit P-3: High-resolution frame capture depicting Complainant exiting meeting room without signs of physical distress."
    },
    {
        "id": "doc_ep_03",
        "gold_category": "EVIDENCE_PHOTO",
        "document_name": "03_CRIME_SCENE_INSPECTION_PHOTO_ALBUM.pdf",
        "sample_text": "SPOT INSPECTION MEMORANDUM & CRIME SCENE PHOTOGRAPHIC ALBUM\nPrepared by Forensic Mobile Unit, District New Delhi\nExhibit Photos 1 to 12 showing conference room layout, unbroken glass partitions, and seized ledger documents."
    },
    {
        "id": "doc_ep_04",
        "gold_category": "EVIDENCE_PHOTO",
        "document_name": "04_VEHICLE_COLLISION_DAMAGE_PHOTOGRAPH.pdf",
        "sample_text": "MOTOR VEHICLE ACCIDENT SITE PHOTOGRAPHIC RECORD\nInspection by Mechanical Inspector under Section 134 Motor Vehicles Act\nPhotographic Exhibit depicting rear bumper dent and brake-mark skid patterns measured on carriageway."
    },
    {
        "id": "doc_ep_05",
        "gold_category": "EVIDENCE_PHOTO",
        "document_name": "05_INVENTORY_SEIZURE_PHOTOGRAPHS_CASH_JEWELRY.pdf",
        "sample_text": "INCOME TAX SEARCH & SEIZURE PHOTOGRAPHIC INVENTORY\nPanchnama Annexure P-4: Photographic documentation of recovered Indian currency notes and physical vault opening."
    },

    # 7. LEGAL_NOTICE
    {
        "id": "doc_ln_01",
        "gold_category": "LEGAL_NOTICE",
        "document_name": "01_FORMAL_LEGAL_DEMAND_NOTICE_SINGHANIA_PARTNERS.pdf",
        "sample_text": "SINGHANIA & PARTNERS LLP, ADVOCATES & LEGAL CONSULTANTS\nRef: SP/LIT/2024/0812, Date: 05/08/2024\nTO: Zenith Cloud Technologies Private Limited\nSUBJECT: LEGAL NOTICE FOR BREACH OF MASTER SOFTWARE ESCROW AGREEMENT DATED 15/01/2024 AND DEMAND FOR REFUND OF INR 4,25,00,000/-.\nUnder instructions from our client, M/s Apex FinTech Innovations Ltd., we call upon you to cure the default within 15 days failing which legal proceedings will commence."
    },
    {
        "id": "doc_ln_02",
        "gold_category": "LEGAL_NOTICE",
        "document_name": "02_STATUTORY_DEMAND_NOTICE_SEC138_NI_ACT.pdf",
        "gold_category": "LEGAL_NOTICE",
        "sample_text": "STATUTORY NOTICE UNDER SECTION 138 OF THE NEGOTIABLE INSTRUMENTS ACT, 1881\nDate: 22/07/2024\nTo: Sameer Verma, Director, Zenith Technologies\nPlease take notice that Cheque No. 492019 dated 15/06/2024 for INR 50,00,000 was dishonored with remarks 'Funds Insufficient'. You are demanded to pay within 15 days."
    },
    {
        "id": "doc_ln_03",
        "gold_category": "LEGAL_NOTICE",
        "document_name": "03_NOTICE_INVOKING_ARBITRATION_SECTION_21.pdf",
        "gold_category": "LEGAL_NOTICE",
        "sample_text": "NOTICE OF ARBITRATION UNDER SECTION 21 OF ARBITRATION & CONCILIATION ACT 1996\nDate: 14/09/2024\nIn re: Dispute under MSA dated 12/02/2022\nWe hereby invoke arbitration and propose the appointment of Hon'ble Justice (Retd.) K.S. Radhakrishnan as sole arbitrator."
    },
    {
        "id": "doc_ln_04",
        "gold_category": "LEGAL_NOTICE",
        "document_name": "04_CEASE_AND_DESIST_TRADEMARK_INFRINGEMENT.pdf",
        "gold_category": "LEGAL_NOTICE",
        "sample_text": "CEASE AND DESIST NOTICE - TRADEMARK AND COPYRIGHT INFRINGEMENT\nFrom: Lall & Sethi Intellectual Property Advocates\nTo: CloudZen Systems Pvt Ltd\nDemand to immediately cease all unauthorized use of the registered mark 'ZENITH CLOUD' within 7 days."
    },
    {
        "id": "doc_ln_05",
        "gold_category": "LEGAL_NOTICE",
        "document_name": "05_EVICTION_NOTICE_TRANSFER_OF_PROPERTY_ACT.pdf",
        "gold_category": "LEGAL_NOTICE",
        "sample_text": "NOTICE OF TERMINATION OF TENANCY UNDER SECTION 106 TRANSFER OF PROPERTY ACT 1882\nTo: M/s Zenith Retailers\nTake notice that your monthly tenancy in respect of premises Shop #14 is terminated with effect from expiration of 15 days."
    },

    # 8. PETITION_AFFIDAVIT
    {
        "id": "doc_pa_01",
        "gold_category": "PETITION_AFFIDAVIT",
        "document_name": "01_CRIMINAL_MISC_MAIN_PETITION_SEC482_CRPC.pdf",
        "sample_text": "IN THE HIGH COURT OF DELHI AT NEW DELHI\nCRL. M.C. NO. 4920 OF 2024\nIN THE MATTER OF: SAMEER VERMA & ANR. ...PETITIONERS\nVERSUS\nSTATE (NCT OF DELHI) & ANR. ...RESPONDENTS\nPETITION UNDER SECTION 482 CRPC / SECTION 528 BNSS FOR QUASHING OF FIR NO. 0412/2024 REGISTERED AT PS MANDIR MARG AND ALL CONSEQUENTIAL PROCEEDINGS.\nDispute is purely commercial arising out of software escrow contract."
    },
    {
        "id": "doc_pa_02",
        "gold_category": "PETITION_AFFIDAVIT",
        "document_name": "02_AFFIDAVIT_IN_SUPPORT_OF_INJUNCTION_APPLICATION.pdf",
        "sample_text": "IN THE HIGH COURT OF DELHI AT NEW DELHI\nIA NO. 4819/2024 IN CS(COMM) NO. 210/2024\nAFFIDAVIT OF RAMESH GUPTA, S/O LATE O.P. GUPTA\nI, the deponent above-named, do hereby solemnly affirm and state on oath: 1. That I am the Director of the Plaintiff company and competent to depose."
    },
    {
        "id": "doc_pa_03",
        "gold_category": "PETITION_AFFIDAVIT",
        "document_name": "03_WRIT_PETITION_ARTICLE_226_CONSTITUTION.pdf",
        "sample_text": "IN THE HIGH COURT OF JUDICATURE AT BOMBAY\nWRIT PETITION (CIVIL) NO. 9210 OF 2024\nPETITION UNDER ARTICLE 226 OF THE CONSTITUTION OF INDIA\nPraying for issuance of a Writ of Mandamus directing the respondent Municipal Corporation to de-seal commercial premises."
    },
    {
        "id": "doc_pa_04",
        "gold_category": "PETITION_AFFIDAVIT",
        "document_name": "04_SECTION_9_ARBITRATION_INTERIM_MEASURES_PETITION.pdf",
        "sample_text": "IN THE HIGH COURT OF DELHI AT NEW DELHI\nOMP (I) (COMM.) NO. 112/2024\nPETITION UNDER SECTION 9 OF THE ARBITRATION AND CONCILIATION ACT, 1996 FOR INTERIM PROTECTION\nSeeking urgent freezing of escrow bank account pending constitution of arbitral tribunal."
    },
    {
        "id": "doc_pa_05",
        "gold_category": "PETITION_AFFIDAVIT",
        "document_name": "05_INSOLVENCY_PETITION_SECTION_7_IBC_NCLT.pdf",
        "sample_text": "BEFORE THE NATIONAL COMPANY LAW TRIBUNAL (NCLT), NEW DELHI BENCH\nCOMPANY PETITION (IB) NO. 410/ND/2024\nAPPLICATION UNDER SECTION 7 OF THE INSOLVENCY AND BANKRUPTCY CODE, 2016\nBy Financial Creditor against Corporate Debtor for initiation of Corporate Insolvency Resolution Process."
    },

    # 9. OTHER
    {
        "id": "doc_oth_01",
        "gold_category": "OTHER",
        "document_name": "01_CERTIFICATE_OF_INCORPORATION_AND_MEMORANDUM.pdf",
        "sample_text": "GOVERNMENT OF INDIA, MINISTRY OF CORPORATE AFFAIRS\nREGISTRAR OF COMPANIES, NCT OF DELHI AND HARYANA\nCERTIFICATE OF INCORPORATION [Pursuant to sub-section (2) of section 7 of Companies Act 2013]\nCorporate Identity Number (CIN): U72900DL2021PTC381920\nCompany Name: Zenith Cloud Technologies Private Limited."
    },
    {
        "id": "doc_oth_02",
        "gold_category": "OTHER",
        "document_name": "02_ANNUAL_FINANCIAL_AUDIT_REPORT_BALANCE_SHEET.pdf",
        "sample_text": "INDEPENDENT AUDITOR'S REPORT TO THE MEMBERS OF APEX FINTECH LTD\nReport on the Audit of the Standalone Financial Statements\nWe have audited the accompanying financial statements comprising Balance Sheet as at March 31, 2024 and Statement of Profit and Loss."
    },
    {
        "id": "doc_oth_03",
        "gold_category": "OTHER",
        "document_name": "03_RESERVE_BANK_OF_INDIA_CIRCULAR_MASTER_DIRECTION.pdf",
        "sample_text": "RESERVE BANK OF INDIA, DEPARTMENT OF REGULATION, CENTRAL OFFICE, MUMBAI\nRBI/2024-25/18, Master Direction - Outsourcing of Information Technology Services\nTo: All Scheduled Commercial Banks and Non-Banking Financial Companies."
    },
    {
        "id": "doc_oth_04",
        "gold_category": "OTHER",
        "document_name": "04_STANDARD_SOFTWARE_DEVELOPMENT_SPECIFICATION.pdf",
        "sample_text": "TECHNICAL ARCHITECTURAL SPECIFICATION AND API BLUEPRINT\nProject: Escrow Core Gateway v2.4\nContains database schema, REST API endpoint definitions, JSON payloads, and network firewall topology diagrams."
    },
    {
        "id": "doc_oth_05",
        "gold_category": "OTHER",
        "document_name": "05_BOARD_RESOLUTION_AUTHORIZING_SIGNATORY.pdf",
        "sample_text": "CERTIFIED TRUE COPY OF THE RESOLUTION PASSED AT THE MEETING OF THE BOARD OF DIRECTORS OF ZENITH TECHNOLOGIES\nResolved that Mr. Sameer Verma, MD, be authorized to execute contracts, tenders, and banking instruments on behalf of the company."
    }
]

def main():
    clauses_file = BENCHMARKS_DIR / "gold_contract_clauses.json"
    with open(clauses_file, "w", encoding="utf-8") as f:
        json.dump(CONTRACT_CLAUSES_DATA, f, indent=2)
    print(f"Generated {len(CONTRACT_CLAUSES_DATA)} contract clauses across 22 CUAD classes -> {clauses_file}")

    case_docs_file = BENCHMARKS_DIR / "gold_case_documents.json"
    with open(case_docs_file, "w", encoding="utf-8") as f:
        json.dump(CASE_DOCUMENTS_DATA, f, indent=2)
    print(f"Generated {len(CASE_DOCUMENTS_DATA)} case documents across 9 classes -> {case_docs_file}")

if __name__ == "__main__":
    main()

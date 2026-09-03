# -*- coding: utf-8 -*-
"""
legal_data.py
=============
The KNOWLEDGE BASE of the LegalMitra project.

Everything the website shows, and everything the chatbot answers from, lives in
this one file. It is written as plain Python lists and dictionaries so that a
second-year student can read it, edit it and add new topics without knowing any
database language.

Structure
---------
CATEGORIES : the 20 broad branches of law shown on the home page
TOPICS     : detailed legal topics, each linked to a category
DOCUMENTS  : ready-to-use legal document / agreement templates
GLOSSARY   : an A-to-Z dictionary of legal words
EMERGENCY  : "what do I do right now" quick-help cards

Disclaimer
----------
This is an academic project. The content is simplified for learning and is NOT
legal advice. Always consult a qualified advocate for a real matter.
"""

# ---------------------------------------------------------------------------
# 1. CATEGORIES - the 20 branches of law
# ---------------------------------------------------------------------------

CATEGORIES = [
    {
        "id": "constitutional",
        "name": "Constitutional Law & Fundamental Rights",
        "icon": "⚖️",
        "tagline": "The supreme law - your basic rights and the structure of the State",
        "description": (
            "Constitutional law studies the Constitution of India, 1950 - the document "
            "from which every other law takes its power. It defines Fundamental Rights, "
            "Directive Principles, the powers of Parliament, State Legislatures, the "
            "Executive and the Judiciary, and it decides what happens when two laws clash."
        ),
    },
    {
        "id": "criminal",
        "name": "Criminal Law & Procedure",
        "icon": "\U0001f6a8",
        "tagline": "Offences, FIR, arrest, bail, trial and punishment",
        "description": (
            "Criminal law defines acts that are offences against the State and society and "
            "prescribes punishment. From 1 July 2024 India replaced the old IPC, CrPC and "
            "Evidence Act with the Bharatiya Nyaya Sanhita, the Bharatiya Nagarik Suraksha "
            "Sanhita and the Bharatiya Sakshya Adhiniyam."
        ),
    },
    {
        "id": "civil",
        "name": "Civil Law, Torts & Litigation",
        "icon": "\U0001f3db️",
        "tagline": "Disputes between private parties - money, property, negligence, defamation",
        "description": (
            "Civil law deals with private wrongs where the remedy is compensation or an "
            "order of the court rather than jail. It covers the law of torts (negligence, "
            "nuisance, defamation), civil procedure, limitation, and the different kinds of "
            "relief a court can grant."
        ),
    },
    {
        "id": "corporate",
        "name": "Corporate & Company Law",
        "icon": "\U0001f3e2",
        "tagline": "Incorporation, directors, shares, compliance and governance",
        "description": (
            "Company law governs the birth, life and death of companies - how they are "
            "registered, who runs them, what they must disclose, how shareholders are "
            "protected, and what happens on merger, oppression or winding up."
        ),
    },
    {
        "id": "contract",
        "name": "Contracts & Commercial Law",
        "icon": "\U0001f4dc",
        "tagline": "Agreements, breach, damages, sale of goods and arbitration",
        "description": (
            "Almost every business relationship is a contract. This branch explains when a "
            "promise becomes legally enforceable, what makes an agreement void, what "
            "happens on breach, and how commercial disputes are settled through arbitration "
            "and mediation instead of court."
        ),
    },
    {
        "id": "labour",
        "name": "Labour & Employment Law",
        "icon": "\U0001f477",
        "tagline": "Wages, working hours, PF, gratuity, termination and workplace safety",
        "description": (
            "Labour law balances the employer's need to run a business with the worker's "
            "right to fair wages, safe conditions and social security. India has "
            "consolidated 29 older labour laws into 4 Labour Codes."
        ),
    },
    {
        "id": "ipr",
        "name": "Intellectual Property Rights",
        "icon": "\U0001f4a1",
        "tagline": "Patents, copyright, trademarks, designs and trade secrets",
        "description": (
            "IPR protects creations of the mind. It gives the creator a limited monopoly so "
            "that innovation and creativity are rewarded, while eventually returning the "
            "knowledge to the public domain."
        ),
    },
    {
        "id": "cyber",
        "name": "Cyber Law & Information Technology",
        "icon": "\U0001f5a5️",
        "tagline": "Online fraud, hacking, data privacy, social media and e-evidence",
        "description": (
            "Cyber law applies legal rules to the internet - electronic contracts, digital "
            "signatures, cybercrime, the liability of platforms as intermediaries, and the "
            "new Digital Personal Data Protection Act, 2023."
        ),
    },
    {
        "id": "family",
        "name": "Family & Personal Law",
        "icon": "\U0001f46a",
        "tagline": "Marriage, divorce, maintenance, custody, adoption and succession",
        "description": (
            "Family law in India is personal-law based: Hindus, Muslims, Christians, Parsis "
            "and inter-faith couples are each governed by different statutes on marriage, "
            "divorce, adoption and inheritance."
        ),
    },
    {
        "id": "property",
        "name": "Property & Real Estate Law",
        "icon": "\U0001f3e0",
        "tagline": "Sale deeds, registration, tenancy, RERA and land records",
        "description": (
            "Property law decides who owns land, how ownership is transferred, what a buyer "
            "must verify before paying, the rights of landlords and tenants, and how "
            "homebuyers are protected against builder delay under RERA."
        ),
    },
    {
        "id": "infrastructure",
        "name": "Infrastructure, Construction & Public Procurement",
        "icon": "\U0001f3d7️",
        "tagline": "Tenders, EPC contracts, PPP projects, land acquisition and delay claims",
        "description": (
            "Roads, metros, power plants and smart cities are built through huge public "
            "contracts. This branch covers government tendering, EPC and PPP models, "
            "performance guarantees, delay and price-escalation claims, and the law of land "
            "acquisition and rehabilitation."
        ),
    },
    {
        "id": "environment",
        "name": "Environmental Law",
        "icon": "\U0001f333",
        "tagline": "Pollution control, EIA clearance, forests, wildlife and climate duties",
        "description": (
            "Environmental law forces development to be sustainable. It works through "
            "permissions (consent to establish and operate, environmental clearance), "
            "prohibitions, and principles such as Polluter Pays and the Precautionary "
            "Principle, enforced by the National Green Tribunal."
        ),
    },
    {
        "id": "consumer",
        "name": "Consumer Protection Law",
        "icon": "\U0001f6d2",
        "tagline": "Defective goods, poor service, refunds, e-commerce and misleading ads",
        "description": (
            "Consumer law gives an ordinary buyer a cheap and fast forum to fight a "
            "company. The Consumer Protection Act, 2019 added e-commerce rules, product "
            "liability and punishment for misleading advertisements."
        ),
    },
    {
        "id": "taxation",
        "name": "Taxation & GST",
        "icon": "\U0001f4b0",
        "tagline": "Income tax, GST, TDS, returns, notices and appeals",
        "description": (
            "Tax law is how the State raises revenue. It covers direct tax (income tax on "
            "persons and companies) and indirect tax (GST on the supply of goods and "
            "services), plus the procedure for returns, assessment, penalty and appeal."
        ),
    },
    {
        "id": "banking",
        "name": "Banking, Finance & Insolvency",
        "icon": "\U0001f3e6",
        "tagline": "Loans, cheque bounce, recovery, NPAs and the IBC",
        "description": (
            "This branch covers the borrower-lender relationship: loan agreements and "
            "security, what a bank can and cannot do to recover money, cheque dishonour "
            "cases, and the Insolvency and Bankruptcy Code process when a company cannot pay."
        ),
    },
    {
        "id": "motor",
        "name": "Motor Vehicles & Accident Claims",
        "icon": "\U0001f697",
        "tagline": "Licences, challans, insurance, hit-and-run and compensation",
        "description": (
            "The Motor Vehicles Act regulates driving and, importantly, provides "
            "compensation to accident victims through the Motor Accident Claims Tribunal "
            "and compulsory third-party insurance."
        ),
    },
    {
        "id": "humanrights",
        "name": "Human Rights & International Law",
        "icon": "\U0001f30d",
        "tagline": "UDHR, UN treaties, refugees, war crimes and global legal systems",
        "description": (
            "International law governs relations between States and protects individuals "
            "everywhere. It includes the Universal Declaration of Human Rights, the UN "
            "Charter, humanitarian law, refugee law, and the International Court of Justice "
            "and International Criminal Court."
        ),
    },
    {
        "id": "startup",
        "name": "Startup, MSME & Business Compliance",
        "icon": "\U0001f680",
        "tagline": "Registration, licences, founders agreements, funding and annual filings",
        "description": (
            "A practical checklist branch: which entity to choose, which registrations and "
            "licences a new business needs, how founders should split equity, how funding "
            "documents work, and the recurring compliance calendar."
        ),
    },
    {
        "id": "medical",
        "name": "Medical, Health & Bioethics Law",
        "icon": "\U0001fa7a",
        "tagline": "Negligence, consent, clinical trials, organ donation and mental health",
        "description": (
            "Health law covers the doctor-patient relationship, informed consent, medical "
            "negligence claims, regulation of hospitals and drugs, and difficult ethical "
            "areas such as surrogacy, organ transplantation and end-of-life care."
        ),
    },
    {
        "id": "education",
        "name": "Education & Student Law",
        "icon": "\U0001f393",
        "tagline": "Right to Education, admissions, ragging, scholarships and university rules",
        "description": (
            "Education law covers the fundamental right to free education, reservation and "
            "admission rules, regulation of universities by UGC and AICTE, anti-ragging law, "
            "and the remedies available to a student against an institution."
        ),
    },
]


# ---------------------------------------------------------------------------
# 2. PULL THE REST OF THE KNOWLEDGE BASE TOGETHER
# ---------------------------------------------------------------------------
# The topics, documents, glossary and emergency cards live in their own files so
# that no single file becomes too long to edit comfortably. This module joins
# them, so the rest of the project only ever has to import from legal_data.

from legal_topics import TOPICS_PART1
from legal_topics_extra import TOPICS_PART2
from legal_documents import DOCUMENTS
from legal_extras import GLOSSARY, EMERGENCY, HELPLINES

TOPICS = TOPICS_PART1 + TOPICS_PART2


# ---------------------------------------------------------------------------
# 3. SMALL HELPER FUNCTIONS USED BY app.py AND chatbot.py
# ---------------------------------------------------------------------------

def get_category(category_id):
    """Return one category dictionary, or None if the id does not exist."""
    for category in CATEGORIES:
        if category["id"] == category_id:
            return category
    return None


def get_topic(topic_id):
    """Return one topic dictionary, or None."""
    for topic in TOPICS:
        if topic["id"] == topic_id:
            return topic
    return None


def get_document(document_id):
    """Return one document template dictionary, or None."""
    for document in DOCUMENTS:
        if document["id"] == document_id:
            return document
    return None


def topics_in_category(category_id):
    """Return every topic belonging to one category."""
    return [topic for topic in TOPICS if topic["category"] == category_id]


def documents_in_category(category_id):
    """Return every document template belonging to one category."""
    return [doc for doc in DOCUMENTS if doc["category"] == category_id]


def category_name(category_id):
    """Return the display name of a category id, falling back to the id."""
    category = get_category(category_id)
    return category["name"] if category else category_id


def get_emergency(emergency_id):
    """Return one emergency quick-help card, or None."""
    for card in EMERGENCY:
        if card["id"] == emergency_id:
            return card
    return None


def stats():
    """Counts shown on the home page."""
    return {
        "categories": len(CATEGORIES),
        "topics": len(TOPICS),
        "documents": len(DOCUMENTS),
        "glossary": len(GLOSSARY),
        "faqs": sum(len(topic.get("faqs", [])) for topic in TOPICS),
    }


if __name__ == "__main__":
    # Running "python legal_data.py" prints a quick summary of the knowledge
    # base. Useful while adding new content.
    summary = stats()
    print("LegalMitra knowledge base")
    print("-" * 40)
    for key, value in summary.items():
        print("{:<12} : {}".format(key, value))
    print("-" * 40)
    for category in CATEGORIES:
        print("{:<18} {:>2} topics  {:>2} documents  {}".format(
            category["id"],
            len(topics_in_category(category["id"])),
            len(documents_in_category(category["id"])),
            category["name"],
        ))

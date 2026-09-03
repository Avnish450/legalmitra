# -*- coding: utf-8 -*-
"""
legal_topics.py
===============
PART 1 of the topic knowledge base: the first ten branches of law
(constitutional, criminal, civil, corporate, contract, labour, ipr, cyber,
family, property).

Every topic is a dictionary with the same seven keys, so the website templates
and the chatbot can loop over them without any special cases:

    id         unique slug used in the URL  ->  /topic/fundamental-rights
    category   the CATEGORIES id it belongs to
    title      heading shown on the page
    summary    2-4 sentence plain-English explanation
    key_points list of the most important rules
    laws       the Acts / Articles / Sections that apply
    steps      "what to actually do" - shown as a numbered procedure
    faqs       list of {"q": question, "a": answer}
    keywords   extra search words that help the chatbot match this topic

Adding a new topic = copying one block and editing the text. Nothing else in
the project has to change.
"""

TOPICS_PART1 = [

    # ==================================================================
    # CONSTITUTIONAL LAW
    # ==================================================================
    {
        "id": "fundamental-rights",
        "category": "constitutional",
        "title": "Fundamental Rights (Articles 12-35)",
        "summary": (
            "Fundamental Rights are the basic freedoms guaranteed to every person by Part III "
            "of the Constitution. They are enforceable against the State, which means that if "
            "the government or any public authority violates them you can go directly to the "
            "High Court or the Supreme Court. A law that takes away a Fundamental Right can be "
            "declared void by the courts."
        ),
        "key_points": [
            "Article 14 - Equality before the law and equal protection of the laws.",
            "Article 15 - No discrimination on grounds of religion, race, caste, sex or place of birth.",
            "Article 19 - Six freedoms including speech and expression, assembly, association, movement, residence and profession, each subject to reasonable restrictions.",
            "Article 21 - Right to life and personal liberty; read widely by courts to include privacy, clean environment, livelihood, health, shelter and a speedy trial.",
            "Article 21A - Free and compulsory education for children aged 6 to 14.",
            "Articles 23-24 - Prohibition of human trafficking, forced labour and child labour in hazardous work.",
            "Article 32 - The right to move the Supreme Court itself for enforcement; Dr Ambedkar called it the 'heart and soul' of the Constitution.",
        ],
        "laws": [
            "Constitution of India, 1950 - Part III, Articles 12 to 35",
            "Article 32 - Supreme Court writ jurisdiction",
            "Article 226 - High Court writ jurisdiction (wider than Article 32)",
            "Kesavananda Bharati v. State of Kerala (1973) - Basic Structure doctrine",
            "K.S. Puttaswamy v. Union of India (2017) - privacy is a Fundamental Right",
        ],
        "steps": [
            "Identify exactly which right has been violated and by whom - it must be the State or a public authority.",
            "Collect documentary proof: orders, notices, letters, photographs, RTI replies.",
            "Send a representation to the authority first; courts prefer that you exhausted the ordinary remedy.",
            "Draft a writ petition asking for one of the five writs: Habeas Corpus, Mandamus, Prohibition, Certiorari or Quo Warranto.",
            "File under Article 226 in the High Court, or Article 32 in the Supreme Court where the violation is grave and of national importance.",
            "If you cannot afford a lawyer, apply for free legal aid to the District/State Legal Services Authority.",
        ],
        "faqs": [
            {
                "q": "Can Fundamental Rights be suspended?",
                "a": "During a National Emergency the enforcement of some rights under Article 19 can be suspended, but Articles 20 and 21 can never be suspended after the 44th Constitutional Amendment.",
            },
            {
                "q": "Are Fundamental Rights available against a private company?",
                "a": "Generally no - they apply against the State. But some rights, like Article 17 (untouchability), Article 23 (trafficking and forced labour) and Article 24 (child labour), operate against private persons as well.",
            },
            {
                "q": "What is the difference between a Fundamental Right and a Directive Principle?",
                "a": "A Fundamental Right is enforceable in court. A Directive Principle (Part IV) is a goal for the government to work towards and cannot by itself be enforced, though courts use it to interpret rights.",
            },
        ],
        "keywords": ["fundamental rights", "article 21", "article 14", "writ", "habeas corpus", "constitution", "equality", "freedom of speech", "right to life", "part iii"],
    },
    {
        "id": "writ-petitions",
        "category": "constitutional",
        "title": "Writ Petitions and Public Interest Litigation (PIL)",
        "summary": (
            "A writ is a direct order from a constitutional court to a government authority. "
            "A Public Interest Litigation is a relaxed form of writ petition where any public "
            "spirited person - not just the victim - can approach the court on behalf of people "
            "who cannot come themselves. PIL is the reason India has judgments on pollution, "
            "prison reform, and mid-day meals."
        ),
        "key_points": [
            "Habeas Corpus - 'produce the body'; used when a person is illegally detained.",
            "Mandamus - 'we command'; orders a public authority to perform a duty it is refusing to perform.",
            "Prohibition - stops a lower court or tribunal from exceeding its jurisdiction.",
            "Certiorari - quashes an order already passed without jurisdiction or against natural justice.",
            "Quo Warranto - questions a person's authority to hold a public office.",
            "In a PIL the traditional rule of locus standi is relaxed - even a letter or a newspaper report has been treated as a petition.",
            "Courts dismiss and even fine 'publicity interest' or 'private interest' litigation disguised as PIL.",
        ],
        "laws": [
            "Article 32 and Article 226 of the Constitution",
            "Supreme Court Rules, 2013",
            "Hussainara Khatoon v. State of Bihar (1979) - speedy trial, first major PIL",
            "S.P. Gupta v. Union of India (1981) - relaxed locus standi",
        ],
        "steps": [
            "Check whether the grievance affects the public at large or only you - that decides PIL versus ordinary writ.",
            "Gather documents: government orders, RTI replies, photographs, news reports, expert reports.",
            "Give a written representation to the concerned authority and wait a reasonable time for a reply.",
            "Draft the petition: facts, the legal right violated, the reliefs prayed for, and an affidavit verifying the facts.",
            "File in the High Court (Article 226) with the prescribed court fee, or in the Supreme Court (Article 32).",
            "Appear on the admission date; if admitted, the court issues notice to the respondents.",
        ],
        "faqs": [
            {
                "q": "How much does a PIL cost?",
                "a": "Court fees are nominal - often a few hundred rupees. The real cost is the advocate's fee, which is why many PILs are filed by NGOs or argued by the petitioner in person.",
            },
            {
                "q": "Can a student file a PIL?",
                "a": "Yes. Any citizen acting in good faith for a genuine public cause can file one, provided the issue is real and the petitioner has no hidden personal motive.",
            },
        ],
        "keywords": ["writ", "pil", "public interest litigation", "mandamus", "habeas corpus", "certiorari", "quo warranto", "high court", "supreme court", "article 226"],
    },
    {
        "id": "rti-act",
        "category": "constitutional",
        "title": "Right to Information (RTI)",
        "summary": (
            "The RTI Act, 2005 turns the citizen's right to know into a working procedure. Any "
            "citizen can ask a public authority for information held by it, and the officer must "
            "reply within 30 days. It is the single most powerful and cheapest legal tool an "
            "ordinary person has against government inaction."
        ),
        "key_points": [
            "Applies to all public authorities - central, state, local bodies, and bodies substantially financed by the government.",
            "Fee is normally Rs 10 for the application; people below the poverty line pay nothing.",
            "Reply must come within 30 days; within 48 hours if it concerns the life or liberty of a person.",
            "You do not have to give a reason for wanting the information.",
            "Section 8 lists exemptions - national security, cabinet papers before a decision, personal information with no public interest, information held in a fiduciary capacity.",
            "If the reply is refused or delayed, a First Appeal goes to the senior officer within 30 days, and a Second Appeal to the Information Commission within 90 days.",
            "The Information Commission can impose a penalty of Rs 250 per day, up to Rs 25,000, on the officer who withheld information.",
        ],
        "laws": [
            "Right to Information Act, 2005",
            "Section 6 - request for information; Section 7 - time limits",
            "Section 8 and 9 - exemptions; Section 19 - appeals; Section 20 - penalty",
        ],
        "steps": [
            "Identify the correct public authority and its Public Information Officer (PIO).",
            "Write the application in simple language on plain paper or the online RTI portal.",
            "Ask specific, factual questions - 'give a copy of file notings on X' works better than 'why did you do X'.",
            "Pay Rs 10 by IPO, court fee stamp, demand draft or online payment.",
            "Keep the receipt or online registration number and wait 30 days.",
            "On refusal or silence, file the First Appeal, then the Second Appeal with a complaint for penalty.",
        ],
        "faqs": [
            {
                "q": "Can I file an RTI online?",
                "a": "Yes, for central government departments through the official RTI online portal. Many states have their own portals; some still require a physical application.",
            },
            {
                "q": "Can RTI be used against a private company?",
                "a": "Not directly. But you can ask the regulator that supervises that company for records it holds, which often reveals the same information.",
            },
        ],
        "keywords": ["rti", "right to information", "information", "pio", "appeal", "transparency", "government records", "2005"],
    },
    {
        "id": "separation-of-powers",
        "category": "constitutional",
        "title": "Structure of Government and Separation of Powers",
        "summary": (
            "The Constitution divides power in two directions: horizontally between the "
            "Legislature, the Executive and the Judiciary, and vertically between the Union and "
            "the States. Understanding this map tells you which authority makes a rule, which "
            "one enforces it, and which one can strike it down."
        ),
        "key_points": [
            "Legislature (Parliament and State Legislatures) makes law; the Executive (President, PM, Council of Ministers, bureaucracy) implements it; the Judiciary interprets it.",
            "The Seventh Schedule has three lists - Union List (defence, foreign affairs, banking), State List (police, public health, land) and Concurrent List (education, forests, criminal law).",
            "If a Union law and a State law on a Concurrent List subject clash, the Union law prevails under Article 254.",
            "Judicial review lets courts strike down a law that violates the Constitution.",
            "The Basic Structure doctrine means Parliament can amend the Constitution but cannot destroy its essential features.",
            "Article 50 directs the separation of the judiciary from the executive in public services.",
        ],
        "laws": [
            "Constitution of India - Articles 52-151 (Union), 152-237 (States), 245-255 (legislative relations)",
            "Seventh Schedule - Union, State and Concurrent Lists",
            "Kesavananda Bharati v. State of Kerala (1973)",
            "Minerva Mills v. Union of India (1980)",
        ],
        "steps": [
            "Work out the subject matter of your problem - is it police, land, education, taxation?",
            "Find which List of the Seventh Schedule that subject falls in.",
            "That tells you whether the relevant law is a Central Act, a State Act, or both.",
            "Identify the department or regulator that administers it - this is who you write to.",
            "If the authority has acted beyond its power, that is 'ultra vires' and can be challenged by writ.",
        ],
        "faqs": [
            {
                "q": "Who is more powerful, Parliament or the Supreme Court?",
                "a": "Neither is absolute. Parliament makes and amends law; the Supreme Court can strike down a law or an amendment that violates the Basic Structure. They check each other.",
            },
        ],
        "keywords": ["separation of powers", "seventh schedule", "union list", "state list", "concurrent list", "federalism", "judicial review", "basic structure", "parliament"],
    },

    # ==================================================================
    # CRIMINAL LAW
    # ==================================================================
    {
        "id": "fir-filing",
        "category": "criminal",
        "title": "How to File an FIR (First Information Report)",
        "summary": (
            "An FIR is the first written record of a cognizable offence and it sets the criminal "
            "law in motion. The police cannot refuse to register an FIR for a cognizable offence, "
            "and you are entitled to a free copy of it. If the police still refuse, the law gives "
            "you three escalation routes."
        ),
        "key_points": [
            "Cognizable offence - serious offence such as theft, assault, rape, murder; police can arrest without a warrant and must register an FIR.",
            "Non-cognizable offence - minor offence; police only record an NCR and need a magistrate's order to investigate.",
            "The FIR must be read back to you and you must sign it; you get a free copy immediately.",
            "Zero FIR - any police station must register the FIR even if the offence happened outside its area, and then transfer it to the correct station.",
            "e-FIR / online FIR is now available in most states for property offences and cybercrime.",
            "Delay in filing is not fatal but must be explained, especially in sexual offence cases where courts accept delay as normal.",
            "Filing a knowingly false FIR is itself an offence.",
        ],
        "laws": [
            "Bharatiya Nagarik Suraksha Sanhita, 2023 (replaced CrPC from 1 July 2024) - Section 173 (information in cognizable cases), Section 175 (magistrate's power to order investigation)",
            "Bharatiya Nyaya Sanhita, 2023 (replaced IPC)",
            "Lalita Kumari v. Government of Uttar Pradesh (2013) - registration of FIR is mandatory for a cognizable offence",
        ],
        "steps": [
            "Go to the nearest police station; you may go to any station under the Zero FIR rule.",
            "Narrate the incident - what happened, when, where, who was involved, what was lost or injured.",
            "Read the written FIR carefully before signing; insist that your words are recorded correctly.",
            "Collect the free copy along with the FIR number and the date.",
            "If the SHO refuses, send a written complaint by registered post to the Superintendent of Police.",
            "If that also fails, file a complaint before the Judicial Magistrate, who can direct the police to register and investigate.",
        ],
        "faqs": [
            {
                "q": "Can a woman be called to the police station at night to record a statement?",
                "a": "No. A woman's statement should be recorded at her residence or a place of her choice, in the presence of a family member or a woman officer, and she cannot be summoned to the station outside prescribed hours.",
            },
            {
                "q": "What if I want to withdraw the FIR?",
                "a": "An FIR cannot simply be withdrawn by you. In compoundable offences the parties can compromise before the court; in non-compoundable offences only the High Court can quash the FIR.",
            },
        ],
        "keywords": ["fir", "police complaint", "cognizable", "zero fir", "first information report", "police station", "crime report", "ncr", "lalita kumari"],
    },
    {
        "id": "arrest-and-bail",
        "category": "criminal",
        "title": "Rights on Arrest, and How Bail Works",
        "summary": (
            "Arrest is the most drastic power the State has over a person, so the law surrounds "
            "it with safeguards. Bail is the rule and jail the exception. Knowing your rights at "
            "the moment of arrest - and the three types of bail - is the most practically useful "
            "criminal-law knowledge a citizen can have."
        ),
        "key_points": [
            "You must be told the grounds of arrest, and a relative or friend of your choice must be informed.",
            "You must be produced before a magistrate within 24 hours, excluding travel time.",
            "You have the right to consult and be defended by a lawyer of your choice, and to free legal aid if you cannot afford one.",
            "A woman cannot normally be arrested after sunset and before sunrise, and only a woman officer may arrest her.",
            "Article 20(3) - you cannot be compelled to be a witness against yourself.",
            "Regular bail is applied for after arrest; anticipatory bail before arrest when you fear it; interim bail is a short protection until the main application is heard.",
            "Bailable offence - bail is a matter of right at the police station itself. Non-bailable - bail is at the court's discretion.",
            "Default bail: if the police do not file the chargesheet within 60 or 90 days depending on the offence, you become entitled to bail as a right.",
        ],
        "laws": [
            "Bharatiya Nagarik Suraksha Sanhita, 2023 - arrest, bail and default bail provisions (Sections 35, 47, 58, 187, 478-482)",
            "Constitution - Articles 20, 21 and 22",
            "D.K. Basu v. State of West Bengal (1997) - mandatory arrest guidelines",
            "Arnesh Kumar v. State of Bihar (2014) - no automatic arrest in offences punishable up to 7 years",
        ],
        "steps": [
            "Stay calm and do not resist; resisting is a separate offence.",
            "Ask the officer for their name and identification, and ask to see the arrest memo.",
            "Ensure the arrest memo is signed by a witness - a family member or a respectable local person - and countersigned by you.",
            "Insist that your family is informed and note the time of arrest.",
            "Ask for a medical examination if you are injured; you have the right to one every 48 hours in custody.",
            "Engage a lawyer or ask the magistrate for legal aid, and file a bail application on the first hearing.",
        ],
        "faqs": [
            {
                "q": "What is anticipatory bail?",
                "a": "It is an order from the Sessions Court or High Court, obtained before arrest, directing that if you are arrested you shall be released on bail. It is used when a person apprehends arrest in a false or exaggerated case.",
            },
            {
                "q": "Can police detain me without arrest for questioning?",
                "a": "They may call you for questioning by written notice, and you must attend. But detention beyond that without formal arrest is illegal and can be challenged by habeas corpus.",
            },
        ],
        "keywords": ["arrest", "bail", "anticipatory bail", "custody", "police", "rights on arrest", "dk basu", "arnesh kumar", "default bail", "remand"],
    },
    {
        "id": "cheque-bounce",
        "category": "criminal",
        "title": "Cheque Bounce - Section 138 Negotiable Instruments Act",
        "summary": (
            "When a cheque is returned unpaid for insufficient funds or because the account is "
            "closed, the drawer commits a criminal offence, provided a strict timeline is "
            "followed. This is one of the most commonly filed cases in India, and missing a "
            "deadline by even one day destroys the case."
        ),
        "key_points": [
            "The cheque must have been issued to discharge a legally enforceable debt or liability - not as a gift or security for an illegal transaction.",
            "The cheque must be presented within its validity period, which is three months.",
            "A written demand notice must be sent within 30 days of receiving the bank's return memo.",
            "The drawer gets 15 days from receiving the notice to pay.",
            "If he does not pay, the complaint must be filed in court within the next 30 days.",
            "Punishment can extend to two years imprisonment, or a fine up to twice the cheque amount, or both.",
            "The court may order interim compensation of up to 20 per cent of the cheque amount even during the trial.",
        ],
        "laws": [
            "Negotiable Instruments Act, 1881 - Sections 138, 139, 142, 143A and 148",
            "Section 139 - presumption that the cheque was issued for a debt (burden shifts to the accused)",
            "Dashrath Rupsingh Rathod and later amendments - jurisdiction is where the payee's bank branch is located",
        ],
        "steps": [
            "Collect the original cheque and the bank return memo stating the reason for dishonour.",
            "Within 30 days of the memo, send a legal demand notice by registered post with acknowledgement due and by email.",
            "Preserve the postal receipt and the tracking printout - this proves service.",
            "Wait 15 days from the date the notice is served.",
            "If unpaid, file a complaint before the Judicial Magistrate within the next 30 days, attaching the cheque, memo, notice and postal proof.",
            "Attend hearings; you may also apply for interim compensation under Section 143A.",
        ],
        "faqs": [
            {
                "q": "What if the notice comes back undelivered?",
                "a": "If it was sent to the correct address and returned as 'refused' or 'not claimed', the law treats it as served. Keep the returned envelope unopened as evidence.",
            },
            {
                "q": "Can I also recover the money separately?",
                "a": "Yes. The Section 138 case is criminal; you may additionally file a civil summary suit under Order 37 CPC to recover the amount, or seek compensation in the criminal case itself.",
            },
        ],
        "keywords": ["cheque bounce", "section 138", "negotiable instruments", "dishonour", "demand notice", "cheque return", "insufficient funds", "138 ni act"],
    },
    {
        "id": "women-safety-laws",
        "category": "criminal",
        "title": "Laws Protecting Women - Harassment, Domestic Violence and POSH",
        "summary": (
            "Several separate laws protect women in different settings: the criminal law for "
            "offences like assault and stalking, a civil law for violence inside the home, and a "
            "workplace law that makes every employer set up an internal committee. Choosing the "
            "right law for the right setting is half the battle."
        ),
        "key_points": [
            "Sexual harassment at the workplace - every employer with 10 or more employees must constitute an Internal Committee (IC) headed by a senior woman.",
            "The IC must complete its inquiry within 90 days and the employer must act within 60 days of the report.",
            "Domestic violence includes physical, sexual, verbal, emotional and economic abuse; the remedy is a civil protection order from the magistrate.",
            "A woman in a domestic relationship has the right to reside in the shared household even if she does not own it.",
            "Stalking, voyeurism, acid attack, and outraging modesty are separate criminal offences.",
            "Dowry demand before, during or after marriage is an offence, and dowry death carries a minimum of seven years.",
            "The identity of a survivor of a sexual offence cannot be published - doing so is itself an offence.",
        ],
        "laws": [
            "Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 - the POSH Act",
            "Protection of Women from Domestic Violence Act, 2005",
            "Dowry Prohibition Act, 1961",
            "Bharatiya Nyaya Sanhita, 2023 - offences against women",
            "Vishaka v. State of Rajasthan (1997) - the guidelines that led to the POSH Act",
        ],
        "steps": [
            "Workplace harassment: write a complaint to the Internal Committee within three months of the incident (extendable).",
            "If the employer has no IC, complain to the Local Committee at the district level.",
            "Domestic violence: approach a Protection Officer, a service provider NGO, the police, or the magistrate directly.",
            "Ask for the specific orders you need - protection order, residence order, monetary relief, custody order, compensation.",
            "For criminal offences, file an FIR; the statement of a survivor of a sexual offence must be recorded by a woman officer.",
            "Call 181 (women's helpline) or 112 (emergency) for immediate assistance.",
        ],
        "faqs": [
            {
                "q": "Can a woman file a domestic violence case against her in-laws?",
                "a": "Yes. The Act covers any adult male respondent in a domestic relationship, and courts have allowed female relatives of the husband to be made respondents as well.",
            },
            {
                "q": "Is a POSH complaint confidential?",
                "a": "Yes. The Act prohibits publication of the identity of the complainant, the respondent, the witnesses or the contents of the inquiry, with a penalty for breach.",
            },
        ],
        "keywords": ["posh", "sexual harassment", "domestic violence", "women", "dowry", "internal committee", "protection order", "498a", "vishaka", "workplace harassment"],
    },

    # ==================================================================
    # CIVIL LAW AND TORTS
    # ==================================================================
    {
        "id": "civil-suit-procedure",
        "category": "civil",
        "title": "How a Civil Suit Works - From Plaint to Decree",
        "summary": (
            "A civil suit is how you enforce a private right: recovery of money, possession of "
            "property, a declaration of title, or an injunction to stop someone. The Code of "
            "Civil Procedure, 1908 lays down every stage, and knowing the sequence removes most "
            "of the mystery from litigation."
        ),
        "key_points": [
            "The document that starts a suit is called a plaint; the defendant's reply is the written statement, due within 30 days (extendable to 90 or 120).",
            "Court fee is usually a percentage of the amount or value claimed, so the valuation matters.",
            "Jurisdiction has three parts - pecuniary (value), territorial (place) and subject-matter.",
            "Issues are framed by the judge from the pleadings; then evidence is led by affidavit and witnesses are cross-examined.",
            "Interim relief - a temporary injunction under Order 39 - can be obtained on the first day if there is a prima facie case, balance of convenience and irreparable injury.",
            "The final decision is a judgment followed by a decree, which then has to be enforced through execution proceedings.",
            "Commercial disputes above the specified value require pre-institution mediation before the suit can be filed.",
        ],
        "laws": [
            "Code of Civil Procedure, 1908 - Order 4 (institution), Order 7 (plaint), Order 8 (written statement), Order 26 (commissions), Order 39 (injunctions), Order 21 (execution)",
            "Specific Relief Act, 1963 - injunctions and specific performance",
            "Limitation Act, 1963",
            "Commercial Courts Act, 2015",
        ],
        "steps": [
            "Send a legal notice first - it is compulsory against the government under Section 80 CPC and useful otherwise.",
            "Choose the correct court based on the value of the claim and the place of cause of action.",
            "Draft the plaint with a clear cause of action, the relief sought, the valuation and a verification affidavit.",
            "Pay the court fee and file, along with a list of documents relied on.",
            "Apply for interim injunction along with the plaint if you need immediate protection.",
            "Attend hearings for service of summons, framing of issues, evidence, arguments and judgment.",
            "After the decree, file an execution petition to actually recover the money or possession.",
        ],
        "faqs": [
            {
                "q": "How long does a civil suit take?",
                "a": "Realistically two to five years at the trial court level, longer with appeals. Summary suits under Order 37 for money claims on written contracts are much faster.",
            },
            {
                "q": "What is the difference between a suit and a petition?",
                "a": "A suit is a regular civil proceeding with full trial. A petition is a shorter proceeding under a specific statute or the Constitution, usually decided on affidavits.",
            },
        ],
        "keywords": ["civil suit", "plaint", "cpc", "written statement", "injunction", "decree", "execution", "civil case", "order 39", "summons"],
    },
    {
        "id": "law-of-torts",
        "category": "civil",
        "title": "Law of Torts - Negligence, Nuisance and Defamation",
        "summary": (
            "A tort is a civil wrong, other than breach of contract, for which the remedy is "
            "unliquidated damages. Most of the law of torts in India is judge-made, borrowed "
            "from English common law and adapted. It is the branch that answers 'someone harmed "
            "me carelessly - can I claim compensation?'"
        ),
        "key_points": [
            "Negligence has four ingredients: a duty of care, breach of that duty, causation, and resulting damage.",
            "Res ipsa loquitur - 'the thing speaks for itself'; where the accident could not have happened without negligence, the burden shifts to the defendant.",
            "Nuisance is unreasonable interference with the use or enjoyment of land - noise, smell, smoke, encroachment.",
            "Defamation requires a false statement, published to a third person, that lowers reputation; truth and fair comment are defences.",
            "Vicarious liability makes an employer liable for a tort committed by an employee in the course of employment.",
            "Strict liability (Rylands v. Fletcher) and India's stricter absolute liability rule (M.C. Mehta) apply to hazardous activities.",
            "Contributory negligence reduces compensation in proportion to the victim's own carelessness.",
        ],
        "laws": [
            "Largely uncodified common law applied by Indian courts",
            "Donoghue v. Stevenson (1932) - the neighbour principle",
            "M.C. Mehta v. Union of India (1987) - absolute liability, Oleum gas leak",
            "Consumer Protection Act, 2019 - a statutory, faster route for many negligence claims",
        ],
        "steps": [
            "Establish that the defendant owed you a duty of care in the circumstances.",
            "Collect proof of the breach: photographs, medical records, bills, expert opinion, witness statements.",
            "Quantify your loss - medical expenses, lost income, repair cost, and a reasonable figure for pain and suffering.",
            "Send a legal notice claiming compensation with a deadline to pay.",
            "File a civil suit for damages, or a consumer complaint if the relationship was that of consumer and service provider.",
            "Watch the limitation period - usually one year for defamation and three years for most other torts.",
        ],
        "faqs": [
            {
                "q": "Is defamation criminal or civil?",
                "a": "It can be both in India. Civil defamation seeks damages; criminal defamation can lead to imprisonment. The same statement may attract both proceedings.",
            },
            {
                "q": "Can I sue a hospital for negligence?",
                "a": "Yes - either as a consumer complaint under the Consumer Protection Act, which is faster and cheaper, or as a civil suit for damages. Expert medical opinion is usually essential.",
            },
        ],
        "keywords": ["tort", "negligence", "nuisance", "defamation", "damages", "duty of care", "vicarious liability", "strict liability", "compensation", "civil wrong"],
    },
    {
        "id": "limitation-periods",
        "category": "civil",
        "title": "Limitation - The Deadline for Filing a Case",
        "summary": (
            "Every legal remedy has an expiry date. The Limitation Act, 1963 fixes how long you "
            "have to approach the court after your right is violated. Miss it and the court will "
            "dismiss the case however strong it is on merits. This is the single most common "
            "reason genuine claims fail."
        ),
        "key_points": [
            "Recovery of money on a contract - 3 years from when the money became due.",
            "Suit for possession of immovable property - 12 years from dispossession.",
            "Compensation for tort or personal injury - generally 1 to 3 years.",
            "Defamation - 1 year from the date of publication.",
            "Appeal to the High Court - usually 90 days; to the District Court - 30 days.",
            "Cheque bounce complaint - 30 days after the 15-day notice period expires.",
            "A written acknowledgement of the debt, or a part payment, restarts the limitation period afresh.",
            "Section 5 allows delay to be condoned in appeals and applications if 'sufficient cause' is shown - but not in ordinary suits.",
        ],
        "laws": [
            "Limitation Act, 1963 - Section 3 (bar), Section 5 (condonation), Section 18 (acknowledgement), and the Schedule of periods",
        ],
        "steps": [
            "Fix the exact date on which your right was violated - this is when the clock starts.",
            "Find the correct Article in the Schedule to the Limitation Act for your type of claim.",
            "Check whether any written acknowledgement or part payment extends the period.",
            "If you are already out of time, look for a legal ground for exclusion - minority, fraud, disability or time spent in a wrong court.",
            "File a delay-condonation application with an affidavit explaining every day of delay.",
        ],
        "faqs": [
            {
                "q": "Does sending a legal notice stop the limitation clock?",
                "a": "No. Only the actual filing of the case stops it. A notice does not extend the period, though a written admission of liability in the reply might.",
            },
        ],
        "keywords": ["limitation", "time limit", "deadline", "limitation act", "delay", "condonation", "3 years", "12 years", "barred by time"],
    },
    {
        "id": "adr-arbitration",
        "category": "civil",
        "title": "Alternative Dispute Resolution - Arbitration, Mediation, Lok Adalat",
        "summary": (
            "Courts are slow and expensive, so the law encourages parties to settle outside. "
            "Arbitration produces a binding award from a private tribunal; mediation and "
            "conciliation produce a negotiated settlement; Lok Adalat gives a free, final "
            "settlement with the force of a decree."
        ),
        "key_points": [
            "Arbitration needs a written arbitration agreement or clause; the award is binding and can be enforced like a court decree.",
            "An arbitral award can be challenged only on narrow grounds under Section 34, such as fraud, lack of jurisdiction or violation of public policy - not because the arbitrator got the facts wrong.",
            "The tribunal should normally make the award within 12 months of completing pleadings, extendable by 6 months.",
            "Mediation is voluntary and confidential; the mediator does not decide, they help the parties decide.",
            "Commercial suits above the specified value require pre-institution mediation unless urgent interim relief is sought.",
            "A Lok Adalat award is final, binding, non-appealable, and the court fee already paid is refunded.",
            "Section 89 CPC lets a court refer a pending case to arbitration, conciliation, mediation or Lok Adalat.",
        ],
        "laws": [
            "Arbitration and Conciliation Act, 1996 (amended 2015, 2019, 2021)",
            "Mediation Act, 2023",
            "Legal Services Authorities Act, 1987 - Lok Adalats",
            "Section 89, Code of Civil Procedure, 1908",
        ],
        "steps": [
            "Read your contract and find the dispute resolution clause - it usually names the seat, the language and the number of arbitrators.",
            "Send a notice invoking arbitration and proposing an arbitrator.",
            "If the other side does not agree, apply to the High Court or Supreme Court under Section 11 for appointment.",
            "Attend the preliminary hearing where the timetable and fees are fixed.",
            "File the statement of claim, defence, evidence and written arguments as scheduled.",
            "After the award, if unpaid, file an execution petition; the loser has 3 months to challenge under Section 34.",
        ],
        "faqs": [
            {
                "q": "Is arbitration cheaper than court?",
                "a": "It is faster, but not always cheaper - arbitrators' fees and venue costs are paid by the parties. For high-value commercial disputes the speed usually justifies it.",
            },
            {
                "q": "Can any dispute be arbitrated?",
                "a": "No. Criminal offences, matrimonial status, insolvency, guardianship and testamentary matters are not arbitrable because they affect rights in rem or public status.",
            },
        ],
        "keywords": ["arbitration", "mediation", "adr", "lok adalat", "conciliation", "arbitral award", "section 34", "settlement", "dispute resolution"],
    },

    # ==================================================================
    # CORPORATE LAW
    # ==================================================================
    {
        "id": "company-incorporation",
        "category": "corporate",
        "title": "Types of Business Entities and How to Incorporate",
        "summary": (
            "Choosing the right legal form is the first business-law decision anyone makes. The "
            "choice decides who is personally liable for debts, how the profits are taxed, how "
            "much compliance you carry, and whether investors can put money in."
        ),
        "key_points": [
            "Sole Proprietorship - simplest and cheapest, but the owner has unlimited personal liability and cannot raise equity.",
            "Partnership Firm - governed by the Indian Partnership Act, 1932; partners have unlimited joint liability; registration is optional but an unregistered firm cannot sue to enforce contracts.",
            "Limited Liability Partnership (LLP) - separate legal person, partners' liability limited, lower compliance than a company, but venture capital rarely invests in an LLP.",
            "One Person Company (OPC) - a private company with a single member and a nominee; good for a solo founder who wants limited liability.",
            "Private Limited Company - 2 to 200 members, minimum 2 directors, limited liability, the standard vehicle for startups because shares can be issued to investors.",
            "Public Limited Company - minimum 7 members and 3 directors, can invite the public to subscribe, heaviest compliance.",
            "Incorporation happens online through the SPICe+ form on the MCA portal, which also gives PAN, TAN, EPFO, ESIC and a bank account in one go.",
        ],
        "laws": [
            "Companies Act, 2013 and the rules made under it",
            "Limited Liability Partnership Act, 2008",
            "Indian Partnership Act, 1932",
            "Companies (Incorporation) Rules, 2014 - SPICe+ procedure",
        ],
        "steps": [
            "Decide the structure based on liability, funding plans and compliance appetite.",
            "Obtain a Digital Signature Certificate (DSC) for each proposed director.",
            "Apply for name reservation through RUN or Part A of SPICe+, keeping two alternatives ready.",
            "Draft the Memorandum of Association (objects) and Articles of Association (internal rules).",
            "File SPICe+ Part B with AGILE-PRO and INC-9, attaching identity, address and office proof.",
            "Receive the Certificate of Incorporation with CIN, PAN and TAN.",
            "Open a current account, deposit the subscription money, and file INC-20A declaration of commencement of business within 180 days.",
        ],
        "faqs": [
            {
                "q": "How much capital do I need to start a private limited company?",
                "a": "There is no minimum paid-up capital requirement any more. Companies are commonly incorporated with Rs 1 lakh or even Rs 10,000 of authorised capital.",
            },
            {
                "q": "Can a student start a company?",
                "a": "Yes, if you are 18 or above and have a PAN and DIN. Two people are needed for a private limited company, or you can form an OPC alone.",
            },
        ],
        "keywords": ["company", "incorporation", "private limited", "llp", "opc", "partnership", "spice", "mca", "registration", "startup entity", "moa", "aoa"],
    },
    {
        "id": "directors-duties",
        "category": "corporate",
        "title": "Directors - Appointment, Duties and Liability",
        "summary": (
            "Directors are the human brains of an artificial person. The Companies Act codified "
            "their duties for the first time in 2013, and a director who ignores them can be "
            "personally liable even though the company has limited liability."
        ),
        "key_points": [
            "Every director needs a Director Identification Number (DIN) and must file KYC annually.",
            "Section 166 duties - act in good faith, in the best interests of the company, with due care and diligence, avoid conflicts of interest, and not make undue gain.",
            "A director must disclose their interest in any contract at the first Board meeting, and must not participate in that discussion.",
            "Independent directors on listed and specified companies must meet strict independence tests and cannot receive stock options.",
            "At least one director must have stayed in India for 182 days or more in the financial year.",
            "A director vacates office automatically on failing to attend all Board meetings for 12 months, or on disqualification under Section 164.",
            "Loans by a company to its directors are heavily restricted under Section 185.",
        ],
        "laws": [
            "Companies Act, 2013 - Sections 149-172 (appointment, duties), 164 (disqualification), 166 (duties), 184 (interest disclosure), 185 (loans)",
            "SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015 for listed companies",
        ],
        "steps": [
            "Obtain DSC and DIN for the proposed director.",
            "Pass a Board resolution and, where required, a shareholders' resolution appointing them.",
            "File form DIR-12 with the Registrar of Companies within 30 days.",
            "Take form DIR-2 consent and DIR-8 disclosure of non-disqualification from the appointee.",
            "Record the disclosure of interest in form MBP-1 at the first Board meeting of each financial year.",
            "For resignation, file DIR-11 by the director and DIR-12 by the company.",
        ],
        "faqs": [
            {
                "q": "Can a director be personally liable for the company's debts?",
                "a": "Normally no, because the company is a separate person. But the corporate veil is lifted for fraud, for statutory dues like tax and PF, for cheque bounce, and where the director gave a personal guarantee.",
            },
        ],
        "keywords": ["director", "din", "board", "duties", "section 166", "disqualification", "dir-12", "corporate governance", "fiduciary"],
    },
    {
        "id": "corporate-compliance",
        "category": "corporate",
        "title": "Annual Compliance Calendar for a Company",
        "summary": (
            "A company is a regulated animal - it must hold meetings, keep registers, get audited "
            "and file returns whether or not it does any business. Most startup penalties come "
            "not from big mistakes but from missed routine filings, which carry a Rs 100 per day "
            "additional fee with no upper limit."
        ),
        "key_points": [
            "At least 4 Board meetings a year, with not more than 120 days between two meetings (relaxed for small companies to 2).",
            "Annual General Meeting within 6 months of the financial year end, and within 15 months of the last AGM.",
            "Form AOC-4 - financial statements, filed within 30 days of the AGM.",
            "Form MGT-7 or MGT-7A - annual return, filed within 60 days of the AGM.",
            "Form DPT-3 for deposits, MSME-1 for dues to micro and small enterprises, and DIR-3 KYC for every director.",
            "Statutory registers - members, directors, charges, related party contracts - must be maintained at the registered office.",
            "Statutory audit is compulsory for every company regardless of turnover; tax audit applies above prescribed limits.",
        ],
        "laws": [
            "Companies Act, 2013 - Sections 92 (annual return), 96 (AGM), 129 (financial statements), 134, 137, 173 (Board meetings)",
            "Companies (Accounts) Rules, 2014 and Companies (Management and Administration) Rules, 2014",
        ],
        "steps": [
            "Prepare a compliance calendar at the start of the financial year listing every due date.",
            "Hold and minute Board meetings with proper 7-day notice.",
            "Get the books audited and the financial statements signed by the Board and the auditor.",
            "Hold the AGM and adopt the accounts.",
            "File AOC-4 and MGT-7 on the MCA portal within the deadlines.",
            "File the income tax return and, if applicable, the tax audit report.",
        ],
        "faqs": [
            {
                "q": "What if my company has done no business at all?",
                "a": "You must still file the annual returns as a dormant or nil-activity company, or formally apply for dormant status or strike-off. Simply stopping filing leads to disqualification of directors.",
            },
        ],
        "keywords": ["compliance", "aoc-4", "mgt-7", "agm", "annual filing", "roc", "board meeting", "statutory audit", "penalty", "company law compliance"],
    },
    {
        "id": "shareholder-rights",
        "category": "corporate",
        "title": "Shareholder Rights and Oppression / Mismanagement",
        "summary": (
            "Shareholders own the company but do not run it. The law therefore gives them "
            "information rights, voting rights and, when the majority abuses its power, a "
            "special remedy before the National Company Law Tribunal for oppression and "
            "mismanagement."
        ),
        "key_points": [
            "Right to receive notice of and vote at general meetings; a member may appoint a proxy.",
            "Right to receive dividend once declared, to inspect statutory registers, and to get copies of financial statements.",
            "Pre-emptive right - a rights issue must first be offered to existing shareholders in proportion to their holding.",
            "Minority protection: members holding at least 10 per cent of shares or 10 per cent of members can apply under Sections 241-242 for oppression and mismanagement.",
            "Class action under Section 245 allows members or depositors to sue the company, directors and auditors together.",
            "Variation of class rights needs the consent of that class, usually by special resolution.",
            "A shareholders' agreement can add contractual rights such as tag-along, drag-along, anti-dilution and board seats.",
        ],
        "laws": [
            "Companies Act, 2013 - Sections 47 (voting), 62 (further issue), 96-114 (meetings), 241-246 (oppression, mismanagement, class action)",
            "SEBI regulations for listed companies",
        ],
        "steps": [
            "Send a written request to the company for inspection of records and copies of resolutions.",
            "If ignored, issue a legal notice recording the refusal.",
            "Collect evidence of the oppressive conduct - diversion of funds, illegal allotment diluting you, exclusion from management.",
            "Check whether you meet the 10 per cent threshold, or apply for waiver of the threshold from the NCLT.",
            "File a petition before the NCLT under Sections 241-242 seeking specific reliefs.",
            "Consider parallel remedies - a civil suit, or enforcement of the shareholders' agreement by arbitration.",
        ],
        "faqs": [
            {
                "q": "What can the NCLT actually order?",
                "a": "Almost anything to end the oppression - cancelling an allotment, buying out the minority at a fair value, removing directors, regulating future conduct, or even winding up the company.",
            },
        ],
        "keywords": ["shareholder", "oppression", "mismanagement", "nclt", "minority", "class action", "section 241", "rights issue", "voting", "dividend"],
    },

    # ==================================================================
    # CONTRACT AND COMMERCIAL LAW
    # ==================================================================
    {
        "id": "valid-contract",
        "category": "contract",
        "title": "What Makes an Agreement a Valid Contract",
        "summary": (
            "The Indian Contract Act, 1872 gives a simple equation: agreement plus enforceability "
            "equals contract. Every commercial dispute starts with the question of whether a "
            "binding contract existed at all, so these ingredients are the foundation of all "
            "business law."
        ),
        "key_points": [
            "Offer and unqualified acceptance - a counter-offer rejects the original offer.",
            "Lawful consideration - something of value each way; an agreement without consideration is void, except a written registered promise out of natural love and affection, compensation for past voluntary service, or a promise to pay a time-barred debt.",
            "Free consent - consent caused by coercion, undue influence, fraud, misrepresentation or mistake makes the contract voidable.",
            "Capacity - a minor's agreement is void ab initio; persons of unsound mind and those disqualified by law cannot contract.",
            "Lawful object - an agreement to do something illegal, immoral or against public policy is void.",
            "Intention to create legal relations - social and domestic promises are usually not contracts.",
            "An oral contract is valid and enforceable, but proving it is much harder; some contracts must be written and registered.",
        ],
        "laws": [
            "Indian Contract Act, 1872 - Sections 10 (what agreements are contracts), 2 (definitions), 11 (capacity), 13-22 (consent), 23 (lawful object), 25 (consideration), 73-75 (damages)",
            "Mohori Bibee v. Dharmodas Ghose (1903) - minor's agreement is void",
            "Information Technology Act, 2000 - electronic contracts and digital signatures are valid",
        ],
        "steps": [
            "Write down what each side is promising and what each side is getting.",
            "Check all six ingredients above against your facts.",
            "Put it in writing, even a simple one-page agreement, and have both parties sign every page.",
            "Add the essential clauses: scope, price and payment schedule, timelines, confidentiality, termination, indemnity, governing law and dispute resolution.",
            "Stamp the document as required by the state Stamp Act - an unstamped agreement may not be admitted in evidence.",
            "Keep the signed original safely; exchange scanned copies by email so the trail is recorded.",
        ],
        "faqs": [
            {
                "q": "Is a WhatsApp agreement legally valid?",
                "a": "It can be. Electronic records are recognised, and courts have accepted WhatsApp chats as evidence of an agreement when the terms are clear and the identity of the parties is proved.",
            },
            {
                "q": "Is a contract on plain paper valid without stamp paper?",
                "a": "It is valid between the parties, but if it is not stamped as the law requires, the court may refuse to look at it until you pay the deficit stamp duty plus a penalty.",
            },
        ],
        "keywords": ["contract", "agreement", "offer", "acceptance", "consideration", "free consent", "void", "voidable", "indian contract act", "capacity", "minor"],
    },
    {
        "id": "breach-and-remedies",
        "category": "contract",
        "title": "Breach of Contract and the Remedies Available",
        "summary": (
            "When one side does not do what it promised, the law gives the innocent party a menu "
            "of remedies. Which one you get depends on whether money can fix the problem, and on "
            "how carefully you drafted the contract before the dispute arose."
        ),
        "key_points": [
            "Damages are the default remedy - they put you where you would have been if the contract had been performed.",
            "Only losses that arise naturally, or that both parties knew about when contracting, are recoverable (the rule in Hadley v. Baxendale).",
            "You have a duty to mitigate - a court will not compensate loss you could reasonably have avoided.",
            "Liquidated damages clauses are enforceable up to reasonable compensation; Indian courts do not award more than actual loss even if a bigger figure is written, except where loss is hard to prove.",
            "Specific performance - an order to actually perform - is now the norm rather than the exception for most contracts after the 2018 amendment.",
            "Injunction stops a party from doing something in breach, such as violating an exclusivity clause.",
            "Rescission cancels the contract and restores both sides to their original position; quantum meruit pays for work actually done.",
        ],
        "laws": [
            "Indian Contract Act, 1872 - Sections 39, 55, 73 (compensation), 74 (liquidated damages), 75",
            "Specific Relief Act, 1963 as amended in 2018 - Sections 10, 14, 20, 36-42",
            "Hadley v. Baxendale (1854) - remoteness of damage",
        ],
        "steps": [
            "Read the contract and identify the exact clause breached and the date of breach.",
            "Check whether the contract requires a cure notice giving the other side time to fix it.",
            "Calculate your loss with documents - invoices, replacement cost, lost profit evidence.",
            "Send a legal notice setting out the breach, the loss and a deadline.",
            "Try the contractual dispute resolution route (mediation or arbitration) if the clause requires it.",
            "File the appropriate proceeding - a summary suit for a clear money claim, a regular suit for damages, or an arbitration claim.",
        ],
        "faqs": [
            {
                "q": "Can I claim mental agony as damages in a business contract?",
                "a": "Rarely in a purely commercial contract. Compensation for mental agony is more commonly awarded in consumer cases and in contracts of a personal nature.",
            },
            {
                "q": "What is force majeure?",
                "a": "A clause excusing performance when an extraordinary event beyond a party's control - flood, war, government prohibition - prevents it. Without such a clause, you must rely on Section 56 frustration, which is much narrower.",
            },
        ],
        "keywords": ["breach", "damages", "specific performance", "injunction", "compensation", "liquidated damages", "force majeure", "frustration", "section 73", "remedy"],
    },
    {
        "id": "sale-of-goods",
        "category": "contract",
        "title": "Sale of Goods - Conditions, Warranties and Risk",
        "summary": (
            "The Sale of Goods Act, 1930 governs every transaction where goods are exchanged for "
            "a price. Its most useful ideas for business are the difference between a condition "
            "and a warranty, and the rule that risk normally follows ownership, not possession."
        ),
        "key_points": [
            "A condition goes to the root of the contract - its breach lets the buyer reject the goods and cancel.",
            "A warranty is collateral - its breach only allows a claim for damages, not rejection.",
            "Implied conditions include title, correspondence with description, merchantable quality, fitness for a disclosed purpose, and correspondence with sample.",
            "Caveat emptor - let the buyer beware - is the starting rule, but the implied conditions have made large exceptions to it.",
            "Risk passes with property unless agreed otherwise - so the party who owns the goods bears the loss if they are destroyed.",
            "An unpaid seller has a lien over the goods, a right of stoppage in transit, and a right of resale.",
            "Nemo dat quod non habet - a seller cannot pass a better title than he has, subject to exceptions like sale by a mercantile agent.",
        ],
        "laws": [
            "Sale of Goods Act, 1930 - Sections 12-17 (conditions and warranties), 18-26 (transfer of property and risk), 45-54 (unpaid seller)",
            "Consumer Protection Act, 2019 for consumer transactions",
        ],
        "steps": [
            "Put the specification, quantity, quality standard and inspection right in the purchase order.",
            "State clearly when property and risk pass - on dispatch, on delivery, or on payment.",
            "Fix the payment terms and the consequence of delay, including interest.",
            "Inspect goods promptly on delivery and record defects in writing within the contractual period.",
            "Reject defective goods immediately and give notice - continuing to use them can amount to acceptance.",
            "Claim damages or replacement, and for consumer purchases use the consumer forum.",
        ],
        "faqs": [
            {
                "q": "What is the difference between a sale and an agreement to sell?",
                "a": "In a sale, ownership passes immediately. In an agreement to sell, ownership passes at a future date or on a condition being fulfilled; until then the risk stays with the seller.",
            },
        ],
        "keywords": ["sale of goods", "condition", "warranty", "caveat emptor", "risk", "unpaid seller", "delivery", "goods", "merchantable quality", "title"],
    },
    {
        "id": "ecommerce-terms",
        "category": "contract",
        "title": "Online Contracts, Terms of Service and Privacy Policies",
        "summary": (
            "Every app and website forms contracts with thousands of users through standard terms "
            "nobody reads. Indian law recognises these click-wrap contracts, but it also imposes "
            "duties: mandatory disclosures, a grievance officer, and a privacy notice under the "
            "new data protection law."
        ),
        "key_points": [
            "Click-wrap - the user actively ticks 'I agree' - is enforceable. Browse-wrap, where terms are merely linked in a footer, is much weaker.",
            "Standard form contracts are read against the drafter, and unreasonable clauses can be struck down as unconscionable.",
            "E-commerce entities must display the seller's identity, total price, return and refund policy, delivery timelines and a grievance officer's contact.",
            "Dark patterns - misleading design that tricks users into purchases or subscriptions - are specifically prohibited by CCPA guidelines.",
            "The DPDP Act, 2023 requires a clear notice, a lawful basis (usually consent), and honouring user rights to access, correction and erasure.",
            "Intermediaries must publish rules, appoint a Grievance Officer, and act on takedown orders to keep their safe-harbour protection.",
            "A jurisdiction clause in the terms is generally valid but cannot defeat a consumer's statutory right to sue where they reside.",
        ],
        "laws": [
            "Information Technology Act, 2000 - Sections 10A (validity of electronic contracts), 79 (intermediary safe harbour)",
            "Consumer Protection (E-Commerce) Rules, 2020",
            "Digital Personal Data Protection Act, 2023",
            "IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021",
        ],
        "steps": [
            "Draft Terms of Service covering eligibility, licence to use, payment, refunds, prohibited conduct, liability limits and termination.",
            "Draft a Privacy Policy stating what data you collect, why, how long you keep it, who you share it with, and how users can exercise their rights.",
            "Implement a real consent flow - an unticked checkbox, not a pre-ticked one.",
            "Publish the name and contact of the Grievance Officer and respond within the prescribed time.",
            "Keep version-dated copies of the terms so you can prove which version a user accepted.",
            "Review annually and whenever the law or your data practices change.",
        ],
        "faqs": [
            {
                "q": "Do I need a privacy policy for a college project website?",
                "a": "If you collect any personal data - even an email address - yes, you should publish one. It is good practice and the DPDP Act applies to digital personal data processed in India.",
            },
        ],
        "keywords": ["terms of service", "privacy policy", "click wrap", "ecommerce", "dpdp", "data protection", "online contract", "dark patterns", "intermediary", "grievance officer"],
    },

    # ==================================================================
    # LABOUR LAW
    # ==================================================================
    {
        "id": "labour-codes",
        "category": "labour",
        "title": "The Four Labour Codes - What Changed",
        "summary": (
            "India consolidated 29 central labour laws into four Codes covering wages, industrial "
            "relations, social security, and occupational safety. The Codes standardise "
            "definitions like 'wages' and 'employee' across all laws, which changes PF, gratuity "
            "and bonus calculations for almost every organisation."
        ),
        "key_points": [
            "Code on Wages, 2019 - minimum wages, timely payment, bonus and equal remuneration, now covering all employees rather than only scheduled employments.",
            "Industrial Relations Code, 2020 - trade unions, standing orders, retrenchment, layoff and strikes.",
            "Code on Social Security, 2020 - PF, ESI, gratuity, maternity benefit, and for the first time gig and platform workers.",
            "Occupational Safety, Health and Working Conditions Code, 2020 - factories, contract labour, migrant workers, and safety duties.",
            "The uniform definition of 'wages' requires that allowances excluded from wages must not exceed 50 per cent of total remuneration, raising PF and gratuity liability where salaries were allowance-heavy.",
            "A national floor wage is fixed by the Centre below which no state minimum wage may fall.",
            "Threshold for standing orders and for prior government permission before retrenchment has been raised, easing compliance for medium units.",
        ],
        "laws": [
            "Code on Wages, 2019",
            "Industrial Relations Code, 2020",
            "Code on Social Security, 2020",
            "Occupational Safety, Health and Working Conditions Code, 2020",
        ],
        "steps": [
            "Map your workforce - employees, workers, contract labour, apprentices, gig workers.",
            "Restructure the salary so that basic plus dearness allowance is at least 50 per cent of the CTC.",
            "Register and maintain the electronic registers and returns the Codes prescribe.",
            "Issue appointment letters to every employee, which the Codes make mandatory.",
            "Review your standing orders, leave policy and working-hour records against the new limits.",
            "Track the commencement notifications, because states must also frame rules before the Codes are fully enforced.",
        ],
        "faqs": [
            {
                "q": "Are the labour codes in force?",
                "a": "They have been passed by Parliament, and implementation has been phased with states framing their own rules. Until a Code is notified in your state, the older Acts continue to apply there - so always check the current status.",
            },
        ],
        "keywords": ["labour code", "wages code", "industrial relations", "social security", "osh code", "labour law", "minimum wage", "gig workers", "29 laws"],
    },
    {
        "id": "employee-rights",
        "category": "labour",
        "title": "Employee Rights - Salary, Leave, PF and Gratuity",
        "summary": (
            "An employee's core entitlements are surprisingly concrete: a written appointment "
            "letter, timely salary, statutory leave, provident fund, and gratuity after five "
            "years. Most workplace disputes are about one of these five, and most are winnable "
            "with documents alone."
        ),
        "key_points": [
            "Salary must be paid by the 7th of the following month in establishments with fewer than 1000 workers, and by the 10th otherwise.",
            "Provident Fund applies to establishments with 20 or more employees; both employer and employee contribute 12 per cent of basic plus DA.",
            "ESI applies where 10 or more employees are engaged and wages are below the notified ceiling, giving medical and cash benefits.",
            "Gratuity is payable after 5 years of continuous service at 15 days' wages for each completed year; the 5-year rule is waived on death or disablement.",
            "Maternity benefit is 26 weeks of paid leave for the first two children, with a creche facility where 50 or more employees work.",
            "Earned leave, casual leave and sick leave depend on the state Shops and Establishments Act - typically around 15 to 21 days of earned leave a year.",
            "Full and final settlement, including unpaid salary and leave encashment, should be paid within two days of the last working day under the Wages Code.",
        ],
        "laws": [
            "Code on Wages, 2019 and Code on Social Security, 2020",
            "Employees' Provident Funds and Miscellaneous Provisions Act, 1952",
            "Payment of Gratuity Act, 1972",
            "Maternity Benefit Act, 1961 as amended in 2017",
            "State Shops and Commercial Establishments Acts",
        ],
        "steps": [
            "Keep every document - appointment letter, payslips, bank statements, emails, resignation acceptance.",
            "Send a written request to HR asking for the specific dues with a computation.",
            "If unpaid, send a legal notice giving 15 days.",
            "For unpaid wages, approach the Authority under the Wages Code or the Labour Commissioner.",
            "For gratuity, file Form I with the employer and then a claim before the Controlling Authority under the Gratuity Act.",
            "For PF, file a grievance on the EPFO portal and escalate to the Regional PF Commissioner.",
        ],
        "faqs": [
            {
                "q": "Can a company withhold my relieving letter if I do not serve the notice period?",
                "a": "It may deduct notice pay as per your contract, but withholding earned salary or experience documents indefinitely as a punishment has been held to be unjustified by several High Courts.",
            },
            {
                "q": "Do interns get PF and gratuity?",
                "a": "Genuine trainees under a recognised apprenticeship scheme are excluded. But if an 'intern' is doing the work of a regular employee for wages, courts look at the substance, not the label.",
            },
        ],
        "keywords": ["salary", "pf", "provident fund", "gratuity", "esi", "leave", "maternity", "employee rights", "full and final", "notice period", "epfo"],
    },
    {
        "id": "termination-law",
        "category": "labour",
        "title": "Termination, Resignation and Wrongful Dismissal",
        "summary": (
            "How an employment ends decides what money changes hands and whether a case follows. "
            "Indian law distinguishes between a 'workman' - who gets strong statutory protection "
            "against retrenchment - and a managerial employee, whose rights come mainly from the "
            "contract."
        ),
        "key_points": [
            "A 'workman' doing manual, skilled, technical, operational or clerical work gets the protection of the Industrial Relations Code; those in mainly managerial or administrative roles usually do not.",
            "Retrenchment of a workman with one year of service requires one month's notice or pay in lieu, retrenchment compensation of 15 days' average pay per completed year, and notice to the government.",
            "Last in, first out - the most recently hired workman in a category should ordinarily go first.",
            "Dismissal for misconduct requires a fair domestic inquiry: a written charge sheet, an opportunity to reply, a hearing, an inquiry report and a proportionate punishment.",
            "Forced resignation obtained under threat can be challenged as a constructive dismissal.",
            "Termination during probation is easier, but must still follow the contract and cannot be discriminatory or malafide.",
            "Notice period and garden leave must be as per the appointment letter; the employer cannot unilaterally extend it.",
        ],
        "laws": [
            "Industrial Relations Code, 2020 - retrenchment, layoff, closure and standing orders",
            "Industrial Disputes Act, 1947 (until the Code is fully notified in the state)",
            "Model Standing Orders and certified standing orders of the establishment",
        ],
        "steps": [
            "Get the termination in writing and note the exact reason given.",
            "Compute what you are owed - salary till date, notice pay, leave encashment, gratuity, bonus, reimbursements.",
            "Send a written representation to the employer disputing the termination within a short time.",
            "If you are a workman, raise an industrial dispute before the Conciliation Officer at the Labour Department.",
            "If conciliation fails, the matter goes to the Labour Court or Industrial Tribunal, which can order reinstatement with back wages.",
            "Managerial employees generally file a civil suit for damages for wrongful termination instead.",
        ],
        "faqs": [
            {
                "q": "Can I be fired by a WhatsApp message?",
                "a": "Technically communication can be electronic, but a termination without following the contractual notice and, for a workman, the statutory procedure, is illegal regardless of the medium.",
            },
        ],
        "keywords": ["termination", "resignation", "retrenchment", "dismissal", "workman", "labour court", "notice pay", "wrongful termination", "layoff", "probation"],
    },
    {
        "id": "contract-labour",
        "category": "labour",
        "title": "Contract Labour, Gig Work and Outsourcing",
        "summary": (
            "Many workers are employed not by the company they work for but by a contractor. The "
            "law regulates this arrangement to stop it being used to deny benefits, and it has "
            "recently begun extending social security to gig and platform workers who fit neither "
            "the employee nor the contractor box."
        ),
        "key_points": [
            "An establishment engaging 20 or more contract workers usually needs registration, and the contractor needs a licence.",
            "The principal employer must ensure wages are paid, and pays them directly if the contractor defaults.",
            "Contract labour is prohibited in work that is perennial and core to the establishment; such workers may claim they are really direct employees.",
            "Courts look at substance - who controls the work, who supervises, who can dismiss - rather than the label on the contract.",
            "Gig and platform workers are now recognised in the Social Security Code, with aggregators contributing 1 to 2 per cent of turnover to a welfare fund.",
            "Equal pay for equal work applies where contract workers do the same work as regular employees in the same establishment.",
            "The principal employer remains liable for safety, working conditions and welfare facilities of contract workers on its premises.",
        ],
        "laws": [
            "Occupational Safety, Health and Working Conditions Code, 2020 - contract labour chapter",
            "Contract Labour (Regulation and Abolition) Act, 1970 (until the Code is notified)",
            "Code on Social Security, 2020 - gig and platform workers",
        ],
        "steps": [
            "Check whether the contractor holds a valid licence and the principal employer is registered.",
            "Preserve ID cards, attendance records, gate passes, payslips and instructions received.",
            "Ask for the wage register and proof of PF and ESI deposit in your name.",
            "Complain to the Labour Enforcement Officer if wages or benefits are short-paid.",
            "For a claim of sham contracting, raise an industrial dispute seeking regularisation.",
        ],
        "faqs": [
            {
                "q": "Are delivery riders employees?",
                "a": "They are usually engaged as independent partners. The Social Security Code creates a separate category of gig and platform workers with welfare benefits, and litigation on their exact status is ongoing.",
            },
        ],
        "keywords": ["contract labour", "gig worker", "platform worker", "outsourcing", "principal employer", "contractor", "regularisation", "aggregator", "sham contract"],
    },

    # ==================================================================
    # INTELLECTUAL PROPERTY
    # ==================================================================
    {
        "id": "copyright-basics",
        "category": "ipr",
        "title": "Copyright - What It Protects and How to Enforce It",
        "summary": (
            "Copyright protects the expression of an idea, never the idea itself. It arises "
            "automatically the moment an original work is created and fixed in some form - no "
            "registration needed - which makes it the most accessible intellectual property "
            "right for a student, artist or developer."
        ),
        "key_points": [
            "Protected works: literary (including computer programs), dramatic, musical and artistic works, cinematograph films and sound recordings.",
            "Term is generally the author's lifetime plus 60 years; for films, sound recordings and photographs it is 60 years from publication.",
            "Registration is optional but the certificate is strong prima facie evidence in court.",
            "The author is the first owner, except a work made during employment under a contract of service, where the employer owns it.",
            "Fair dealing permits private study, research, criticism, review, reporting current events, and educational use within limits.",
            "Moral rights - the right to be identified as the author and to object to distortion - stay with the author even after the copyright is sold.",
            "Remedies include injunction, damages, account of profits, delivery up of infringing copies, and criminal prosecution.",
        ],
        "laws": [
            "Copyright Act, 1957 - Sections 13 (works), 14 (rights), 17 (ownership), 51 (infringement), 52 (fair dealing), 57 (moral rights)",
            "Copyright Rules, 2013",
            "Information Technology Act, 2000 - takedown of infringing content by intermediaries",
        ],
        "steps": [
            "Keep dated proof of creation - drafts, version history, git commits, email to yourself.",
            "Add a copyright notice: (c) year, name, all rights reserved.",
            "Optionally register at the Copyright Office by filing Form XIV with the work and the fee.",
            "On infringement, collect screenshots with URL and date, and preserve the evidence.",
            "Send a cease and desist notice, and a takedown notice to the platform hosting the content.",
            "If ignored, file a suit for injunction and damages in the District Court or High Court.",
        ],
        "faqs": [
            {
                "q": "Is software protected by copyright or patent in India?",
                "a": "Software is protected as a literary work under copyright. A computer program 'per se' is not patentable, though an invention with a genuine technical effect that uses software may be.",
            },
            {
                "q": "Can I use a song in my college project video?",
                "a": "Not freely. Educational use has narrow exceptions and does not generally cover uploading to a public platform. Use royalty-free or Creative Commons licensed music instead, and credit it.",
            },
        ],
        "keywords": ["copyright", "infringement", "fair dealing", "moral rights", "software copyright", "plagiarism", "takedown", "creative commons", "author", "60 years"],
    },
    {
        "id": "trademark-registration",
        "category": "ipr",
        "title": "Trademarks - Brand Names, Logos and Registration",
        "summary": (
            "A trademark is anything that distinguishes your goods or services from someone "
            "else's - a name, a logo, a shape, even a sound. Registration gives you a nationwide "
            "monopoly in that class and is the cheapest insurance a business can buy for its "
            "brand."
        ),
        "key_points": [
            "Goods and services are divided into 45 classes; you register only in the classes you operate in.",
            "A mark must be distinctive. Generic and purely descriptive marks are refused unless they have acquired distinctiveness through long use.",
            "Registration lasts 10 years and is renewable indefinitely.",
            "Use the TM symbol while the application is pending and the R symbol only after registration.",
            "Even without registration, a business can sue for passing off based on goodwill built by actual use.",
            "The process is: search, file TM-A, examination report, reply, publication in the Trade Marks Journal, four months for opposition, then registration.",
            "Non-use for five years and three months makes a registered mark vulnerable to a rectification petition.",
        ],
        "laws": [
            "Trade Marks Act, 1999 - Sections 9 (absolute grounds), 11 (relative grounds), 18 (application), 21 (opposition), 29 (infringement)",
            "Trade Marks Rules, 2017",
        ],
        "steps": [
            "Do a public search on the IP India portal and a general internet and MCA name search.",
            "Pick the correct class or classes for your goods and services.",
            "File form TM-A online - fees are lower for individuals, startups and small enterprises.",
            "Respond to the examination report within one month if objections are raised.",
            "Attend the show-cause hearing if the objection is maintained.",
            "After publication, wait out the opposition period; if unopposed, the registration certificate is issued.",
        ],
        "faqs": [
            {
                "q": "Can I trademark my own name?",
                "a": "Yes, if it is used as a brand and has become distinctive of your goods or services. Common surnames are harder to register without proof of reputation.",
            },
            {
                "q": "How much does a trademark cost?",
                "a": "The government fee is a few thousand rupees per class for an individual or startup, and higher for a large company. Attorney fees are extra.",
            },
        ],
        "keywords": ["trademark", "brand", "logo", "tm", "registration", "passing off", "class", "opposition", "infringement", "trade marks act"],
    },
    {
        "id": "patents",
        "category": "ipr",
        "title": "Patents - Protecting an Invention",
        "summary": (
            "A patent gives an inventor a 20-year monopoly in exchange for publicly disclosing "
            "how the invention works. It is the strongest but also the slowest and most expensive "
            "intellectual property right, and a single public disclosure before filing can "
            "destroy the whole application."
        ),
        "key_points": [
            "Three tests: novelty (new anywhere in the world), inventive step (not obvious to a skilled person), and industrial applicability.",
            "Section 3 excludes many things - mere discoveries, mathematical or business methods, computer programs per se, methods of agriculture, and methods of medical treatment.",
            "Term is 20 years from the date of filing, subject to paying annual renewal fees.",
            "A provisional specification can be filed first to secure a priority date, with the complete specification within 12 months.",
            "The application is published 18 months after filing, and examination must be requested separately within the prescribed period.",
            "Startups, small entities and educational institutions get large fee concessions and expedited examination.",
            "Do not publish a paper, demo the product publicly or post about it before filing - that becomes prior art against you.",
        ],
        "laws": [
            "Patents Act, 1970 as amended - Sections 2(1)(j), 3 and 4 (non-patentable), 9 (provisional), 11A (publication), 53 (term)",
            "Patents Rules, 2003 as amended",
        ],
        "steps": [
            "Do a prior art search on Google Patents, the Indian patent database and scientific literature.",
            "Keep an inventor's notebook with dated entries and signatures.",
            "File a provisional application to lock in the priority date if the invention is still evolving.",
            "File the complete specification with claims, description, drawings and abstract within 12 months.",
            "File form 18 requesting examination, and reply to the First Examination Report within the deadline.",
            "Attend the hearing if required; on grant, pay the renewal fees every year to keep it alive.",
        ],
        "faqs": [
            {
                "q": "Can a student file a patent?",
                "a": "Yes. Students and educational institutions get an 80 per cent fee reduction in many categories, and many colleges have an IPR cell that helps with drafting.",
            },
            {
                "q": "Is an idea patentable?",
                "a": "No. An idea must be developed into a concrete, workable invention with a technical solution before it can be claimed.",
            },
        ],
        "keywords": ["patent", "invention", "novelty", "inventive step", "prior art", "provisional specification", "20 years", "patent office", "section 3", "claims"],
    },
    {
        "id": "trade-secrets-designs",
        "category": "ipr",
        "title": "Designs, Trade Secrets and Confidential Information",
        "summary": (
            "Not everything valuable can be patented or copyrighted. The visual shape of a "
            "product is protected by design registration, and commercially valuable secrets - "
            "recipes, algorithms, customer lists - are protected not by any registration but by "
            "contract and the law of confidence."
        ),
        "key_points": [
            "A design protects only the shape, configuration, pattern or ornament that appeals to the eye, not how the article functions.",
            "Design registration lasts 10 years, extendable by 5, and the design must be new and not previously published anywhere.",
            "India has no dedicated trade secrets statute; protection comes from contract, equity and the common law of breach of confidence.",
            "The three ingredients of a confidence claim are: the information had the necessary quality of confidence, it was imparted in circumstances importing an obligation, and it was used without authorisation.",
            "Non-disclosure agreements and confidentiality clauses in employment contracts are the practical protection.",
            "Post-employment non-compete clauses are void under Section 27 of the Contract Act as restraint of trade; non-solicitation and confidentiality clauses are enforceable.",
            "Practical security - access control, need-to-know, exit interviews, device policies - matters as much as the paperwork.",
        ],
        "laws": [
            "Designs Act, 2000 and Designs Rules, 2001",
            "Indian Contract Act, 1872 - Section 27 (restraint of trade)",
            "Common law of breach of confidence as applied by Indian courts",
        ],
        "steps": [
            "Identify precisely what is secret and write it down in a confidential information schedule.",
            "Sign an NDA before any disclosure to a vendor, investor or potential partner.",
            "Add confidentiality, assignment of IP and non-solicitation clauses to every employment contract.",
            "Mark documents 'Confidential' and restrict access technically.",
            "For a design, file the application with representations of the article before any public launch.",
            "On breach, act fast - seek an urgent injunction, because delay itself weakens a confidence claim.",
        ],
        "faqs": [
            {
                "q": "Is a non-compete clause valid in India?",
                "a": "During employment, yes. After employment ends, a clause preventing you from working elsewhere is void under Section 27. Only confidentiality and reasonable non-solicitation survive.",
            },
        ],
        "keywords": ["design", "trade secret", "nda", "confidential", "non compete", "section 27", "restraint of trade", "non solicitation", "breach of confidence"],
    },

    # ==================================================================
    # CYBER LAW
    # ==================================================================
    {
        "id": "cybercrime-reporting",
        "category": "cyber",
        "title": "Cybercrime - Online Fraud, Hacking and How to Report",
        "summary": (
            "Cybercrime cases succeed or fail in the first few hours. India has a national "
            "cybercrime reporting portal and a dedicated helpline number 1930, and for financial "
            "fraud reporting within what is called the golden hour can get the money frozen "
            "before it is withdrawn."
        ),
        "key_points": [
            "Common offences: identity theft, phishing, OTP fraud, UPI fraud, hacking, ransomware, cyberstalking, sextortion and morphed images.",
            "Report financial fraud immediately on the National Cybercrime Reporting Portal or by calling 1930 - the sooner the report, the better the chance of freezing the transfer.",
            "Under the IT Act, unauthorised access, data theft and introducing a virus attract compensation and criminal punishment.",
            "Identity theft and cheating by personation using a computer are separate offences with imprisonment up to three years.",
            "Publishing or transmitting obscene or sexually explicit material electronically is punishable, with heavier punishment involving children.",
            "Electronic records and their certificates are admissible as evidence if the statutory certificate is produced.",
            "Never share OTP, CVV, or screen access; no bank or government officer ever asks for them.",
        ],
        "laws": [
            "Information Technology Act, 2000 - Sections 43, 43A, 65, 66, 66C, 66D, 66E, 67, 67A, 67B, 72A",
            "Bharatiya Nyaya Sanhita, 2023 - cheating, forgery and criminal breach of trust",
            "Bharatiya Sakshya Adhiniyam, 2023 - admissibility of electronic records",
        ],
        "steps": [
            "Immediately call 1930 and report on the national cybercrime portal with transaction details.",
            "Inform your bank in writing and ask them to freeze the beneficiary account and raise a chargeback.",
            "Take screenshots with visible URL, date and time; export chat logs and emails with headers.",
            "Do not format the device or delete anything - it is evidence.",
            "File an FIR at the local police station or the cyber cell; they cannot refuse under the Zero FIR rule.",
            "Follow up with the acknowledgement number and, if the bank delays, complain to the RBI Ombudsman.",
        ],
        "faqs": [
            {
                "q": "Will I get my money back after a UPI fraud?",
                "a": "Often yes, if you report within the golden hour of a few hours and the bank freezes the beneficiary account before withdrawal. RBI's limited liability rules protect customers who report unauthorised transactions promptly.",
            },
            {
                "q": "Someone created a fake profile with my photos. What do I do?",
                "a": "Report it to the platform for impersonation, preserve screenshots and the profile URL, file a complaint on the cybercrime portal, and ask the police for a takedown direction under the IT Rules.",
            },
        ],
        "keywords": ["cybercrime", "online fraud", "hacking", "phishing", "upi fraud", "1930", "cyber cell", "identity theft", "otp fraud", "sextortion", "it act"],
    },
    {
        "id": "data-protection",
        "category": "cyber",
        "title": "Data Protection - The DPDP Act, 2023",
        "summary": (
            "India's first comprehensive data privacy law creates a simple structure: whoever "
            "decides why and how personal data is processed is a Data Fiduciary and owes duties "
            "to the individual, called a Data Principal. Consent must be free, specific, informed "
            "and revocable."
        ),
        "key_points": [
            "Applies to digital personal data processed in India, and to processing outside India that offers goods or services to people in India.",
            "A clear notice must be given describing the data, the purpose, and how to withdraw consent and complain.",
            "Lawful bases are consent and certain 'legitimate uses' such as an employment purpose or a medical emergency.",
            "Data Principal rights: access, correction, erasure, grievance redressal, and nomination of another person to exercise rights.",
            "Children's data - anyone under 18 - requires verifiable parental consent, and tracking or targeted advertising at children is prohibited.",
            "Significant Data Fiduciaries have extra duties: a Data Protection Officer in India, independent audits and impact assessments.",
            "Breaches must be notified to the Data Protection Board and to affected individuals; penalties can run to hundreds of crores.",
        ],
        "laws": [
            "Digital Personal Data Protection Act, 2023",
            "Information Technology Act, 2000 - Section 43A and the SPDI Rules, 2011 (existing regime)",
            "K.S. Puttaswamy v. Union of India (2017) - privacy as a Fundamental Right",
        ],
        "steps": [
            "Map what personal data you collect, where it is stored, who can access it and how long you keep it.",
            "Write a plain-language privacy notice and get consent through an affirmative action.",
            "Build the mechanism to let a user withdraw consent as easily as they gave it.",
            "Sign data processing agreements with every vendor who handles your users' data.",
            "Set retention limits and delete data when the purpose is over.",
            "Prepare a breach response plan naming who reports, to whom, and within what time.",
        ],
        "faqs": [
            {
                "q": "Does the DPDP Act apply to a college project?",
                "a": "If your project processes real personal data of real people, treat it as applicable and follow the same practices. If you use only dummy data, there is no personal data being processed.",
            },
        ],
        "keywords": ["dpdp", "data protection", "privacy", "consent", "data fiduciary", "data principal", "personal data", "puttaswamy", "breach", "2023"],
    },
    {
        "id": "social-media-law",
        "category": "cyber",
        "title": "Social Media, Content Takedown and Intermediary Liability",
        "summary": (
            "Platforms are not liable for what users post, provided they follow the conditions "
            "for safe harbour. Those conditions - due diligence, grievance officers, and prompt "
            "action on lawful orders - are what the IT Rules, 2021 spell out, and they are also "
            "the route an ordinary user takes to get harmful content removed."
        ),
        "key_points": [
            "Section 79 safe harbour protects an intermediary that does not initiate, select the receiver of, or modify the content.",
            "Every intermediary must publish rules, a privacy policy and user agreement, and appoint a Grievance Officer who acknowledges a complaint in 24 hours and resolves it in 15 days.",
            "Significant social media intermediaries must also appoint a Chief Compliance Officer, a Nodal Contact Person and a Resident Grievance Officer, all resident in India, and publish monthly compliance reports.",
            "Non-consensual intimate imagery must be removed within 24 hours of a complaint.",
            "Grievance Appellate Committees hear appeals against a platform's decision on a complaint.",
            "Defamatory posts can attract both civil and criminal proceedings against the poster, not the platform.",
            "Free speech online is protected by Article 19(1)(a) but subject to the reasonable restrictions in Article 19(2); Shreya Singhal struck down the vague Section 66A.",
        ],
        "laws": [
            "Information Technology Act, 2000 - Sections 69A and 79",
            "IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021",
            "Shreya Singhal v. Union of India (2015) - Section 66A struck down",
        ],
        "steps": [
            "Preserve evidence first - screenshots showing URL, handle, date and time; use a screen recording for stories.",
            "Report the content in the platform's own tool and note the ticket number.",
            "If unresolved, write to the platform's Resident Grievance Officer, whose details must be published.",
            "Appeal to the Grievance Appellate Committee if the platform refuses or does not respond.",
            "In parallel, file a complaint on the cybercrime portal for offences like obscenity, impersonation or threats.",
            "For serious defamation, send a legal notice and consider a civil suit for injunction and damages.",
        ],
        "faqs": [
            {
                "q": "Can I be arrested for a social media post?",
                "a": "Section 66A was struck down as unconstitutional, so a mere offensive post is not an offence under it. But posts amounting to defamation, threats, obscenity, incitement or hate speech can still attract criminal law.",
            },
        ],
        "keywords": ["social media", "intermediary", "takedown", "safe harbour", "it rules 2021", "grievance officer", "shreya singhal", "66a", "content removal", "trolling"],
    },
    {
        "id": "digital-evidence",
        "category": "cyber",
        "title": "Electronic Evidence and Digital Signatures",
        "summary": (
            "A screenshot by itself is weak. Indian law recognises electronic records as evidence "
            "but attaches a certification requirement, and understanding it turns a WhatsApp "
            "chat or CCTV clip from a story into proof a court will accept."
        ),
        "key_points": [
            "An electronic record produced from a computer is admissible if accompanied by a certificate identifying the record, describing the device and confirming its regular use.",
            "The certificate must be signed by a person in a responsible official position in relation to the device.",
            "Best practice is to produce the original device or the hash value of the file, so tampering can be ruled out.",
            "Digital signatures and electronic signatures are legally recognised and equivalent to a handwritten signature for most documents.",
            "Some documents are excluded from electronic execution - negotiable instruments other than cheques, powers of attorney, trusts, wills and contracts for sale of immovable property.",
            "Chain of custody matters: who seized the device, when, how it was stored, and who accessed it.",
            "Metadata, headers, server logs and call detail records are often stronger than the message content itself.",
        ],
        "laws": [
            "Bharatiya Sakshya Adhiniyam, 2023 - electronic records and the certificate requirement (replacing Section 65B of the Evidence Act)",
            "Information Technology Act, 2000 - Sections 3, 3A, 5 and Schedule I",
            "Anvar P.V. v. P.K. Basheer (2014) and Arjun Panditrao Khotkar (2020) - certificate is mandatory",
        ],
        "steps": [
            "Preserve the original device and do not delete or reinstall anything.",
            "Export the data in its native format with metadata, not just as a photograph of a screen.",
            "Compute and record a hash value of the exported file.",
            "Obtain the statutory certificate from the person controlling the device.",
            "Where the data sits with a service provider, get it preserved by a request through the investigating officer.",
            "File the record with the certificate along with your affidavit of evidence.",
        ],
        "faqs": [
            {
                "q": "Are WhatsApp chats admissible in court?",
                "a": "Yes, if properly proved. You need the device or an export with the statutory certificate; a bare screenshot without certification is often objected to and may be given little weight.",
            },
        ],
        "keywords": ["electronic evidence", "65b", "digital signature", "whatsapp evidence", "cctv", "certificate", "admissibility", "metadata", "hash", "chain of custody"],
    },

    # ==================================================================
    # FAMILY LAW
    # ==================================================================
    {
        "id": "marriage-registration",
        "category": "family",
        "title": "Marriage - Conditions, Registration and Inter-Faith Marriage",
        "summary": (
            "Which law applies to a marriage depends on the religion of the parties, with the "
            "Special Marriage Act available to everyone as a secular option. Registration is not "
            "what makes a marriage valid, but it is what makes it easy to prove for passports, "
            "visas, insurance and inheritance."
        ),
        "key_points": [
            "Hindu Marriage Act conditions: neither party has a living spouse, both are of sound mind, the groom is 21 and the bride 18, and they are not within prohibited degrees unless custom permits.",
            "Special Marriage Act, 1954 allows any two persons of any religion to marry, after a 30-day public notice period.",
            "Muslim marriage is a contract (nikah) requiring offer, acceptance and mahr; Christian marriages are solemnised under the Indian Christian Marriage Act, 1872.",
            "Registration is compulsory in most states, and the Supreme Court has directed compulsory registration of all marriages.",
            "A marriage in violation of the age condition is voidable at the option of the underage party, and child marriage is separately punishable.",
            "Bigamy is an offence for those governed by the Hindu, Christian and Parsi laws, and for anyone married under the Special Marriage Act.",
            "A live-in relationship in the nature of marriage is recognised for the limited purposes of domestic violence protection and maintenance.",
        ],
        "laws": [
            "Hindu Marriage Act, 1955",
            "Special Marriage Act, 1954",
            "Indian Christian Marriage Act, 1872 and Parsi Marriage and Divorce Act, 1936",
            "Prohibition of Child Marriage Act, 2006",
        ],
        "steps": [
            "Collect documents: proof of age and address for both parties, passport photographs, and witnesses' ID.",
            "For Special Marriage Act, file a notice of intended marriage with the Marriage Officer where either party has resided for 30 days.",
            "Wait the 30-day notice period for objections.",
            "Solemnise the marriage before the Marriage Officer and three witnesses, or perform the religious ceremony as applicable.",
            "Apply for the marriage certificate at the sub-registrar's office with the required forms and fee.",
            "Collect the certificate and keep multiple attested copies - it is needed for passport, visa and bank purposes.",
        ],
        "faqs": [
            {
                "q": "Is a temple or court marriage stronger?",
                "a": "Both are valid if the legal conditions are met. What matters in a dispute is proof - a registered certificate is far easier to prove than photographs of a ceremony.",
            },
            {
                "q": "Do inter-faith couples have to convert?",
                "a": "No. The Special Marriage Act exists precisely so that two people of different religions can marry without either converting.",
            },
        ],
        "keywords": ["marriage", "registration", "special marriage act", "hindu marriage act", "inter faith", "nikah", "certificate", "bigamy", "child marriage", "live in"],
    },
    {
        "id": "divorce-maintenance",
        "category": "family",
        "title": "Divorce, Maintenance and Alimony",
        "summary": (
            "A marriage can be dissolved by mutual consent, which is faster and less bitter, or "
            "on contested grounds such as cruelty, desertion or adultery. Separately from "
            "divorce, a spouse and children who cannot maintain themselves have a right to "
            "maintenance, which can be claimed quickly and independently."
        ),
        "key_points": [
            "Mutual consent divorce requires one year of separation, a joint petition, a six-month cooling-off period between the two motions, and a settlement of alimony and custody.",
            "The Supreme Court has held that the six-month cooling-off period can be waived where the marriage is irretrievably broken and the settlement is genuine.",
            "Contested grounds under the Hindu Marriage Act include cruelty, desertion for two years, adultery, conversion, mental disorder, and renunciation of the world.",
            "Maintenance can be claimed under the secular criminal provision available to any wife, child or parent unable to maintain themselves, regardless of religion.",
            "Interim maintenance can be ordered during the case itself so the dependent spouse can afford to fight it.",
            "Permanent alimony can be a monthly sum or a one-time lump sum; courts weigh income, standard of living, duration of marriage and conduct.",
            "A Muslim divorced woman has rights under the 1986 Act, and the Supreme Court has held she may also claim under the general maintenance provision.",
        ],
        "laws": [
            "Hindu Marriage Act, 1955 - Sections 13 (divorce), 13B (mutual consent), 24 and 25 (maintenance and alimony)",
            "Bharatiya Nagarik Suraksha Sanhita, 2023 - maintenance of wife, children and parents (successor to Section 125 CrPC)",
            "Protection of Women from Domestic Violence Act, 2005 - monetary relief",
            "Muslim Women (Protection of Rights on Divorce) Act, 1986",
        ],
        "steps": [
            "Try mediation first - most family courts have a mediation centre and it is free.",
            "Prepare a written settlement covering alimony, custody, visitation, and division of assets and jewellery.",
            "File the joint petition for mutual consent divorce in the family court with jurisdiction.",
            "Record statements at the first motion; wait the cooling-off period, or apply for waiver.",
            "Appear for the second motion, after which the decree of divorce is granted.",
            "For maintenance, file a separate application with proof of the other spouse's income - salary slips, ITR, bank statements.",
        ],
        "faqs": [
            {
                "q": "How long does a mutual consent divorce take?",
                "a": "Typically six to eighteen months. With a waiver of the cooling-off period and a complete settlement, some courts have granted it in a few months.",
            },
            {
                "q": "Can a working woman claim maintenance?",
                "a": "Yes, but the amount is adjusted against her income. The test is whether she can maintain herself at a standard reasonably comparable to that in the matrimonial home.",
            },
        ],
        "keywords": ["divorce", "mutual consent", "alimony", "maintenance", "cruelty", "desertion", "13b", "family court", "125 crpc", "separation", "settlement"],
    },
    {
        "id": "child-custody",
        "category": "family",
        "title": "Child Custody, Guardianship and Adoption",
        "summary": (
            "In every custody dispute the court applies one test above all others: the welfare of "
            "the child. The parents' rights are secondary. Adoption, meanwhile, follows two "
            "separate routes - a religious personal law route and a secular statutory route "
            "through a central agency."
        ),
        "key_points": [
            "Types of custody: physical custody with visitation, joint custody, legal custody (decision-making), and in rare cases third-party custody.",
            "Children below five years are ordinarily left in the mother's care, but this is a guideline, not a rule.",
            "A child of sufficient maturity is heard by the judge in chambers, and their preference carries weight.",
            "The natural guardian of a Hindu minor is the father, and after him the mother - but the Supreme Court has read this down so that the mother can act as guardian where the father is absent or uninvolved.",
            "Adoption under the Hindu Adoptions and Maintenance Act is between Hindus and gives the child the status of a natural-born child.",
            "Adoption under the Juvenile Justice Act, 2015 through CARA is open to all religions, and involves registration, home study, referral and a court order.",
            "Adoption cannot be done privately by an agreement - an unregistered private handover of a child is illegal.",
        ],
        "laws": [
            "Guardians and Wards Act, 1890",
            "Hindu Minority and Guardianship Act, 1956",
            "Hindu Adoptions and Maintenance Act, 1956",
            "Juvenile Justice (Care and Protection of Children) Act, 2015 and the CARA Adoption Regulations",
        ],
        "steps": [
            "For custody, file a petition before the family court or district court where the child ordinarily resides.",
            "Show your capacity to provide - income, housing, schooling arrangements, and available time.",
            "Attend counselling and mediation, which most family courts order first.",
            "Propose a realistic parenting plan with a visitation schedule rather than demanding exclusive custody.",
            "For adoption, register as a prospective adoptive parent on the CARA portal.",
            "Complete the home study, accept a referral, and obtain the adoption order from the court, followed by follow-up reports.",
        ],
        "faqs": [
            {
                "q": "Can a single person adopt?",
                "a": "Yes. A single woman can adopt a child of any gender; a single man cannot adopt a girl child under the CARA regulations. Age difference and age limits also apply.",
            },
            {
                "q": "Does the father lose all rights if the mother gets custody?",
                "a": "No. Custody and guardianship are different. The non-custodial parent normally retains visitation, access, and a say in major decisions about the child.",
            },
        ],
        "keywords": ["custody", "guardianship", "adoption", "cara", "child welfare", "visitation", "family court", "minor", "juvenile justice", "parenting plan"],
    },
    {
        "id": "succession-inheritance",
        "category": "family",
        "title": "Wills, Succession and Inheritance",
        "summary": (
            "Property passes on death in one of two ways: by a will, called testamentary "
            "succession, or by the rules of the applicable personal law when there is no will, "
            "called intestate succession. Writing a simple will is the single cheapest way a "
            "family can avoid years of litigation."
        ),
        "key_points": [
            "A will needs a person of sound mind above 18, signed by the testator and attested by two witnesses who saw the signature.",
            "Registration of a will is optional but strongly recommended, as it makes proof much easier.",
            "A beneficiary should not be a witness, and a doctor's fitness certificate on the date of signing prevents later challenges of unsound mind.",
            "The last valid will revokes earlier ones; every page should be signed and dated.",
            "Under Hindu intestate succession, Class I heirs - widow, sons, daughters, mother - inherit equally and simultaneously.",
            "Daughters are coparceners in a Hindu Undivided Family by birth with the same rights as sons, including for daughters born before the 2005 amendment.",
            "Muslim succession follows Sharia rules, and a Muslim can bequeath only up to one-third of the estate by will without the heirs' consent.",
        ],
        "laws": [
            "Indian Succession Act, 1925 - wills, probate and Christian and Parsi succession",
            "Hindu Succession Act, 1956 as amended in 2005 - Section 6 coparcenary rights of daughters",
            "Muslim personal law (Shariat) Application Act, 1937",
            "Vineeta Sharma v. Rakesh Sharma (2020) - daughters' coparcenary rights confirmed",
        ],
        "steps": [
            "List all assets and liabilities: property, bank accounts, shares, insurance, gold, loans.",
            "Decide who gets what, and appoint an executor you trust.",
            "Write the will in simple language, with a clause revoking earlier wills.",
            "Sign every page in the presence of two witnesses who then sign as attesting witnesses.",
            "Register the will at the sub-registrar's office - optional but advisable.",
            "On death, the executor applies for probate where required, or the heirs apply for a succession certificate or legal heir certificate.",
        ],
        "faqs": [
            {
                "q": "Do I need stamp paper for a will?",
                "a": "No. A will requires no stamp duty and can be written on plain paper. Only the registration fee applies if you choose to register it.",
            },
            {
                "q": "Can a will be challenged?",
                "a": "Yes, on grounds of forgery, unsound mind, coercion, undue influence, or suspicious circumstances. Registration, medical fitness proof and independent witnesses reduce that risk greatly.",
            },
        ],
        "keywords": ["will", "succession", "inheritance", "probate", "intestate", "legal heir", "coparcener", "hindu succession", "testament", "executor", "succession certificate"],
    },

    # ==================================================================
    # PROPERTY LAW
    # ==================================================================
    {
        "id": "property-purchase",
        "category": "property",
        "title": "Buying Property - Due Diligence and Registration",
        "summary": (
            "Buying property is the largest transaction most families make, and the law puts the "
            "burden of checking title squarely on the buyer. A methodical due diligence of "
            "documents before paying anything prevents almost every property dispute that later "
            "reaches court."
        ),
        "key_points": [
            "Verify the chain of title for at least 30 years through the mother deed and all subsequent conveyances.",
            "Obtain an Encumbrance Certificate to confirm no mortgage, lien or attachment is registered against the property.",
            "Check the approved layout plan, building plan sanction, commencement certificate and occupancy certificate.",
            "Confirm land use in the master plan, and that agricultural land has been converted for non-agricultural use if applicable.",
            "Collect the latest property tax receipts, electricity and water bills, and the khata or mutation record.",
            "A sale of immovable property above Rs 100 must be by a registered sale deed - an agreement to sell or a power of attorney does not transfer ownership.",
            "Registration must be done within four months of execution; stamp duty rates vary by state and are often lower for a woman buyer.",
            "TDS of 1 per cent must be deducted by the buyer where the consideration is Rs 50 lakh or more.",
        ],
        "laws": [
            "Transfer of Property Act, 1882 - Sections 54 (sale), 53A (part performance)",
            "Registration Act, 1908 - Sections 17 (compulsory registration), 23 (time limit)",
            "Indian Stamp Act, 1899 and state stamp legislation",
            "Suraj Lamp v. State of Haryana (2011) - sale by power of attorney does not convey title",
        ],
        "steps": [
            "Get certified copies of the title documents and have an advocate issue a title search report.",
            "Apply for the Encumbrance Certificate for the past 30 years from the sub-registrar.",
            "Verify approvals with the municipal or development authority, and RERA registration for an under-construction project.",
            "Execute an agreement to sell recording the price, payment schedule, timeline and default consequences.",
            "Pay the stamp duty and registration fee, and register the sale deed before the sub-registrar with two witnesses.",
            "Apply for mutation or khata transfer in the revenue records and update the electricity and tax records.",
        ],
        "faqs": [
            {
                "q": "Is a General Power of Attorney sale valid?",
                "a": "No. The Supreme Court held that GPA, will and agreement-to-sell transactions do not convey ownership. Only a registered sale deed transfers title.",
            },
            {
                "q": "What is an Encumbrance Certificate?",
                "a": "A certificate from the sub-registrar listing all registered transactions on the property for a period, which shows whether it is mortgaged or otherwise charged.",
            },
        ],
        "keywords": ["property purchase", "sale deed", "registration", "encumbrance certificate", "title", "stamp duty", "khata", "mutation", "due diligence", "gpa"],
    },
    {
        "id": "rent-and-tenancy",
        "category": "property",
        "title": "Landlord and Tenant - Rent, Eviction and Deposits",
        "summary": (
            "Tenancy is governed by a mix of the rent agreement, the state Rent Control Act and "
            "the Model Tenancy Act where adopted. The two questions that generate most disputes "
            "are how much security deposit can be held and on what grounds a tenant can be "
            "evicted."
        ),
        "key_points": [
            "A lease for a year or more must be in writing and registered; the common 11-month agreement is used precisely to avoid compulsory registration.",
            "The Model Tenancy Act, 2021 caps the security deposit at two months' rent for residential premises and six for commercial, where a state has adopted it.",
            "Eviction grounds typically include non-payment of rent, subletting without consent, misuse of premises, bona fide requirement of the landlord and structural repairs.",
            "A landlord cannot evict by force, cut off electricity or water, or change the locks - that is illegal and the tenant can approach the police and court.",
            "Rent increases must follow the agreement or the statutory formula, with prior written notice.",
            "The landlord must return the deposit within the agreed period after handover, deducting only for agreed dues and damage beyond normal wear and tear.",
            "Both parties should record the condition of the premises and the meter readings at the start and end with photographs.",
        ],
        "laws": [
            "Transfer of Property Act, 1882 - Sections 105-117 (leases)",
            "Model Tenancy Act, 2021 (adopted by states individually)",
            "State Rent Control Acts",
            "Registration Act, 1908 - registration of leases of one year or more",
        ],
        "steps": [
            "Verify the landlord's ownership document and identity before paying anything.",
            "Put everything in the written agreement: rent, deposit, escalation, notice period, maintenance, and who pays which bill.",
            "Take dated photographs of every room, fittings and meter readings at handover.",
            "Pay rent by bank transfer so a payment record exists, and collect receipts.",
            "For any dispute, send a written notice first; then approach the Rent Authority or civil court.",
            "At the end, give proper notice, hand over peacefully with a handover letter, and get the deposit refund in writing.",
        ],
        "faqs": [
            {
                "q": "Can a landlord keep my whole deposit for painting?",
                "a": "Only if the agreement says so or the damage exceeds normal wear and tear. Routine repainting after a long tenancy is usually treated as the landlord's cost unless expressly agreed.",
            },
            {
                "q": "Why are rent agreements always 11 months?",
                "a": "Because a lease of one year or more requires compulsory registration and higher stamp duty. An 11-month agreement avoids that, and is renewed instead.",
            },
        ],
        "keywords": ["rent", "tenant", "landlord", "eviction", "security deposit", "lease", "11 month", "model tenancy act", "rent agreement", "notice period"],
    },
    {
        "id": "rera",
        "category": "property",
        "title": "RERA - Homebuyer Protection Against Builder Delay",
        "summary": (
            "RERA was passed because homebuyers had no fast remedy against builders who took "
            "money and delayed for years. It forces registration of projects, escrow of 70 per "
            "cent of buyer money, and gives buyers a dedicated tribunal that decides in months "
            "rather than decades."
        ),
        "key_points": [
            "Every project above 500 square metres or with more than 8 apartments must be registered with the state RERA before any advertisement or sale.",
            "Seventy per cent of the money collected from buyers must be kept in a separate escrow account and used only for that project.",
            "The promoter must upload quarterly updates on construction progress and approvals on the RERA website.",
            "Carpet area is the mandatory basis of sale - selling on super built-up area is not permitted.",
            "On delay, the buyer may either withdraw and get a full refund with interest, or continue and claim monthly interest for the delay period.",
            "Structural defects must be rectified free of cost for five years from handover.",
            "The promoter cannot make changes to the sanctioned plan without the consent of two-thirds of the allottees.",
        ],
        "laws": [
            "Real Estate (Regulation and Development) Act, 2016 - Sections 3 (registration), 4 (escrow), 12, 14, 18 (delay), 31 (complaints)",
            "State RERA Rules",
            "Consumer Protection Act, 2019 - an alternative remedy",
        ],
        "steps": [
            "Check the project's RERA registration number on the state RERA website before booking.",
            "Download the registered project details - approvals, plans, promised completion date, promoter's litigation history.",
            "Keep the allotment letter, agreement for sale, all payment receipts and every communication.",
            "On delay, send a written demand to the promoter citing the agreed possession date.",
            "File a complaint online with the state RERA authority, paying the small prescribed fee.",
            "Attend hearings; appeal to the Real Estate Appellate Tribunal if needed.",
        ],
        "faqs": [
            {
                "q": "RERA or consumer court - which is better?",
                "a": "RERA is specialised and usually faster for delay and refund. The consumer forum can award compensation for mental agony. You may choose, but should not pursue both for the same relief.",
            },
        ],
        "keywords": ["rera", "builder delay", "possession", "refund", "carpet area", "escrow", "homebuyer", "real estate", "allottee", "promoter"],
    },
    {
        "id": "land-records",
        "category": "property",
        "title": "Land Records, Mutation and Partition",
        "summary": (
            "Ownership on paper has two layers: the registered deed that transfers title, and the "
            "revenue record that shows who is in possession and who pays tax. Both must be "
            "updated, and family property must be formally partitioned, or the next generation "
            "inherits a dispute."
        ),
        "key_points": [
            "Mutation is the change of name in the revenue or municipal records after a sale, inheritance or gift.",
            "Mutation does not by itself create title - it is evidence of possession and liability to pay tax.",
            "Key records vary by state: 7/12 extract, khatauni, khata or patta, and the record of rights.",
            "Partition of joint family property can be by a registered partition deed, a family settlement, or a partition suit.",
            "A family settlement of existing rights among members may not need registration, but any document creating or transferring new rights does.",
            "Agricultural land often has ceiling limits and restrictions on purchase by non-agriculturists in several states.",
            "Adverse possession allows a person in open, continuous, hostile possession for 12 years to claim title against the true owner.",
        ],
        "laws": [
            "State Land Revenue Codes and Record of Rights rules",
            "Transfer of Property Act, 1882 and Registration Act, 1908",
            "Partition Act, 1893 and Code of Civil Procedure, 1908",
            "Limitation Act, 1963 - Article 65 on adverse possession",
        ],
        "steps": [
            "Obtain the current record of rights and check whose name stands recorded.",
            "Apply for mutation with the registered deed or the succession documents and the prescribed form.",
            "Publish or serve notice on other interested persons as the rules require.",
            "For a family partition, prepare a partition deed listing shares, get it stamped and registered.",
            "If members do not agree, file a partition suit seeking a preliminary decree declaring shares, then a final decree dividing by metes and bounds.",
            "Update tax records, electricity connection and society records after the change.",
        ],
        "faqs": [
            {
                "q": "Is mutation the same as registration?",
                "a": "No. Registration of a deed transfers legal title. Mutation only updates the government's revenue record so the tax demand goes to the right person.",
            },
        ],
        "keywords": ["land records", "mutation", "partition", "7/12", "khata", "patta", "record of rights", "family settlement", "adverse possession", "revenue record"],
    },
]

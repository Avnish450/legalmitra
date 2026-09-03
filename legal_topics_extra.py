# -*- coding: utf-8 -*-
"""
legal_topics_extra.py
=====================
PART 2 of the topic knowledge base: the remaining ten branches of law
(infrastructure, environment, consumer, taxation, banking, motor,
humanrights, startup, medical, education).

The dictionary format is exactly the same as in legal_topics.py. The knowledge
base was split into two files only so that no single file becomes too long to
open and edit comfortably.
"""

TOPICS_PART2 = [

    # ==================================================================
    # INFRASTRUCTURE AND PUBLIC PROCUREMENT
    # ==================================================================
    {
        "id": "government-tenders",
        "category": "infrastructure",
        "title": "Government Tenders and Public Procurement",
        "summary": (
            "When the government buys goods or awards a construction contract, it cannot simply "
            "pick a friend. Article 14 requires a fair, transparent and non-arbitrary process, "
            "and the General Financial Rules and the e-procurement portals turn that principle "
            "into a detailed tender procedure."
        ),
        "key_points": [
            "Common methods: open tender, limited tender, single tender on justified grounds, and rate contracts through GeM.",
            "A two-bid system separates the technical bid from the financial bid, and only technically qualified bidders' price bids are opened.",
            "Earnest Money Deposit secures the bid; the Performance Bank Guarantee, usually 5 to 10 per cent, secures performance after award.",
            "The lowest evaluated bidder, L1, normally wins, but the tender may use a quality-cum-cost basis for consultancy work.",
            "Public Procurement (Preference to Make in India) Orders give price preference to local suppliers meeting minimum local content.",
            "MSMEs get exemption from EMD and tender fee and a share of procurement under the MSME procurement policy.",
            "Tender conditions can be challenged by writ petition, but courts interfere only where the process is arbitrary, malafide or irrational - not merely because a bidder disagrees.",
        ],
        "laws": [
            "Constitution of India - Article 14 (arbitrariness in State contracts)",
            "General Financial Rules, 2017",
            "Public Procurement (Preference to Make in India) Order, 2017",
            "MSME Development Act, 2006 and the Public Procurement Policy for MSEs",
            "Tata Cellular v. Union of India (1994) - scope of judicial review in tenders",
        ],
        "steps": [
            "Register on the relevant e-procurement portal and obtain a Class III digital signature certificate.",
            "Read the entire tender document, especially eligibility criteria and the bid submission checklist.",
            "Raise queries in the pre-bid meeting - clarifications given there become part of the tender.",
            "Prepare the technical bid with every certificate asked for; a single missing document usually means disqualification.",
            "Submit the EMD and upload the bids before the deadline, since the portal closes automatically.",
            "If aggrieved by the evaluation, first make a written representation; approach the High Court quickly, because delay defeats a tender challenge.",
        ],
        "faqs": [
            {
                "q": "Can a court cancel a tender that was awarded unfairly?",
                "a": "It can, but courts are reluctant to interfere once work has begun. They intervene mainly where the process was arbitrary or malafide, and often grant compensation instead of cancellation.",
            },
        ],
        "keywords": ["tender", "procurement", "gem", "emd", "bank guarantee", "l1", "bid", "government contract", "make in india", "msme"],
    },
    {
        "id": "construction-contracts",
        "category": "infrastructure",
        "title": "Construction and EPC Contracts - Delay, Variation and Claims",
        "summary": (
            "Infrastructure contracts are long, expensive and almost always delayed. The money in "
            "these projects is won or lost not on the original price but on claims - extension of "
            "time, price escalation, idling of machinery and variation in scope - and every claim "
            "depends on contemporaneous records."
        ),
        "key_points": [
            "EPC means Engineering, Procurement and Construction, where a single contractor takes responsibility for the whole delivery at a lump sum price.",
            "An item-rate contract pays per measured quantity; a lump sum contract pays a fixed price regardless of quantity variations.",
            "Extension of Time protects the contractor from liquidated damages when the delay is caused by the employer or by an excusable event.",
            "Concurrent delay - where both parties caused delay in the same period - is one of the hardest issues in construction law.",
            "Price escalation clauses tie payment to published indices for steel, cement, fuel and labour.",
            "Retention money, usually 5 to 10 per cent, is held back and released after the defect liability period, commonly 12 to 24 months.",
            "Most EPC contracts use a tiered dispute mechanism: engineer's decision, then a Dispute Adjudication Board, then arbitration.",
        ],
        "laws": [
            "Indian Contract Act, 1872 - Sections 55, 73 and 74",
            "Arbitration and Conciliation Act, 1996",
            "Standard forms - FIDIC conditions of contract, CPWD and NHAI model documents",
            "Specific Relief Act, 1963 - Section 14 on contracts not specifically enforceable",
        ],
        "steps": [
            "Maintain a daily site diary, labour and plant returns, and dated photographs from day one.",
            "Give written notice of any delay event within the notice period in the contract - late notice often bars the claim entirely.",
            "Keep the as-planned programme and update it, so delay can be demonstrated by a proper analysis.",
            "Submit variation requests in writing and obtain written approval before doing extra work.",
            "Submit claims with a cause-effect narrative, supporting records and a clear computation.",
            "Escalate through the contractual tiers in order; skipping a tier can make the arbitration claim premature.",
        ],
        "faqs": [
            {
                "q": "Can a contractor claim for work done without a written variation order?",
                "a": "It is difficult but possible under quantum meruit if the employer knew of and accepted the benefit of the work. Written approval remains far safer.",
            },
        ],
        "keywords": ["epc", "construction contract", "delay", "extension of time", "variation", "escalation", "retention", "fidic", "claim", "liquidated damages", "defect liability"],
    },
    {
        "id": "ppp-projects",
        "category": "infrastructure",
        "title": "Public Private Partnership (PPP) Models",
        "summary": (
            "PPP is how a government builds a highway or an airport without paying the entire "
            "cost upfront: a private concessionaire finances and builds it and recovers money "
            "over decades through tolls or annuity payments. The whole arrangement lives inside "
            "one long document called a concession agreement."
        ),
        "key_points": [
            "BOT-Toll - the concessionaire builds and recovers through user charges, taking traffic risk.",
            "BOT-Annuity - the authority pays fixed semi-annual annuities, so the private party takes no traffic risk.",
            "Hybrid Annuity Model - the authority funds 40 per cent during construction and pays the rest as annuities, sharing the risk.",
            "EPC - the authority pays the full cost and owns the asset; there is no concession.",
            "The concession agreement allocates risk: land, approvals and change in law usually sit with the authority; construction, cost overrun and operations with the concessionaire.",
            "Termination payments differ sharply depending on whether termination is for authority default, concessionaire default or force majeure.",
            "Viability Gap Funding is a capital grant of up to 20 per cent given by the government to make socially necessary but commercially weak projects bankable.",
        ],
        "laws": [
            "Concession agreements based on Model Concession Agreements issued by NITI Aayog and sectoral ministries",
            "National Highways Act, 1956 for road projects",
            "Arbitration and Conciliation Act, 1996 for dispute resolution",
            "Electricity Act, 2003 for power sector PPPs",
        ],
        "steps": [
            "Study the model concession agreement for the sector before bidding.",
            "Assess the conditions precedent - land handover percentage, approvals, financial close deadlines.",
            "Model the revenue and stress-test traffic or demand assumptions.",
            "Negotiate or price the risks the authority is transferring, especially change in law and force majeure.",
            "Achieve financial close within the contractual window; failure carries a heavy penalty.",
            "Track milestones and issue notices for authority delay - claims here are contractual and time-barred by the notice clauses.",
        ],
        "faqs": [
            {
                "q": "Who owns a PPP asset?",
                "a": "The government usually retains ownership of the land and the asset; the concessionaire only has the right to build, operate and collect revenue for the concession period, after which it transfers back.",
            },
        ],
        "keywords": ["ppp", "bot", "hybrid annuity", "concession agreement", "viability gap funding", "infrastructure", "toll", "annuity", "nhai", "financial close"],
    },
    {
        "id": "land-acquisition",
        "category": "infrastructure",
        "title": "Land Acquisition, Compensation and Rehabilitation",
        "summary": (
            "The State can compulsorily take private land for a public purpose, but the 2013 Act "
            "replaced the colonial law with a far more demanding process: a social impact "
            "assessment, consent requirements for private projects, market-linked compensation "
            "and a rehabilitation package."
        ),
        "key_points": [
            "Compensation is computed as the higher of the market value benchmarks, multiplied by a factor of 1 in urban and up to 2 in rural areas, plus 100 per cent solatium.",
            "Consent of 80 per cent of affected families is needed for a private project, and 70 per cent for a PPP project; no consent is needed for a pure government project.",
            "A Social Impact Assessment must be completed within six months and appraised by an expert group before the acquisition proceeds.",
            "Rehabilitation and Resettlement entitlements include housing, a job or annuity, transportation and subsistence allowances.",
            "Acquisition lapses if the award was made five years or more before the Act came into force and possession was not taken or compensation not paid.",
            "The urgency clause is limited mainly to defence, national security and natural disasters.",
            "Disputes on compensation go to the Land Acquisition, Rehabilitation and Resettlement Authority, with appeal to the High Court.",
        ],
        "laws": [
            "Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013",
            "Constitution - Article 300A, the constitutional right to property",
            "National Highways Act, 1956 (a separate acquisition mechanism for highways)",
        ],
        "steps": [
            "Read the Section 4 preliminary notification carefully and note the deadline for objections.",
            "File written objections within the statutory period and appear at the personal hearing.",
            "Collect evidence of value - recent registered sale deeds of comparable land, valuation reports, details of trees, wells and structures.",
            "Participate in the Social Impact Assessment public hearing and record your concerns.",
            "Accept compensation under protest if you intend to contest it, otherwise you may be treated as having accepted.",
            "File a reference for enhancement of compensation before the Authority within the limitation period.",
        ],
        "faqs": [
            {
                "q": "Is the right to property still a Fundamental Right?",
                "a": "No. The 44th Amendment made it a constitutional legal right under Article 300A. The State can still take property only by authority of law and on payment of compensation.",
            },
        ],
        "keywords": ["land acquisition", "compensation", "rehabilitation", "solatium", "social impact assessment", "2013 act", "300a", "consent", "resettlement"],
    },

    # ==================================================================
    # ENVIRONMENTAL LAW
    # ==================================================================
    {
        "id": "pollution-control",
        "category": "environment",
        "title": "Pollution Control - Consents, Standards and the NGT",
        "summary": (
            "Any industry that discharges effluent or emits into the air needs two permissions "
            "from the State Pollution Control Board before it can even start. Enforcement now "
            "runs largely through the National Green Tribunal, which can be approached cheaply "
            "and decides environmental disputes within months."
        ),
        "key_points": [
            "Consent to Establish is needed before construction; Consent to Operate before production begins, and both must be renewed.",
            "Industries are colour-coded red, orange, green and white by pollution potential, which decides the frequency of renewal and inspection.",
            "The Boards can issue directions to stop water and electricity supply and to close a polluting unit.",
            "The Polluter Pays Principle makes the polluter bear the cost of remediation and compensation, regardless of fault.",
            "The Precautionary Principle allows action to prevent environmental harm even where scientific certainty is incomplete.",
            "The NGT has jurisdiction over civil cases arising from seven environmental statutes and must decide within six months.",
            "Noise standards differ by zone and time - industrial, commercial, residential and silence zones - and are commonly enforced through the police and the Boards.",
        ],
        "laws": [
            "Water (Prevention and Control of Pollution) Act, 1974",
            "Air (Prevention and Control of Pollution) Act, 1981",
            "Environment (Protection) Act, 1986 and the rules on hazardous waste, plastic waste, e-waste and noise",
            "National Green Tribunal Act, 2010",
            "M.C. Mehta v. Union of India line of cases",
        ],
        "steps": [
            "Classify the activity and find its category in the Board's colour-coded list.",
            "Apply online for Consent to Establish with the project report, layout and effluent details.",
            "Install the pollution control equipment and apply for Consent to Operate.",
            "Maintain monitoring records and file the annual environmental statement.",
            "To complain about a polluter, write to the State Pollution Control Board with photographs and location.",
            "If the Board does not act, file an application before the NGT - the fee is nominal and an individual can appear.",
        ],
        "faqs": [
            {
                "q": "Can an individual approach the NGT?",
                "a": "Yes. Any person aggrieved, including a resident affected by pollution, can file an application. The filing fee is small and legal representation is not compulsory.",
            },
        ],
        "keywords": ["pollution", "consent to operate", "ngt", "pollution control board", "polluter pays", "precautionary principle", "air act", "water act", "noise", "environment"],
    },
    {
        "id": "environmental-clearance",
        "category": "environment",
        "title": "Environmental Impact Assessment and Clearance",
        "summary": (
            "Large projects - mines, highways, thermal plants, big buildings - cannot start "
            "without prior Environmental Clearance. The process is designed so that the "
            "environmental cost is studied and the affected public is heard before, not after, "
            "the investment decision."
        ),
        "key_points": [
            "Projects are listed in a Schedule and divided into Category A, cleared by the Centre, and Category B, cleared by the State authority.",
            "The four stages are screening, scoping, public consultation and appraisal.",
            "Terms of Reference are issued at the scoping stage and define what the EIA study must cover.",
            "Public consultation includes a public hearing at the site and written responses from other stakeholders; some categories are exempt.",
            "Clearance comes with binding conditions, and half-yearly compliance reports must be filed.",
            "Starting work before clearance is a violation; post-facto clearance has been repeatedly criticised by courts.",
            "Coastal projects need clearance under the Coastal Regulation Zone Notification, and forest land needs separate approval under the Forest Conservation Act.",
        ],
        "laws": [
            "Environment (Protection) Act, 1986 and the EIA Notification, 2006 as amended",
            "Forest (Conservation) Act, 1980",
            "Coastal Regulation Zone Notification",
            "Wildlife (Protection) Act, 1972 for projects near protected areas",
        ],
        "steps": [
            "Check the EIA Schedule to identify the category and the threshold your project crosses.",
            "File Form 1 with the pre-feasibility report on the PARIVESH portal.",
            "Obtain the Terms of Reference and commission an accredited consultant to do the EIA study.",
            "Publish and conduct the public hearing through the State Pollution Control Board.",
            "Submit the final EIA and Environment Management Plan for appraisal by the Expert Appraisal Committee.",
            "After clearance, comply with conditions and upload half-yearly compliance reports.",
        ],
        "faqs": [
            {
                "q": "Can a citizen object to a project's clearance?",
                "a": "Yes, at the public hearing and in writing during consultation. After clearance is granted, an appeal lies to the National Green Tribunal within 30 days.",
            },
        ],
        "keywords": ["eia", "environmental clearance", "public hearing", "parivesh", "forest clearance", "crz", "terms of reference", "expert appraisal committee"],
    },
    {
        "id": "waste-management",
        "category": "environment",
        "title": "Waste Management and Extended Producer Responsibility",
        "summary": (
            "India regulates waste through a family of rules, each covering one waste stream. The "
            "common thread is Extended Producer Responsibility: whoever puts a product into the "
            "market is responsible for collecting it back at the end of its life."
        ),
        "key_points": [
            "Solid Waste Management Rules require segregation at source into wet, dry and domestic hazardous waste.",
            "Plastic Waste Management Rules ban identified single-use plastics and impose EPR targets on producers, importers and brand owners.",
            "E-Waste Rules make producers responsible for collecting a percentage of what they sold in earlier years.",
            "Hazardous and Other Wastes Rules regulate storage, transport with manifests, and disposal only at authorised facilities.",
            "Bio-Medical Waste Rules require colour-coded segregation by hospitals and clinics and treatment at common facilities.",
            "Construction and Demolition Waste Rules require large generators to submit a waste management plan.",
            "EPR is tracked through registration and credit certificates on a central online portal, with penalties for shortfall.",
        ],
        "laws": [
            "Environment (Protection) Act, 1986 as the parent statute",
            "Solid Waste Management Rules, 2016",
            "Plastic Waste Management Rules, 2016 and EPR Guidelines, 2022",
            "E-Waste (Management) Rules, 2022",
            "Bio-Medical Waste Management Rules, 2016",
        ],
        "steps": [
            "Identify which waste streams your activity generates.",
            "Register as a producer, importer, brand owner or recycler on the applicable EPR portal.",
            "Set annual collection and recycling targets and tie up with authorised recyclers.",
            "Keep manifests and records of every consignment handed to a transporter or recycler.",
            "File the annual returns to the Pollution Control Board within the deadline.",
            "For a citizen complaint about illegal dumping or burning, report to the municipal body and the Board, and escalate to the NGT.",
        ],
        "faqs": [
            {
                "q": "Is burning garbage illegal?",
                "a": "Yes. Open burning of waste, including leaves and plastic, is prohibited under the waste rules and attracts environmental compensation fixed by the Boards and the NGT.",
            },
        ],
        "keywords": ["waste management", "epr", "plastic waste", "e-waste", "hazardous waste", "biomedical waste", "segregation", "recycler", "single use plastic"],
    },
    {
        "id": "forest-wildlife",
        "category": "environment",
        "title": "Forests, Wildlife and Community Rights",
        "summary": (
            "Forest law does two things at once: it restricts the diversion of forest land for "
            "non-forest use, and it recognises the rights of the forest-dwelling communities who "
            "have lived there for generations. Wildlife law adds a strict prohibition on hunting "
            "and trade in protected species."
        ),
        "key_points": [
            "No forest land can be used for a non-forest purpose without prior approval of the Central Government.",
            "Compensatory afforestation and the net present value of the diverted forest must be paid by the user agency.",
            "The Forest Rights Act recognises individual rights to cultivate, and community rights to collect and manage minor forest produce.",
            "The Gram Sabha's consent is required before forest land where such rights exist is diverted.",
            "The Wildlife Protection Act lists species in schedules by protection level, with the strictest protection for Schedule I animals.",
            "Hunting, possession and trade in protected wildlife and their derivatives are offences with imprisonment and heavy fines.",
            "National Parks, Wildlife Sanctuaries, Conservation Reserves and Eco-Sensitive Zones each carry different levels of restriction on activity.",
        ],
        "laws": [
            "Forest (Conservation) Act, 1980 as amended",
            "Indian Forest Act, 1927",
            "Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act, 2006",
            "Wildlife (Protection) Act, 1972",
            "Biological Diversity Act, 2002",
        ],
        "steps": [
            "Check whether the land is recorded as forest in the revenue or forest records - the definition is wide and includes deemed forests.",
            "For diversion, apply through the state to the Central Government with a compensatory afforestation plan.",
            "Obtain the Gram Sabha resolution certifying that forest rights have been settled.",
            "For a wildlife offence, report to the Forest Department; forest officers have powers of search, seizure and arrest.",
            "Communities claiming forest rights should file claims before the Forest Rights Committee with evidence of long occupation.",
        ],
        "faqs": [
            {
                "q": "Can I keep an injured wild bird at home?",
                "a": "No. Possession of a protected species, even with good intentions, is an offence. Hand it to the Forest Department or a recognised rescue centre.",
            },
        ],
        "keywords": ["forest", "wildlife", "forest rights act", "gram sabha", "compensatory afforestation", "sanctuary", "national park", "schedule i", "eco sensitive zone"],
    },

    # ==================================================================
    # CONSUMER PROTECTION
    # ==================================================================
    {
        "id": "consumer-complaint",
        "category": "consumer",
        "title": "Filing a Consumer Complaint",
        "summary": (
            "The consumer forum is the friendliest court in India: low fees, no compulsory "
            "lawyer, complaint can be filed online, and you can sue where you live rather than "
            "where the company sits. It is the correct first stop for a defective product, a "
            "deficient service or an unfair trade practice."
        ),
        "key_points": [
            "A consumer is a person who buys goods or hires services for consideration - but not for resale or commercial purpose, unless for self-employment.",
            "Three tiers by value: District Commission up to Rs 50 lakh, State Commission up to Rs 2 crore, National Commission above Rs 2 crore.",
            "The complaint must be filed within two years of the cause of action, with delay condonable for sufficient cause.",
            "You can file where you reside or work, which was a major improvement introduced in 2019.",
            "Reliefs available: removal of defect, replacement, refund, compensation for loss and mental agony, discontinuation of unfair practice, and punitive damages.",
            "Product liability lets you sue the manufacturer, the seller and the service provider for harm caused by a defective product.",
            "Misleading advertisements can attract penalties on the manufacturer and even on the endorser.",
        ],
        "laws": [
            "Consumer Protection Act, 2019 - Sections 2(7) (consumer), 34, 47, 58 (jurisdiction), 35 (complaint), 69 (limitation), 82-87 (product liability)",
            "Consumer Protection (E-Commerce) Rules, 2020",
            "Central Consumer Protection Authority guidelines on misleading advertisements and dark patterns",
        ],
        "steps": [
            "Collect the invoice, warranty card, packaging, photographs of the defect and all correspondence.",
            "Complain to the company's customer care and to the National Consumer Helpline 1915, and note the ticket numbers.",
            "Send a legal notice giving 15 days to resolve.",
            "Draft the complaint with facts, the deficiency, the relief claimed and an affidavit; attach all documents.",
            "File online on the e-Daakhil portal or physically in the correct Commission with the prescribed fee.",
            "Attend hearings; you may appear yourself without an advocate.",
        ],
        "faqs": [
            {
                "q": "Can I claim compensation for mental agony?",
                "a": "Yes. Consumer Commissions regularly award compensation for harassment and mental agony in addition to refund or replacement, along with litigation costs.",
            },
            {
                "q": "Can I file a consumer case against an online seller in another city?",
                "a": "Yes. Under the 2019 Act you may file where you reside or work, and e-commerce rules require the platform to disclose the seller's details for service of notice.",
            },
        ],
        "keywords": ["consumer", "complaint", "defective", "deficiency in service", "refund", "e-daakhil", "district commission", "1915", "compensation", "unfair trade practice"],
    },
    {
        "id": "ecommerce-consumer",
        "category": "consumer",
        "title": "E-Commerce, Returns and Misleading Advertisements",
        "summary": (
            "Online shopping created problems the old law never imagined: sellers who cannot be "
            "traced, prices that change while you watch, fake reviews and design tricks that push "
            "you into buying. The 2020 e-commerce rules and the CCPA guidelines address each of "
            "these directly."
        ),
        "key_points": [
            "Marketplaces must display the seller's legal name, address, customer care contact and country of origin.",
            "No platform may manipulate prices to make an unreasonable profit, or discriminate between consumers of the same class.",
            "Cancellation charges cannot be imposed on a consumer unless the platform bears similar charges when it cancels.",
            "Every platform must appoint a Grievance Officer who acknowledges within 48 hours and resolves within one month.",
            "Fake or paid reviews presented as genuine consumer reviews are an unfair trade practice.",
            "Thirteen dark patterns are specifically prohibited, including false urgency, basket sneaking, confirm shaming, forced action and subscription traps.",
            "The CCPA can order the withdrawal of a misleading advertisement and impose penalties on the manufacturer and the endorser.",
        ],
        "laws": [
            "Consumer Protection Act, 2019",
            "Consumer Protection (E-Commerce) Rules, 2020",
            "Guidelines for Prevention and Regulation of Dark Patterns, 2023",
            "Guidelines for Prevention of Misleading Advertisements and Endorsements, 2022",
        ],
        "steps": [
            "Screenshot the product page, the price, the offer terms and the delivery promise at the time of ordering.",
            "Raise the complaint within the platform and note the ticket number and timestamps.",
            "Escalate to the platform's Grievance Officer in writing.",
            "Register the complaint on the National Consumer Helpline or the INGRAM portal.",
            "For misleading advertisements or dark patterns, complain to the Central Consumer Protection Authority.",
            "If unresolved, file a consumer complaint on e-Daakhil against the platform and the seller together.",
        ],
        "faqs": [
            {
                "q": "The seller refuses a return even though the site promised one. What can I do?",
                "a": "The advertised return policy is part of the contract. Preserve the screenshot, escalate to the Grievance Officer, and file a consumer complaint claiming refund plus compensation.",
            },
        ],
        "keywords": ["ecommerce", "online shopping", "return policy", "refund", "dark patterns", "misleading advertisement", "ccpa", "fake reviews", "marketplace", "grievance officer"],
    },
    {
        "id": "insurance-claims",
        "category": "consumer",
        "title": "Insurance Claims and Rejections",
        "summary": (
            "Insurance disputes usually turn on two things: whether something was disclosed when "
            "the policy was taken, and whether the claim falls inside an exclusion. Knowing that "
            "an insurer must prove a suppression was both deliberate and material shifts many "
            "rejected claims back in the policyholder's favour."
        ),
        "key_points": [
            "Insurance is a contract of utmost good faith, so material facts must be disclosed honestly in the proposal form.",
            "After three years, a life insurance policy cannot be repudiated on the ground of misstatement, except for proven fraud.",
            "Rejection must be in writing with reasons; a bare rejection without reasons is itself a deficiency in service.",
            "Exclusions must be specifically brought to the notice of the insured - a clause buried in fine print not supplied to the insured is often not enforced.",
            "Health policies have waiting periods for pre-existing diseases, and specified sub-limits for room rent that reduce payouts.",
            "Third-party motor insurance is compulsory and unlimited in amount; own-damage cover is optional.",
            "The Insurance Ombudsman handles complaints up to a prescribed value free of cost, and the consumer forum is an alternative.",
        ],
        "laws": [
            "Insurance Act, 1938 - Section 45 on repudiation of life policies",
            "IRDAI (Protection of Policyholders' Interests) Regulations",
            "Consumer Protection Act, 2019",
            "Motor Vehicles Act, 1988 - compulsory third-party insurance",
        ],
        "steps": [
            "Inform the insurer immediately and within the time stated in the policy.",
            "Submit the claim form with all documents - bills, discharge summary, FIR or surveyor report as applicable.",
            "Ask for the rejection in writing with the exact clause relied on.",
            "Send a written representation to the insurer's grievance cell and then to IRDAI's Bima Bharosa portal.",
            "Approach the Insurance Ombudsman within one year of the rejection - the process is free.",
            "Alternatively, or afterwards, file a consumer complaint claiming the sum plus interest and compensation.",
        ],
        "faqs": [
            {
                "q": "My health claim was rejected for a pre-existing disease I did not know about. Is that valid?",
                "a": "Non-disclosure must be of a fact you actually knew and that was material. Courts and Ombudsmen have repeatedly set aside rejections based on conditions the insured was never diagnosed with.",
            },
        ],
        "keywords": ["insurance", "claim rejection", "policy", "irdai", "ombudsman", "pre-existing disease", "repudiation", "health insurance", "utmost good faith", "section 45"],
    },
    {
        "id": "medical-negligence-consumer",
        "category": "consumer",
        "title": "Service Deficiency - Banks, Telecom, Airlines and Builders",
        "summary": (
            "'Deficiency in service' is a deliberately wide phrase, and it covers almost every "
            "organised service you pay for. The same forum that handles a faulty phone handles a "
            "bank's wrong debit, an airline's lost baggage and a builder's delayed flat."
        ),
        "key_points": [
            "Banking: unauthorised electronic transactions reported promptly attract zero or limited customer liability under RBI rules; the burden is on the bank to prove customer negligence.",
            "Telecom: billing disputes and service outages are deficiencies, though pure tariff matters lie with TRAI.",
            "Airlines: DGCA rules fix compensation for denied boarding, cancellation and long delay, and separate limits apply for lost or damaged baggage.",
            "Real estate: delayed possession, reduced carpet area and false amenities are all actionable, with RERA as a parallel remedy.",
            "Education: coaching institutes refusing refunds of fees have repeatedly been held liable, though core academic decisions of universities are outside consumer jurisdiction.",
            "Electricity and municipal services: billing errors and wrongful disconnection are covered, subject to statutory forums under the Electricity Act.",
            "Keep in mind the difference between a regulator's jurisdiction and the consumer forum's - many complaints can go to both.",
        ],
        "laws": [
            "Consumer Protection Act, 2019 - Section 2(11) deficiency in service",
            "RBI circulars on limiting customer liability in unauthorised electronic transactions",
            "DGCA Civil Aviation Requirements on passenger rights",
            "Real Estate (Regulation and Development) Act, 2016",
        ],
        "steps": [
            "Identify the exact promised standard - the tariff, the schedule, the agreement, the RBI or DGCA rule.",
            "Report immediately through the official channel and keep the reference number.",
            "Escalate to the internal ombudsman or nodal officer of the service provider.",
            "Approach the sectoral regulator's grievance system - RBI Ombudsman, TRAI, DGCA, IRDAI.",
            "File a consumer complaint if unresolved, claiming refund, compensation and costs.",
        ],
        "faqs": [
            {
                "q": "Money was debited from my account by fraud. Who bears the loss?",
                "a": "Under RBI's limited liability framework, if you report the unauthorised transaction promptly and the fraud was not due to your negligence, the bank generally has to restore the amount.",
            },
        ],
        "keywords": ["deficiency in service", "bank", "telecom", "airline", "flight delay", "baggage", "rbi ombudsman", "electricity", "coaching refund", "unauthorised transaction"],
    },

    # ==================================================================
    # TAXATION
    # ==================================================================
    {
        "id": "income-tax-basics",
        "category": "taxation",
        "title": "Income Tax - Heads of Income, Returns and Regimes",
        "summary": (
            "Income tax is charged on total income computed under five heads, after deductions "
            "and set-offs. Since the introduction of a second, lower-rate regime with fewer "
            "deductions, the practical question for most individuals is which of the two regimes "
            "costs less for their particular mix of income and investments."
        ),
        "key_points": [
            "Five heads: Salary, House Property, Profits and Gains of Business or Profession, Capital Gains, and Income from Other Sources.",
            "The old regime allows deductions like 80C, 80D, HRA and home loan interest; the new regime has lower slab rates but very few deductions.",
            "Residential status decides scope - a resident is taxed on global income, a non-resident only on income received or accruing in India.",
            "Capital gains are short-term or long-term depending on the holding period, which differs for shares, property and other assets.",
            "TDS is tax deducted at source by the payer; it is credited to you and visible in Form 26AS and the Annual Information Statement.",
            "Advance tax is payable in instalments if the liability after TDS exceeds the threshold, and interest runs on shortfalls.",
            "A belated or revised return can be filed within the extended deadline, and an updated return within a longer period on payment of additional tax.",
        ],
        "laws": [
            "Income-tax Act, 1961 - Sections 2(7), 5, 14 (heads), 80C-80U (deductions), 115BAC (new regime), 139 (returns), 143 (assessment), 234A-C (interest)",
            "Annual Finance Acts that fix the rates",
        ],
        "steps": [
            "Collect Form 16, Form 16A, bank interest certificates, capital gains statements and proof of deductions.",
            "Reconcile everything against Form 26AS and the Annual Information Statement before filing.",
            "Compute tax under both regimes and choose the cheaper one - salaried taxpayers can switch each year.",
            "File the correct ITR form on the e-filing portal before the due date.",
            "E-verify within the prescribed days, otherwise the return is treated as never filed.",
            "Keep the acknowledgement and all supporting documents for at least six years.",
        ],
        "faqs": [
            {
                "q": "Do I need to file a return if my income is below the exemption limit?",
                "a": "Not always, but you must file if you meet certain triggers such as high value deposits, large electricity bills, foreign travel spending or foreign assets - and filing is anyway useful for visas and loans.",
            },
            {
                "q": "What happens if I miss the deadline?",
                "a": "You can file a belated return with a late fee and interest, but you lose the right to carry forward certain losses. An updated return is possible later with additional tax.",
            },
        ],
        "keywords": ["income tax", "itr", "tds", "26as", "new regime", "old regime", "80c", "capital gains", "advance tax", "efiling", "deduction"],
    },
    {
        "id": "gst-basics",
        "category": "taxation",
        "title": "GST - Registration, Returns and Input Tax Credit",
        "summary": (
            "GST replaced a tangle of central and state indirect taxes with one tax on supply, "
            "collected at every stage but with credit for tax already paid. The system runs "
            "entirely online, and the single biggest practical issue is the conditions attached "
            "to claiming input tax credit."
        ),
        "key_points": [
            "GST is destination-based: CGST plus SGST on an intra-state supply, IGST on an inter-state supply.",
            "Registration is mandatory above the turnover threshold, and compulsory regardless of turnover for inter-state supply of goods, e-commerce operators and certain other categories.",
            "The composition scheme offers a low flat rate for small taxpayers but bars them from collecting tax or claiming input credit.",
            "Input Tax Credit needs four conditions: a valid tax invoice, receipt of goods or services, the tax actually paid to the government by the supplier, and the return filed.",
            "Credit is blocked for specified items such as motor vehicles in most cases, food and beverages, club memberships and goods used for personal consumption.",
            "Core returns are GSTR-1 for outward supplies and GSTR-3B for summary and payment, with GSTR-2B as the auto-generated credit statement.",
            "An e-way bill is required for movement of goods above the notified value, and e-invoicing applies above prescribed turnover.",
        ],
        "laws": [
            "Central Goods and Services Tax Act, 2017 and the State GST Acts",
            "Integrated Goods and Services Tax Act, 2017",
            "CGST Rules, 2017 - Sections 16 (ITC conditions), 17(5) (blocked credits), 22 and 24 (registration), 39 (returns)",
        ],
        "steps": [
            "Check whether your turnover or activity triggers compulsory registration.",
            "Apply on the GST portal with PAN, proof of business place, bank details and photographs; complete Aadhaar authentication.",
            "Issue tax invoices in the prescribed format with GSTIN, HSN or SAC code and the correct rate.",
            "Reconcile purchases with GSTR-2B every month before claiming input credit.",
            "File GSTR-1 and GSTR-3B by their due dates and pay the tax; late fees and interest apply automatically.",
            "File the annual return and, above the prescribed turnover, the reconciliation statement.",
        ],
        "faqs": [
            {
                "q": "Can I claim input credit if my supplier did not pay the tax?",
                "a": "Generally no. Credit is available only when the supplier has declared the invoice and paid the tax, which is why reconciliation with GSTR-2B before payment matters.",
            },
            {
                "q": "Does a freelancer need GST registration?",
                "a": "Only if the turnover crosses the threshold for services, or if a compulsory-registration category applies. Exports of services need registration to claim refunds or supply under a bond.",
            },
        ],
        "keywords": ["gst", "input tax credit", "gstr-1", "gstr-3b", "registration", "composition scheme", "e-way bill", "igst", "cgst", "gstin", "2b"],
    },
    {
        "id": "tax-notices-appeals",
        "category": "taxation",
        "title": "Tax Notices, Assessment and Appeals",
        "summary": (
            "A tax notice is not an accusation; it is usually a request for information or an "
            "intimation of a mismatch. Each type has a different deadline and a different "
            "consequence for ignoring it, so the first task on receiving one is identifying which "
            "section it is issued under."
        ),
        "key_points": [
            "An intimation matching your return against the department's computation is the most common communication and often needs only a rectification.",
            "A defective return notice must be answered within the time given, or the return is treated as invalid.",
            "A scrutiny notice starts a detailed assessment; faceless assessment means the exchange is entirely online.",
            "A notice for income escaping assessment requires the department to first give you the information relied on and consider your reply.",
            "Demand notices require payment or an appeal within 30 days; recovery can otherwise begin.",
            "The appeal ladder is Commissioner (Appeals), then the Income Tax Appellate Tribunal, then the High Court on a substantial question of law, then the Supreme Court.",
            "For GST, the ladder is the Appellate Authority, then the Appellate Tribunal, and appeals require a pre-deposit of a percentage of the disputed tax.",
        ],
        "laws": [
            "Income-tax Act, 1961 - Sections 139(9), 143(1), 143(2), 147-151, 156, 246A, 253",
            "Central Goods and Services Tax Act, 2017 - Sections 73, 74, 107, 112",
            "Faceless Assessment and Faceless Appeal Schemes",
        ],
        "steps": [
            "Read the notice and note the section, the document identification number and the deadline.",
            "Verify it is genuine using the department's authenticate-notice utility - fake tax notices are a common fraud.",
            "Collect the documents specifically asked for; do not send extra material that opens new questions.",
            "File the response through the e-proceedings tab of the portal within the deadline, seeking an extension in writing if needed.",
            "If the order goes against you, file the appeal within 30 days with the prescribed fee and the grounds of appeal.",
            "Apply for stay of demand while the appeal is pending, usually on paying a part of the demand.",
        ],
        "faqs": [
            {
                "q": "What if I simply ignore a tax notice?",
                "a": "The assessment proceeds ex-parte on the department's estimate, penalties are levied, and recovery can attach your bank account. Responding on time is far cheaper than fixing it later.",
            },
        ],
        "keywords": ["tax notice", "scrutiny", "143(1)", "148", "assessment", "appeal", "cit appeals", "itat", "demand", "faceless", "rectification"],
    },
    {
        "id": "business-taxes",
        "category": "taxation",
        "title": "Business Taxation, TDS Duties and Presumptive Schemes",
        "summary": (
            "A business is not just a taxpayer, it is also a tax collector. It must deduct TDS on "
            "many payments, deposit it on time and file quarterly statements. Small businesses "
            "and professionals can escape most of this book-keeping through the presumptive "
            "taxation schemes."
        ),
        "key_points": [
            "TDS applies to salary, contractor payments, professional fees, rent, commission and several other payments above threshold limits.",
            "Deducted tax must be deposited by the 7th of the following month, and quarterly TDS returns must be filed, followed by issuing Form 16 or 16A.",
            "Failure to deduct or deposit attracts interest, a late filing fee per day, penalty, and disallowance of 30 per cent of the expense.",
            "Presumptive taxation for small businesses treats a fixed percentage of turnover as income, with a lower percentage for digital receipts.",
            "Professionals below the prescribed gross receipts can offer 50 per cent of receipts as income under the professional presumptive scheme.",
            "A tax audit is required when turnover or receipts exceed the prescribed limits, with a higher limit where cash transactions are minimal.",
            "Payments above the cash limit to a single person in a day are disallowed as expenditure, pushing businesses towards banking channels.",
        ],
        "laws": [
            "Income-tax Act, 1961 - Sections 40A(3), 44AA (books), 44AB (audit), 44AD and 44ADA (presumptive), 192-206 (TDS), 234E, 271H",
        ],
        "steps": [
            "Obtain a TAN before making any payment liable to TDS.",
            "Maintain a payment master showing the section, rate and threshold for each vendor type.",
            "Deposit TDS monthly by challan and file the quarterly statement.",
            "Issue TDS certificates to deductees within the prescribed time.",
            "Decide at the start of the year whether the presumptive scheme suits you, since opting out has a lock-in consequence.",
            "Get the tax audit done and the report filed before the due date if the limits are crossed.",
        ],
        "faqs": [
            {
                "q": "Does a freelancer have to deduct TDS?",
                "a": "An individual or HUF must deduct TDS on specified payments once their turnover crosses the audit threshold, and there is also a separate provision for large payments by any individual to a contractor or professional.",
            },
        ],
        "keywords": ["tds", "tan", "44ad", "44ada", "presumptive", "tax audit", "form 16", "business tax", "quarterly return", "40a(3)"],
    },

    # ==================================================================
    # BANKING AND INSOLVENCY
    # ==================================================================
    {
        "id": "loans-and-recovery",
        "category": "banking",
        "title": "Loans, Default and What a Bank Can Legally Do",
        "summary": (
            "A borrower in default is not without rights. Banks have powerful recovery tools - "
            "SARFAESI, DRT, arbitration - but each has a procedure, and recovery agents in "
            "particular are bound by strict RBI rules that prohibit harassment."
        ),
        "key_points": [
            "An account is classified as a Non-Performing Asset when interest or principal stays overdue for more than 90 days.",
            "Under SARFAESI, a secured creditor issues a 60-day demand notice, and if unpaid may take possession of the secured asset without going to court.",
            "The borrower can object to the notice, and the bank must reply with reasons; an appeal lies to the Debts Recovery Tribunal.",
            "SARFAESI does not apply to agricultural land, and applies only to secured debts above the notified minimum.",
            "Recovery agents cannot call outside 8 am to 7 pm, cannot use threats or abusive language, cannot contact your relatives to shame you, and must carry authorisation.",
            "The bank must return surplus sale proceeds to the borrower and must sell only after proper valuation and public notice.",
            "A borrower's credit score reflects defaults for years, and lenders must report corrections to credit bureaus within the prescribed time.",
        ],
        "laws": [
            "Securitisation and Reconstruction of Financial Assets and Enforcement of Security Interest Act, 2002 - Sections 13(2), 13(4), 17",
            "Recovery of Debts and Bankruptcy Act, 1993 - Debts Recovery Tribunals",
            "RBI Master Directions on outsourcing of financial services and recovery agents",
            "Credit Information Companies (Regulation) Act, 2005",
        ],
        "steps": [
            "Do not ignore the notices - every SARFAESI stage has a short deadline.",
            "Ask the bank in writing for the loan account statement and the computation of the demand.",
            "Negotiate a restructuring or a one-time settlement in writing before possession is taken.",
            "File objections under Section 13(3A) within the notice period, and a securitisation application before the DRT under Section 17 if action is taken.",
            "Report harassment by recovery agents in writing to the bank's nodal officer and then to the RBI Ombudsman, with call recordings.",
            "After settlement, obtain a no-dues certificate and confirm the credit bureau record is updated.",
        ],
        "faqs": [
            {
                "q": "Can a bank take my house without a court order?",
                "a": "Under SARFAESI a secured creditor can take possession of mortgaged property after the 60-day notice, but it needs the Magistrate's assistance for physical possession, and you can challenge the action before the DRT.",
            },
            {
                "q": "Is loan default a criminal offence?",
                "a": "No, ordinary default is a civil matter. It becomes criminal only where there is cheating, fraud, or a dishonoured cheque under Section 138.",
            },
        ],
        "keywords": ["loan", "default", "npa", "sarfaesi", "drt", "recovery agent", "possession", "one time settlement", "credit score", "harassment"],
    },
    {
        "id": "insolvency-ibc",
        "category": "banking",
        "title": "Insolvency and Bankruptcy Code - Corporate Insolvency",
        "summary": (
            "The IBC replaced a slow, scattered set of laws with a single time-bound process. Its "
            "central idea is a shift of control: the moment insolvency is admitted, management "
            "passes from the promoters to an insolvency professional supervised by the creditors."
        ),
        "key_points": [
            "A financial creditor, an operational creditor or the corporate debtor itself can apply to the NCLT once the default crosses the threshold.",
            "On admission, a moratorium freezes all suits, recovery and enforcement against the company.",
            "An Interim Resolution Professional takes over management and constitutes the Committee of Creditors from financial creditors.",
            "The Committee decides by a 66 per cent voting share on a resolution plan; a plan that is approved binds all stakeholders including dissenters.",
            "The process must be completed in 180 days, extendable by 90, with an outer limit of 330 days including litigation.",
            "If no plan is approved, the company goes into liquidation and the waterfall in Section 53 decides who gets paid in what order.",
            "Pre-packaged insolvency is available for MSMEs, allowing the existing management to stay while a plan is approved.",
        ],
        "laws": [
            "Insolvency and Bankruptcy Code, 2016 - Sections 7, 9, 10 (initiation), 14 (moratorium), 30 and 31 (resolution plan), 53 (liquidation waterfall), 29A (ineligible persons)",
            "IBBI regulations on the corporate insolvency resolution process",
            "Swiss Ribbons v. Union of India (2019) - constitutional validity upheld",
        ],
        "steps": [
            "Establish the debt and the default with records - invoices, agreements, statements, and the information utility record.",
            "For an operational creditor, first serve a demand notice and wait 10 days for a dispute or payment.",
            "File the application before the NCLT in the prescribed form with the fee and proposed professional.",
            "After admission, file your claim with the Interim Resolution Professional within the public announcement deadline.",
            "Participate in the Committee of Creditors if you are a financial creditor.",
            "Vote on the resolution plan, or await distribution under the liquidation waterfall.",
        ],
        "faqs": [
            {
                "q": "Where do employees stand in insolvency?",
                "a": "Workmen's dues for 24 months rank very high in the liquidation waterfall, alongside secured creditors who gave up their security, and other employees' dues for 12 months come next.",
            },
        ],
        "keywords": ["ibc", "insolvency", "nclt", "moratorium", "committee of creditors", "resolution plan", "liquidation", "corporate debtor", "operational creditor", "29a"],
    },
    {
        "id": "banking-customer-rights",
        "category": "banking",
        "title": "Banking Customer Rights and the RBI Ombudsman",
        "summary": (
            "The RBI's Charter of Customer Rights gives bank customers five basic entitlements, "
            "and the Integrated Ombudsman Scheme gives them one free, single window to enforce "
            "those entitlements against any bank, NBFC or payment system participant."
        ),
        "key_points": [
            "The five rights: fair treatment, transparency and honest dealing, suitability, privacy, and grievance redress and compensation.",
            "Banks must not levy charges that were not disclosed, and must give prior notice of changes in charges.",
            "Zero-balance basic savings accounts must be offered, and a bank cannot refuse to open one for lack of a minimum balance.",
            "For unauthorised electronic transactions, customer liability is zero if the fault is the bank's or a third party's and the customer reports promptly.",
            "A complaint must first be made to the bank; the Ombudsman can be approached after 30 days without a reply or on rejection.",
            "The Ombudsman process is free, online through the CMS portal, and can award compensation for loss and for mental agony.",
            "Nomination in every account and locker avoids painful succession disputes later.",
        ],
        "laws": [
            "Reserve Bank - Integrated Ombudsman Scheme, 2021",
            "RBI Charter of Customer Rights",
            "RBI circular on limiting liability of customers in unauthorised electronic banking transactions",
            "Banking Regulation Act, 1949",
        ],
        "steps": [
            "Complain in writing to the branch and obtain a complaint reference number.",
            "Escalate to the bank's Principal Nodal Officer if unresolved.",
            "After 30 days or on rejection, file with the RBI Ombudsman on the CMS portal - no fee, no lawyer required.",
            "Provide the complaint trail, statements and evidence of loss.",
            "If the Ombudsman's award does not satisfy you, an appeal lies to the Appellate Authority within 30 days.",
            "The consumer forum remains an alternative route for compensation.",
        ],
        "faqs": [
            {
                "q": "Can a bank deduct charges without telling me?",
                "a": "No. Charges must be disclosed in the schedule of charges and notified in advance. Undisclosed deductions can be reversed through the grievance process or the Ombudsman.",
            },
        ],
        "keywords": ["banking", "rbi ombudsman", "customer rights", "unauthorised transaction", "charges", "cms portal", "nodal officer", "nomination", "complaint"],
    },
    {
        "id": "securities-market",
        "category": "banking",
        "title": "Securities Market, SEBI and Investor Protection",
        "summary": (
            "SEBI regulates everything to do with buying and selling securities: how companies "
            "raise money from the public, how brokers behave, and what counts as insider trading "
            "or market manipulation. For an ordinary investor, its most useful creation is the "
            "SCORES grievance system."
        ),
        "key_points": [
            "A company raising money from the public must file a prospectus containing all material disclosures; misstatements attract civil and criminal liability.",
            "Insider trading - dealing on unpublished price sensitive information - is prohibited, and companies must maintain a structured digital database of who received such information.",
            "Listed companies must make continuous disclosures of material events and quarterly results.",
            "Fraudulent and unfair trade practices such as pump-and-dump, front running and circular trading are prohibited.",
            "SEBI can pass ex-parte interim orders, disgorge unlawful gains, bar persons from the market and levy monetary penalties.",
            "Unregistered investment advisers and guaranteed-return schemes on social media are a major current risk area for retail investors.",
            "Investor grievances can be filed on the SCORES portal, and disputes with brokers go to the exchange's arbitration mechanism or the online dispute resolution portal.",
        ],
        "laws": [
            "Securities and Exchange Board of India Act, 1992",
            "SEBI (Prohibition of Insider Trading) Regulations, 2015",
            "SEBI (Prohibition of Fraudulent and Unfair Trade Practices) Regulations, 2003",
            "SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015",
            "Companies Act, 2013 - prospectus and public offer provisions",
        ],
        "steps": [
            "Verify that the adviser, broker or scheme is registered with SEBI before investing.",
            "Read the offer document, especially the risk factors and the object of the issue.",
            "Keep contract notes, ledger statements and the demat holding statement.",
            "Complain to the intermediary first and note the reference number.",
            "Escalate to SCORES, and use the exchange's online dispute resolution or arbitration for broker disputes.",
            "Report suspected fraud, tip circulation or guaranteed-return schemes to SEBI directly.",
        ],
        "faqs": [
            {
                "q": "Are stock tips on social media legal?",
                "a": "Giving investment advice for consideration without SEBI registration is illegal, and coordinated tip-and-dump schemes are market manipulation. SEBI has penalised several such operators.",
            },
        ],
        "keywords": ["sebi", "securities", "insider trading", "ipo", "prospectus", "scores", "investor protection", "broker", "market manipulation", "disclosure"],
    },

    # ==================================================================
    # MOTOR VEHICLES
    # ==================================================================
    {
        "id": "accident-compensation",
        "category": "motor",
        "title": "Road Accident Compensation and MACT Claims",
        "summary": (
            "A road accident victim does not have to prove anything complicated to get "
            "compensation. Two routes exist: a fault-based claim before the Motor Accident Claims "
            "Tribunal where negligence is proved, and a no-fault structured route that pays a "
            "fixed sum quickly without proving fault at all."
        ),
        "key_points": [
            "The claim is filed before the MACT where the accident happened, where the claimant resides, or where the respondent resides.",
            "Compensation for death is computed from the deceased's income, adding future prospects, deducting personal expenses, and multiplying by an age-based multiplier.",
            "Conventional heads - loss of estate, loss of consortium and funeral expenses - are added on top.",
            "In injury cases, compensation covers medical expenses, loss of earning during treatment, permanent disability, pain and suffering, and future medical care.",
            "There is no limitation period for filing a MACT claim, though early filing is far better for evidence.",
            "The insurer pays on behalf of the owner in third-party claims; the insurer can recover from the owner if there was a fundamental breach such as driving without a valid licence.",
            "Hit-and-run victims can claim a fixed compensation from the government scheme, and the law protects good samaritans who take victims to hospital from harassment.",
        ],
        "laws": [
            "Motor Vehicles Act, 1988 as amended in 2019 - Sections 140 and 163A (no-fault), 166 (fault-based claim), 164 (fixed compensation), 161 (hit and run)",
            "Sarla Verma v. DTC (2009) and National Insurance v. Pranay Sethi (2017) - computation of compensation",
            "Good Samaritan guidelines",
        ],
        "steps": [
            "Ensure the injured get medical help first - a good samaritan cannot be forced to give personal details.",
            "Ensure an FIR or an accident information report is registered and get a copy.",
            "Collect the charge sheet, the injury or post-mortem report, medical bills, salary proof and the vehicle and insurance particulars.",
            "File the claim petition before the MACT with the documents and the details of the offending vehicle.",
            "Attend the hearings; the Tribunal follows a summary procedure and can award interim compensation.",
            "On award, the insurer deposits the amount, often partly in fixed deposit for minors and illiterate claimants.",
        ],
        "faqs": [
            {
                "q": "What if the offending vehicle was uninsured?",
                "a": "The award is then enforced against the owner and driver personally, and their assets can be attached. For untraced vehicles, the hit-and-run compensation scheme applies.",
            },
            {
                "q": "Can I claim if I was partly at fault?",
                "a": "Yes. Compensation is reduced in proportion to your contributory negligence, but it is not denied altogether.",
            },
        ],
        "keywords": ["accident", "mact", "compensation", "motor vehicle", "insurance claim", "hit and run", "negligence", "multiplier", "good samaritan", "third party"],
    },
    {
        "id": "traffic-rules-challan",
        "category": "motor",
        "title": "Traffic Offences, Challans and Licences",
        "summary": (
            "The 2019 amendment sharply increased penalties for traffic offences and created "
            "electronic enforcement through cameras. Most disputes now involve e-challans issued "
            "without the driver being stopped, and there is a defined way to contest them."
        ),
        "key_points": [
            "Driving without a valid licence, without insurance, without a helmet or seat belt, and using a phone while driving are all separately punishable.",
            "Drunken driving carries imprisonment and fine, with higher punishment for a repeat offence, and the licence can be suspended.",
            "Juvenile offences make the guardian or vehicle owner liable, with registration cancellation and a bar on the juvenile obtaining a licence until 25.",
            "Over-speeding, dangerous driving and racing carry escalating penalties, and points-based licence action is being implemented.",
            "An e-challan can be paid online or contested before the traffic court; unpaid challans can lead to court summons and blocking of fitness or transfer of the vehicle.",
            "Documents can be produced in digital form through the official mobile app and are legally valid.",
            "Third-party insurance is compulsory; driving without it is an offence and leaves the owner personally liable for accident compensation.",
        ],
        "laws": [
            "Motor Vehicles Act, 1988 as amended by the Motor Vehicles (Amendment) Act, 2019 - Chapter XIII penalties",
            "Central Motor Vehicles Rules, 1989",
            "Information Technology Act, 2000 - validity of digital documents",
        ],
        "steps": [
            "Check pending challans on the official e-challan portal using the vehicle number.",
            "If the challan is correct, pay online and keep the receipt.",
            "To contest, use the portal's grievance option or appear before the designated traffic court on the date given.",
            "Gather proof - photographs showing the vehicle was elsewhere, a sale certificate if the vehicle was transferred, or evidence of a wrong number plate reading.",
            "For a licence suspension, apply to the licensing authority with the court order once the case ends.",
            "Always transfer the registration certificate promptly after selling a vehicle to avoid liability for the buyer's offences.",
        ],
        "faqs": [
            {
                "q": "I sold my bike but challans still come to me. What do I do?",
                "a": "Liability follows the registered owner. Complete the transfer of registration with the RTO, and produce the sale documents to contest challans issued after the sale date.",
            },
        ],
        "keywords": ["challan", "traffic", "licence", "drunk driving", "helmet", "e-challan", "penalty", "rto", "insurance", "over speeding"],
    },
    {
        "id": "vehicle-registration",
        "category": "motor",
        "title": "Vehicle Registration, Transfer and Fitness",
        "summary": (
            "Every vehicle must be registered, and every change - sale, address, hypothecation, "
            "state transfer - must be recorded with the RTO. Ignoring these formalities is what "
            "creates liability for accidents and challans long after a vehicle has been sold."
        ),
        "key_points": [
            "Registration is valid for 15 years for a private vehicle and is renewable in 5-year blocks after a fitness test.",
            "Transfer of ownership must be reported within 14 days by the transferor and 30 days by the transferee in the prescribed forms.",
            "Hypothecation is recorded when a vehicle is financed and must be removed with a no-objection certificate after the loan is repaid.",
            "Taking a vehicle to another state for more than 12 months requires a no-objection certificate and re-registration, with road tax adjustment.",
            "Commercial vehicles need a permit and periodic fitness certificate, and the rules on age limits are stricter.",
            "High Security Registration Plates are mandatory, and older vehicles have been required to retrofit them.",
            "End-of-life vehicles in specified categories must be scrapped at registered facilities, with incentives for voluntary scrapping.",
        ],
        "laws": [
            "Motor Vehicles Act, 1988 - Sections 39-65 on registration and transfer",
            "Central Motor Vehicles Rules, 1989",
            "Motor Vehicles (Registration and Functions of Vehicle Scrapping Facility) Rules, 2021",
        ],
        "steps": [
            "On sale, execute the sale agreement and Forms 29 and 30 and file them with the RTO.",
            "Obtain the acknowledgement and keep a copy of the buyer's ID and the delivery note.",
            "Confirm on the Parivahan portal after a few weeks that the ownership has actually changed.",
            "For a loan closure, collect Form 35 and the NOC from the financier and file for removal of hypothecation.",
            "For an inter-state move, obtain the NOC from the original RTO and apply for re-registration.",
            "Renew fitness and insurance before expiry - lapse in insurance is an offence and destroys accident cover.",
        ],
        "faqs": [
            {
                "q": "How long is a driving licence valid?",
                "a": "A private driving licence is generally valid for 20 years or until the age of 50, whichever is earlier, and is then renewed for shorter periods. Commercial licences are renewed more frequently.",
            },
        ],
        "keywords": ["registration", "rc transfer", "hypothecation", "noc", "fitness certificate", "hsrp", "parivahan", "form 29", "scrapping", "re-registration"],
    },
    {
        "id": "public-transport-law",
        "category": "motor",
        "title": "Public Transport, Aggregators and Passenger Rights",
        "summary": (
            "Cab aggregators, buses and now bike taxis sit between transport law and consumer "
            "law. The Motor Vehicle Aggregator Guidelines put concrete obligations on app-based "
            "platforms about surge pricing, driver background checks and passenger safety."
        ),
        "key_points": [
            "Aggregators need a licence from the state and must comply with the aggregator guidelines.",
            "Surge pricing is capped at a multiple of the base fare, and a minimum fare floor also applies.",
            "Cancellation fees are capped as a percentage of the fare for both driver and passenger cancellations.",
            "Drivers must undergo police verification, medical examination and induction training, and vehicles must carry a valid permit.",
            "Every vehicle must have a functioning emergency button linked to the state emergency response system, and the platform must have a 24x7 control room.",
            "Aggregators must share data with the state as prescribed and cannot store or misuse passenger location data beyond stated purposes.",
            "Deficiency by an aggregator - unsafe driver conduct, overcharging, refusal of ride - is actionable in the consumer forum in addition to transport department action.",
        ],
        "laws": [
            "Motor Vehicles Act, 1988 - Section 93 and the definition of aggregator",
            "Motor Vehicle Aggregator Guidelines issued by the Ministry of Road Transport and Highways",
            "State aggregator rules and taxi schemes",
            "Consumer Protection Act, 2019",
        ],
        "steps": [
            "Note the vehicle number, driver name and trip ID from the app before or during the trip.",
            "Use the in-app emergency button and share the ride with a contact.",
            "Raise a complaint in the app immediately, since it records trip data.",
            "Escalate to the aggregator's grievance officer in writing.",
            "Complain to the State Transport Department against the licence holder for safety violations.",
            "File a consumer complaint for overcharging, injury or deficient service, keeping the receipt and trip history.",
        ],
        "faqs": [
            {
                "q": "Can a driver refuse a ride after accepting it?",
                "a": "Repeated refusal after acceptance is a violation of the aggregator guidelines and the platform is required to act against the driver. Passengers should not be charged cancellation fees in such cases.",
            },
        ],
        "keywords": ["aggregator", "ola", "uber", "cab", "surge pricing", "passenger safety", "bike taxi", "permit", "emergency button", "transport"],
    },

    # ==================================================================
    # HUMAN RIGHTS AND INTERNATIONAL LAW
    # ==================================================================
    {
        "id": "human-rights-framework",
        "category": "humanrights",
        "title": "Human Rights - International Framework and Indian Commissions",
        "summary": (
            "Human rights operate at two levels. Internationally, the UDHR and the two Covenants "
            "set the standard that States accept by treaty. Domestically, India enforces them "
            "through Fundamental Rights and a network of statutory commissions that can "
            "investigate complaints and recommend compensation."
        ),
        "key_points": [
            "The Universal Declaration of Human Rights, 1948 is not a treaty but has become the moral foundation of modern human rights law.",
            "The ICCPR covers civil and political rights; the ICESCR covers economic, social and cultural rights. India has ratified both.",
            "The National Human Rights Commission can inquire into violations by public servants, visit jails, and recommend compensation and prosecution.",
            "State Human Rights Commissions have similar powers within a state, and separate commissions exist for women, children, SC/ST, minorities and persons with disabilities.",
            "NHRC recommendations are not directly binding, but non-compliance must be explained and can be challenged in court.",
            "Custodial death and torture must be reported to the NHRC within 24 hours, and videography of post-mortem is required.",
            "India is a party to the conventions against racial discrimination, discrimination against women, torture (signed), and the rights of the child and persons with disabilities.",
        ],
        "laws": [
            "Protection of Human Rights Act, 1993",
            "Universal Declaration of Human Rights, 1948",
            "International Covenant on Civil and Political Rights, 1966 and ICESCR, 1966",
            "Constitution of India - Part III and Part IV",
        ],
        "steps": [
            "Identify whether the violation is by a public servant or a private person - the Commissions deal mainly with the former.",
            "Draft a complaint stating the incident, date, place, the officials involved and the right violated.",
            "File it free of cost online with the NHRC or the relevant State Commission; there is no court fee.",
            "Provide supporting documents - medical reports, FIR copies, photographs, news reports.",
            "Follow up on the case number; the Commission may call for a report from the authority.",
            "Where the Commission's response is inadequate, file a writ petition in the High Court.",
        ],
        "faqs": [
            {
                "q": "Are NHRC orders binding?",
                "a": "They are recommendations, not decrees. But the authority must report the action taken, and courts frequently rely on NHRC findings, so they carry real practical weight.",
            },
        ],
        "keywords": ["human rights", "nhrc", "udhr", "iccpr", "custodial death", "commission", "torture", "complaint", "international", "protection of human rights act"],
    },
    {
        "id": "international-law-basics",
        "category": "humanrights",
        "title": "Public International Law - Sources, Treaties and Courts",
        "summary": (
            "International law binds States rather than individuals, and it has no world "
            "policeman. It works through consent - treaties States sign, and customs they follow "
            "out of a sense of legal obligation - and it is applied by courts such as the ICJ and "
            "the ICC."
        ),
        "key_points": [
            "Sources under Article 38 of the ICJ Statute: treaties, customary international law, general principles of law, and judicial decisions and writings as subsidiary means.",
            "Custom requires two elements - consistent State practice and opinio juris, the belief that the practice is legally required.",
            "Jus cogens norms, such as the prohibitions on genocide, slavery, torture and aggression, cannot be overridden by any treaty.",
            "The ICJ decides disputes between States that consent to its jurisdiction, and gives advisory opinions to UN organs.",
            "The ICC prosecutes individuals for genocide, crimes against humanity, war crimes and aggression, and works on the principle of complementarity to national courts.",
            "In India, treaties do not automatically become domestic law - Parliament must legislate under Article 253 to implement them.",
            "The UN Security Council can authorise sanctions and force; the General Assembly's resolutions are recommendatory but carry political weight.",
        ],
        "laws": [
            "Charter of the United Nations, 1945",
            "Statute of the International Court of Justice - Article 38",
            "Vienna Convention on the Law of Treaties, 1969",
            "Rome Statute of the International Criminal Court, 1998",
            "Constitution of India - Articles 51 and 253",
        ],
        "steps": [
            "Identify whether the question involves States, individuals, or an international organisation.",
            "Locate the governing treaty and check which States have ratified it and with what reservations.",
            "If there is no treaty, examine State practice and opinio juris for a customary rule.",
            "Check whether India has enacted implementing legislation, because Indian courts apply the domestic statute.",
            "For an academic analysis, cite the primary instruments and the leading ICJ or ICC decisions.",
        ],
        "faqs": [
            {
                "q": "Can an individual sue a country at the ICJ?",
                "a": "No. Only States can be parties in ICJ contentious cases. Individuals may petition human rights treaty bodies or regional human rights courts where those mechanisms apply.",
            },
        ],
        "keywords": ["international law", "treaty", "custom", "icj", "icc", "un charter", "jus cogens", "vienna convention", "article 253", "sovereignty"],
    },
    {
        "id": "refugee-migration-law",
        "category": "humanrights",
        "title": "Refugees, Asylum and Migration Law",
        "summary": (
            "A refugee is someone outside their country who cannot return because of a "
            "well-founded fear of persecution. India is not a party to the Refugee Convention "
            "and has no refugee statute, so it handles refugees through executive policy, the "
            "Foreigners Act and Article 21 protections applied by courts."
        ),
        "key_points": [
            "The 1951 Refugee Convention definition rests on a well-founded fear of persecution on grounds of race, religion, nationality, political opinion or membership of a particular social group.",
            "Non-refoulement - not returning a person to a country where they face persecution - is the core principle and is widely treated as customary international law.",
            "India hosts large refugee populations and grants residence permits administratively; UNHCR registers some groups in India.",
            "The Foreigners Act, 1946 gives the government wide powers over entry, stay and deportation of any non-citizen.",
            "Article 21 protects the life and liberty of every person, citizen or not, and Indian courts have used it to restrain arbitrary deportation.",
            "Statelessness leaves a person without any nationality, and creates severe practical barriers to work, education and documentation.",
            "Economic migrants are legally distinct from refugees, and mixed migration flows make status determination difficult in practice.",
        ],
        "laws": [
            "Convention Relating to the Status of Refugees, 1951 and its 1967 Protocol (India is not a party)",
            "Foreigners Act, 1946 and Registration of Foreigners Act, 1939",
            "Passport (Entry into India) Act, 1920",
            "Constitution of India - Articles 14 and 21, which apply to all persons",
        ],
        "steps": [
            "Establish identity and the reason for flight with whatever documentation exists.",
            "Approach UNHCR where it registers the relevant group, or the FRRO for a residence permit.",
            "Apply for a long-term visa where the government's policy allows it for the applicant's category.",
            "For detention or deportation threats, file a habeas corpus or writ petition invoking Article 21 and non-refoulement.",
            "Connect with legal aid clinics and NGOs, since these matters require sustained documentation support.",
        ],
        "faqs": [
            {
                "q": "Does India have a refugee law?",
                "a": "No dedicated statute. Refugees are dealt with under the general foreigners law and executive policy, supplemented by constitutional protections that courts have extended to non-citizens.",
            },
        ],
        "keywords": ["refugee", "asylum", "non refoulement", "unhcr", "foreigners act", "deportation", "statelessness", "migration", "frro", "long term visa"],
    },
    {
        "id": "comparative-legal-systems",
        "category": "humanrights",
        "title": "Legal Systems of the World - A Comparative View",
        "summary": (
            "Not every country reasons about law the way India does. Broadly, the world runs on "
            "four families of legal systems, and knowing which family a country belongs to tells "
            "you how its courts think, how much weight precedent carries, and where the law is "
            "actually written down."
        ),
        "key_points": [
            "Common law - England, USA, India, Australia, Canada. Judge-made law, binding precedent, adversarial trials.",
            "Civil law - France, Germany, Japan, Brazil. Comprehensive codes, judges as investigators, precedent persuasive rather than binding.",
            "Religious law - Sharia-based systems in several countries, where religious sources are a primary source of law.",
            "Customary and hybrid systems - many African and Asian states combine customary law with a colonial-era code.",
            "India is a hybrid: common law in structure and procedure, but with codified substantive law and religion-based personal laws.",
            "The doctrine of stare decisis makes higher court decisions binding in common law systems; in India, Supreme Court decisions bind all courts under Article 141.",
            "International commercial parties often choose a neutral common law seat, such as England or Singapore, precisely because the precedent-based system is predictable.",
        ],
        "laws": [
            "Constitution of India - Article 141 (law declared by the Supreme Court is binding)",
            "Comparative jurisprudence - civil law codes such as the French Code Civil and the German BGB",
            "New York Convention, 1958 - enforcement of foreign arbitral awards across systems",
        ],
        "steps": [
            "Identify the country's legal family before researching a foreign law question.",
            "In civil law countries, start with the code, not with case law.",
            "In common law countries, trace the leading precedents and check whether they are still good law.",
            "For cross-border contracts, expressly choose the governing law and the dispute resolution seat.",
            "Check whether a foreign judgment or arbitral award will actually be enforceable in the other country.",
        ],
        "faqs": [
            {
                "q": "Why does India follow English cases?",
                "a": "Because the Indian legal system was built on the common law during colonial rule. English decisions are not binding today, but they are persuasive where Indian law is silent.",
            },
        ],
        "keywords": ["comparative law", "common law", "civil law", "sharia", "precedent", "stare decisis", "article 141", "legal systems", "hybrid", "new york convention"],
    },

    # ==================================================================
    # STARTUP AND BUSINESS COMPLIANCE
    # ==================================================================
    {
        "id": "startup-registration",
        "category": "startup",
        "title": "Starting a Business - Licences and Registrations Checklist",
        "summary": (
            "Between deciding to start and legally operating there is a list of registrations, "
            "and the list depends on what you do, where you do it and how much you earn. Getting "
            "this right at the beginning is far cheaper than fixing it during a funding due "
            "diligence."
        ),
        "key_points": [
            "Universal basics: PAN and TAN for the entity, a current bank account, and the entity registration certificate itself.",
            "Shops and Establishments registration under the state Act is needed for almost every commercial premises.",
            "GST registration once the turnover threshold is crossed, or immediately for inter-state supply of goods and for e-commerce operators.",
            "Professional tax registration applies in several states for both the employer and employees.",
            "EPF registration at 20 employees and ESI at 10 employees, with voluntary registration possible earlier.",
            "Sector licences: FSSAI for food, drug licence for pharmacies, trade licence from the municipality, fire NOC, and pollution board consent for manufacturing.",
            "Startup India recognition through DPIIT gives tax benefits, self-certification on labour and environment laws, and IPR fee concessions.",
        ],
        "laws": [
            "Companies Act, 2013 or LLP Act, 2008 or Partnership Act, 1932 depending on the entity",
            "Central Goods and Services Tax Act, 2017",
            "State Shops and Commercial Establishments Acts",
            "Food Safety and Standards Act, 2006 and other sectoral statutes",
            "Startup India / DPIIT recognition notification",
        ],
        "steps": [
            "Choose the entity type based on liability, funding and compliance appetite.",
            "Incorporate and obtain PAN, TAN and the Certificate of Incorporation.",
            "Open the current account and bring in the subscription money through banking channels.",
            "Register under Shops and Establishments, GST and professional tax as applicable.",
            "Apply for sector-specific licences before starting operations, not after.",
            "Apply for DPIIT recognition if you qualify, and maintain a compliance calendar from day one.",
        ],
        "faqs": [
            {
                "q": "Do I need GST registration from day one?",
                "a": "Not unless you fall into a compulsory category such as inter-state supply of goods or selling through an e-commerce operator. Otherwise it starts when you cross the turnover threshold.",
            },
        ],
        "keywords": ["startup", "registration", "licence", "gst", "shops and establishment", "fssai", "dpiit", "startup india", "msme", "udyam", "checklist"],
    },
    {
        "id": "founders-agreement",
        "category": "startup",
        "title": "Founders Agreements, ESOPs and Equity Splits",
        "summary": (
            "Most startups die of founder disputes, not of competition. A founders agreement "
            "signed while everyone is still friendly decides what happens when someone leaves, "
            "and vesting is the single clause that protects the company from a founder who walks "
            "away with a large stake."
        ),
        "key_points": [
            "Vesting means equity is earned over time - typically four years with a one-year cliff, so a founder leaving in month six keeps nothing.",
            "Roles, responsibilities and decision-making thresholds should be written down, including which decisions need unanimous consent.",
            "Intellectual property created by founders must be assigned to the company in writing, or investors will flag it in due diligence.",
            "Good leaver and bad leaver clauses decide what a departing founder keeps depending on how they left.",
            "Transfer restrictions - right of first refusal, tag-along and drag-along - stop a founder selling to a stranger.",
            "ESOPs must be issued under a scheme approved by shareholders, with a defined pool, exercise price, vesting schedule and treatment on exit.",
            "Non-compete during the relationship is enforceable, but a post-exit non-compete is void under Section 27 of the Contract Act.",
        ],
        "laws": [
            "Indian Contract Act, 1872 - Section 27",
            "Companies Act, 2013 - Section 62(1)(b) and the Share Capital and Debentures Rules for ESOPs",
            "Companies Act, 2013 - Section 58 and 59 on transfer of shares",
        ],
        "steps": [
            "Agree the equity split honestly, weighing idea, capital, time commitment and risk taken.",
            "Write the founders agreement covering roles, vesting, IP assignment, leaver provisions and dispute resolution.",
            "Reflect the agreed restrictions in the Articles of Association, because a shareholders agreement alone may not bind the company.",
            "Sign IP assignment and confidentiality agreements with every founder, employee and freelancer.",
            "Approve an ESOP scheme by shareholder resolution and maintain a clean cap table.",
            "Review the documents before every funding round, since investors will require amendments.",
        ],
        "faqs": [
            {
                "q": "Should equity be split equally among founders?",
                "a": "Only if the contributions are genuinely equal. An honest unequal split with vesting causes far fewer problems later than an equal split that nobody actually believes is fair.",
            },
        ],
        "keywords": ["founders agreement", "vesting", "cliff", "esop", "equity split", "cap table", "ip assignment", "good leaver", "shareholders agreement", "drag along"],
    },
    {
        "id": "startup-funding",
        "category": "startup",
        "title": "Funding Rounds - SAFE, Convertible Notes and Term Sheets",
        "summary": (
            "Raising money changes who controls the company. A term sheet is mostly non-binding, "
            "but the economic and control terms it sets are almost never renegotiated later, so "
            "understanding liquidation preference, anti-dilution and board composition before "
            "signing is essential."
        ),
        "key_points": [
            "Bootstrapping, angel, seed, Series A and beyond describe stages, not legal categories.",
            "Convertible instruments postpone valuation - in India a CCPS or a compulsorily convertible debenture is typically used, since foreign investment rules restrict pure SAFEs.",
            "Liquidation preference decides who is paid first on a sale; a 1x non-participating preference is founder-friendly, participating preferences are not.",
            "Anti-dilution protects the investor if a later round is at a lower price; full ratchet is harsh, broad-based weighted average is the market norm.",
            "Reserved matters give investors a veto on specified decisions even without a board majority.",
            "Foreign investment must follow FEMA pricing guidelines, sectoral caps and reporting through Form FC-GPR within the prescribed time.",
            "Angel tax concerns on share premium have been relaxed for DPIIT-recognised startups meeting the conditions.",
        ],
        "laws": [
            "Companies Act, 2013 - Sections 42 (private placement), 62 (further issue)",
            "Foreign Exchange Management Act, 1999 and the Non-Debt Instruments Rules, 2019",
            "Income-tax Act, 1961 - Section 56(2)(viib) and the startup exemption notifications",
            "SEBI (Alternative Investment Funds) Regulations, 2012",
        ],
        "steps": [
            "Prepare a data room - incorporation documents, cap table, contracts, IP assignments, financials, statutory filings.",
            "Negotiate the term sheet, focusing on valuation, preference, anti-dilution, board seats and reserved matters.",
            "Complete legal and financial due diligence and fix the issues found.",
            "Execute the Share Subscription Agreement and the Shareholders Agreement, and amend the Articles to match.",
            "Pass the Board and shareholder resolutions, file the private placement forms, and allot shares within the statutory time.",
            "For foreign investors, complete FEMA reporting within the prescribed period after receipt of funds.",
        ],
        "faqs": [
            {
                "q": "Can a startup take money before valuation is decided?",
                "a": "Yes, through a convertible instrument that converts at the next round's valuation, usually with a discount or a cap. In India these are structured as compulsorily convertible instruments to comply with FEMA.",
            },
        ],
        "keywords": ["funding", "term sheet", "safe", "convertible note", "ccps", "liquidation preference", "anti dilution", "fema", "fc-gpr", "due diligence", "angel tax"],
    },
    {
        "id": "msme-benefits",
        "category": "startup",
        "title": "MSME Registration and Delayed Payment Protection",
        "summary": (
            "Udyam registration is free, takes minutes and gives a small business one very "
            "powerful right: if a buyer does not pay within 45 days, compound interest at three "
            "times the RBI bank rate runs automatically, and a special council decides the "
            "dispute quickly."
        ),
        "key_points": [
            "Classification is based on investment in plant and machinery and on turnover, in three tiers - micro, small and medium.",
            "Udyam registration is online, free, based on PAN and Aadhaar, and requires no documents to be uploaded.",
            "A buyer must pay an MSE supplier within the agreed period, and in any case within 45 days of acceptance.",
            "On delay, compound interest at three times the RBI notified bank rate is payable, and that interest is not deductible for the buyer's income tax.",
            "Disputes go to the Micro and Small Enterprises Facilitation Council, which must decide within 90 days, and any challenge to its award needs a 75 per cent pre-deposit.",
            "Buyers must report outstanding MSE dues beyond 45 days in half-yearly MSME-1 filings.",
            "Other benefits: collateral-free credit schemes, tender preferences, EMD exemption and subsidies on IP registration and certification.",
        ],
        "laws": [
            "Micro, Small and Medium Enterprises Development Act, 2006 - Sections 15, 16, 18 and 22",
            "Udyam Registration Notification, 2020",
            "Income-tax Act, 1961 - Section 43B(h) disallowance for delayed MSE payments",
            "Companies Act, 2013 - MSME-1 return",
        ],
        "steps": [
            "Register on the Udyam portal using PAN and Aadhaar - do not pay any agent, the process is free.",
            "Print the Udyam certificate and mention the registration number on every invoice and purchase order.",
            "Record the date of acceptance of goods or services, since the 45-day clock runs from it.",
            "Send a written demand with the interest computation once payment is delayed.",
            "File a reference before the MSEFC online; conciliation is attempted first, then arbitration.",
            "Enforce the award like a decree if the buyer still does not pay.",
        ],
        "faqs": [
            {
                "q": "Does MSME registration cost anything?",
                "a": "No. Udyam registration is completely free on the government portal. Websites charging fees for it are private agents, not the government.",
            },
        ],
        "keywords": ["msme", "udyam", "delayed payment", "45 days", "msefc", "interest", "small business", "43b(h)", "registration", "facilitation council"],
    },

    # ==================================================================
    # MEDICAL AND HEALTH LAW
    # ==================================================================
    {
        "id": "medical-negligence",
        "category": "medical",
        "title": "Medical Negligence and Patient Rights",
        "summary": (
            "A doctor is not liable simply because treatment failed. Liability arises only when "
            "the care fell below the standard of an ordinary competent practitioner in that "
            "field. The Bolam test, as adopted in India, is what separates an unfortunate outcome "
            "from actionable negligence."
        ),
        "key_points": [
            "The Bolam test: a doctor is not negligent if acting in accordance with a practice accepted as proper by a responsible body of medical professionals.",
            "Informed consent must be real - the patient must be told the nature of the procedure, the material risks and the alternatives.",
            "For surgery and invasive procedures, written consent is required, and consent for one procedure does not cover another.",
            "Res ipsa loquitur applies where the harm speaks for itself, such as an instrument left inside the body.",
            "Patients have the right to receive their medical records, usually within 72 hours of a request.",
            "Remedies: a consumer complaint for compensation, a civil suit for damages, a complaint to the State Medical Council for professional misconduct, and in gross cases criminal prosecution.",
            "Criminal liability requires gross negligence, not mere error of judgment, and courts require a prior independent medical opinion before prosecuting a doctor.",
        ],
        "laws": [
            "Consumer Protection Act, 2019 - medical services are 'services'",
            "Indian Medical Council (Professional Conduct, Etiquette and Ethics) Regulations, 2002 and the National Medical Commission Act, 2019",
            "Indian Medical Association v. V.P. Shantha (1995) - doctors covered by consumer law",
            "Jacob Mathew v. State of Punjab (2005) - standard for criminal medical negligence",
        ],
        "steps": [
            "Request the complete medical records in writing, including case sheet, investigation reports, consent forms and discharge summary.",
            "Get an independent opinion from a specialist in the same field about whether the standard of care was met.",
            "Compute the loss - medical expenses incurred, further treatment needed, loss of income, and compensation for suffering.",
            "Send a legal notice to the hospital and the treating doctor.",
            "File a consumer complaint in the appropriate Commission, supported by expert opinion and an affidavit.",
            "Separately, complain to the State Medical Council if professional misconduct is involved.",
        ],
        "faqs": [
            {
                "q": "Is a government hospital covered by consumer law?",
                "a": "Free treatment at a government hospital is generally outside consumer jurisdiction for want of consideration, but a writ petition or civil suit remains available, and paid services are covered.",
            },
            {
                "q": "Can a hospital refuse to give me my records?",
                "a": "No. Medical ethics regulations require records to be supplied to the patient or an authorised attendant on request, and refusal is itself professional misconduct.",
            },
        ],
        "keywords": ["medical negligence", "bolam", "informed consent", "medical records", "hospital", "doctor", "compensation", "shantha", "jacob mathew", "patient rights"],
    },
    {
        "id": "health-regulations",
        "category": "medical",
        "title": "Clinical Establishments, Drugs and Clinical Trials",
        "summary": (
            "Healthcare is a licensed activity from end to end - the clinic needs registration, "
            "the medicine needs approval and a licensed seller, and testing a new drug on humans "
            "needs ethics committee approval and regulatory permission at every stage."
        ),
        "key_points": [
            "Clinical establishments must register under the Clinical Establishments Act where the state has adopted it, and meet minimum standards.",
            "Drugs need manufacturing and sale licences, and Schedule H and H1 drugs can be sold only against a prescription, with records maintained.",
            "Clinical trials require approval from the licensing authority and from a registered Ethics Committee, plus registration on the Clinical Trials Registry of India.",
            "Trial participants must give written informed consent, with audio-visual recording in vulnerable-population trials, and are entitled to compensation for trial-related injury.",
            "Sex determination of a foetus is prohibited, and clinics must display the prohibition and maintain prescribed records.",
            "The Mental Healthcare Act, 2017 recognises the right to access mental healthcare, advance directives, and decriminalised attempted suicide in most cases.",
            "Transplantation of human organs requires authorisation committee approval for unrelated donors, and commercial dealing in organs is a serious offence.",
        ],
        "laws": [
            "Clinical Establishments (Registration and Regulation) Act, 2010",
            "Drugs and Cosmetics Act, 1940 and the New Drugs and Clinical Trials Rules, 2019",
            "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
            "Mental Healthcare Act, 2017",
            "Transplantation of Human Organs and Tissues Act, 1994",
        ],
        "steps": [
            "Identify every licence the activity needs before starting - registration, drug licence, biomedical waste authorisation, fire NOC.",
            "Constitute or engage a registered Ethics Committee for any research involving human participants.",
            "Prepare the protocol, the informed consent document in the local language, and the insurance and compensation plan.",
            "Obtain regulatory permission and register the trial before enrolling the first participant.",
            "Maintain records for the prescribed period and report serious adverse events within the timelines.",
            "For a grievance, complain to the state health authority, the drug controller, or the relevant council.",
        ],
        "faqs": [
            {
                "q": "Is telemedicine legal in India?",
                "a": "Yes. The Telemedicine Practice Guidelines, 2020 permit registered medical practitioners to consult remotely, with restrictions on which categories of medicine can be prescribed.",
            },
        ],
        "keywords": ["clinical establishment", "drug licence", "clinical trial", "ethics committee", "pcpndt", "mental healthcare", "organ transplant", "telemedicine", "schedule h"],
    },
    {
        "id": "reproductive-rights",
        "category": "medical",
        "title": "Reproductive Rights, Surrogacy and ART",
        "summary": (
            "Reproductive law in India balances a woman's autonomy against regulatory concerns "
            "about sex selection and commercial exploitation. Abortion is permitted within "
            "defined gestational limits and grounds, while surrogacy has been restricted to "
            "altruistic arrangements only."
        ),
        "key_points": [
            "Medical termination of pregnancy is allowed up to 20 weeks on the opinion of one registered practitioner, and up to 24 weeks for specified categories on the opinion of two.",
            "Beyond 24 weeks, termination is permitted for substantial foetal abnormalities on a Medical Board's opinion.",
            "The Supreme Court has extended the 24-week benefit to unmarried women, holding that marital status cannot decide reproductive autonomy.",
            "Only the woman's consent is required - a husband's consent is not a legal requirement; a guardian's consent is needed for a minor.",
            "The identity of a woman seeking termination must be kept confidential.",
            "Commercial surrogacy is prohibited; only altruistic surrogacy for eligible couples and certain women is permitted, with certificates of essentiality and eligibility.",
            "Assisted reproductive technology clinics and banks must be registered, and donor anonymity and record-keeping requirements apply.",
        ],
        "laws": [
            "Medical Termination of Pregnancy Act, 1971 as amended in 2021",
            "Surrogacy (Regulation) Act, 2021",
            "Assisted Reproductive Technology (Regulation) Act, 2021",
            "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
            "X v. Principal Secretary, Health, NCT of Delhi (2022)",
        ],
        "steps": [
            "Consult a registered medical practitioner at a facility approved for the procedure.",
            "Where the gestational age requires it, obtain the opinions or Medical Board approval prescribed by law.",
            "Give written consent on the prescribed form; confidentiality must be maintained by the facility.",
            "For surrogacy or ART, obtain the certificates of eligibility and essentiality from the appropriate authority before proceeding.",
            "Ensure the clinic is registered on the national registry and that all statutory records are maintained.",
        ],
        "faqs": [
            {
                "q": "Does an unmarried woman need anyone's permission for an abortion?",
                "a": "No. The Supreme Court has held that unmarried women are entitled to the same protection under the MTP Act, and only her own consent is required if she is an adult.",
            },
        ],
        "keywords": ["abortion", "mtp act", "surrogacy", "art", "reproductive rights", "24 weeks", "medical board", "altruistic surrogacy", "consent", "pcpndt"],
    },
    {
        "id": "public-health-law",
        "category": "medical",
        "title": "Public Health, Epidemics and Food Safety",
        "summary": (
            "Public health law gives the State emergency powers to control disease and everyday "
            "powers to regulate what people eat. Both were tested during COVID-19, which showed "
            "how much of India's epidemic response still rests on a short colonial-era statute."
        ),
        "key_points": [
            "The Epidemic Diseases Act, 1897 lets governments take temporary measures to prevent the spread of a dangerous epidemic disease.",
            "The Disaster Management Act, 2005 was used during COVID-19 to issue nationwide binding directions, with penalties for violation.",
            "Assault on healthcare personnel during an epidemic was made a serious offence by the 2020 amendment.",
            "Food businesses need an FSSAI licence or registration by scale, and must display the licence number on packaging.",
            "Labelling must disclose ingredients, nutrition, veg or non-veg mark, allergens, date of manufacture and best-before date.",
            "Misbranded and substandard food attracts penalties, and unsafe food causing injury or death attracts imprisonment.",
            "Adulteration complaints can be made to the Food Safety Officer, who takes samples for analysis by a notified laboratory.",
        ],
        "laws": [
            "Epidemic Diseases Act, 1897 as amended in 2020",
            "Disaster Management Act, 2005",
            "Food Safety and Standards Act, 2006 and the Packaging and Labelling Regulations",
            "National Medical Commission Act, 2019",
        ],
        "steps": [
            "For a food business, determine the licence category by turnover and scale, and apply on the FoSCoS portal.",
            "Display the FSSAI number, maintain hygiene standards, and keep purchase and testing records.",
            "For a complaint about unsafe food, preserve the packaging and bill and report to the Food Safety Officer.",
            "Note the sample seizure procedure - a portion is sealed for analysis and you are entitled to the report.",
            "For epidemic-period orders, check the exact notification, since powers and penalties differ under each statute.",
        ],
        "faqs": [
            {
                "q": "Can I complain about a restaurant that made me ill?",
                "a": "Yes - to the Food Safety Officer under the FSS Act for regulatory action, and separately in the consumer forum for compensation. Preserve the bill, packaging and medical records.",
            },
        ],
        "keywords": ["public health", "epidemic", "fssai", "food safety", "labelling", "adulteration", "disaster management", "covid", "licence", "food safety officer"],
    },

    # ==================================================================
    # EDUCATION LAW
    # ==================================================================
    {
        "id": "right-to-education",
        "category": "education",
        "title": "Right to Education and School Admissions",
        "summary": (
            "Education for children aged 6 to 14 is not a welfare scheme but a Fundamental Right "
            "under Article 21A. The RTE Act turns it into enforceable duties: free schooling, no "
            "screening at admission, and a 25 per cent quota for disadvantaged children in "
            "private schools."
        ),
        "key_points": [
            "Free and compulsory education for every child aged 6 to 14 in a neighbourhood school.",
            "Private unaided schools must reserve 25 per cent of entry-level seats for children from disadvantaged and weaker sections, reimbursed by the State.",
            "No capitation fee, and no screening procedure for the child or the parents at admission.",
            "No child may be held back or expelled till the completion of elementary education, and no board examination till then.",
            "Corporal punishment and mental harassment of children are prohibited.",
            "Schools must meet prescribed norms for pupil-teacher ratio, infrastructure and working days, and teachers must hold prescribed qualifications.",
            "School Management Committees with parent majority monitor school functioning in government and aided schools.",
        ],
        "laws": [
            "Constitution of India - Article 21A and Article 45",
            "Right of Children to Free and Compulsory Education Act, 2009 - Sections 3, 12(1)(c), 13, 16, 17",
            "Society for Unaided Private Schools of Rajasthan v. Union of India (2012) - validity of the 25 per cent quota",
        ],
        "steps": [
            "Check the state's RTE admission portal for the notified schedule and the neighbourhood definition.",
            "Keep the child's birth certificate, address proof, income or caste certificate ready as required.",
            "Apply within the window - most states run a lottery for oversubscribed schools.",
            "If a school refuses admission, demand the refusal in writing.",
            "Complain to the Block or District Education Officer, and then to the State Commission for Protection of Child Rights.",
            "A writ petition in the High Court is available where administrative remedies fail.",
        ],
        "faqs": [
            {
                "q": "Can a school ask for a donation for admission?",
                "a": "No. Capitation fee is expressly prohibited and attracts a penalty of up to ten times the amount collected. Ask for a receipt and complain if it is demanded.",
            },
        ],
        "keywords": ["rte", "right to education", "21a", "admission", "capitation fee", "25 percent quota", "school", "corporal punishment", "neighbourhood school"],
    },
    {
        "id": "ragging-and-campus",
        "category": "education",
        "title": "Anti-Ragging Law and Campus Safety",
        "summary": (
            "Ragging is not a tradition, it is a punishable offence, and the UGC Regulations make "
            "the institution itself liable if it fails to act. Every student and parent signs an "
            "anti-ragging affidavit each year precisely because the Supreme Court directed it."
        ),
        "key_points": [
            "Ragging includes any conduct that teases, treats rudely, or causes physical or psychological harm or apprehension to a fresher.",
            "Every institution must have an Anti-Ragging Committee and an Anti-Ragging Squad, and display the helpline prominently.",
            "Punishments range from suspension of scholarships and debarment from examinations to rustication and expulsion, with an FIR in serious cases.",
            "An institution failing to act can lose affiliation, grants and recognition.",
            "The national anti-ragging helpline 1800-180-5522 and the online portal accept complaints, including anonymous ones.",
            "Every student and parent must submit an online anti-ragging affidavit at the start of each academic year.",
            "Hostels and campuses also owe a duty of care for safety, and institutions must have an Internal Committee under the POSH Act for sexual harassment complaints.",
        ],
        "laws": [
            "UGC Regulations on Curbing the Menace of Ragging in Higher Educational Institutions, 2009",
            "University of Kerala v. Council of Principals of Colleges (Raghavan Committee directions)",
            "Bharatiya Nyaya Sanhita, 2023 - hurt, criminal intimidation, wrongful restraint",
            "Sexual Harassment of Women at Workplace Act, 2013 - applies to students as aggrieved women in an institution",
        ],
        "steps": [
            "Record what happened with dates, names and any messages or recordings.",
            "Call the national anti-ragging helpline or file on the portal - complaints can be anonymous.",
            "Complain in writing to the Anti-Ragging Committee and the head of the institution, and keep an acknowledged copy.",
            "For physical assault or serious threats, file an FIR immediately; the institution cannot stop you.",
            "If the institution does not act within the prescribed time, escalate to the UGC and the affiliating university.",
            "Seek counselling support - institutions are required to provide it.",
        ],
        "faqs": [
            {
                "q": "Will complaining about ragging affect my academic record?",
                "a": "It should not, and retaliation against a complainant is itself punishable. Keep documentary proof of your complaint and escalate immediately if you face any victimisation.",
            },
        ],
        "keywords": ["ragging", "anti ragging", "ugc", "campus", "helpline", "affidavit", "college", "hostel", "student safety", "1800 180 5522"],
    },
    {
        "id": "higher-education-regulation",
        "category": "education",
        "title": "Universities, UGC/AICTE Approval and Degree Validity",
        "summary": (
            "Not every institution calling itself a university can grant a degree. Only "
            "institutions established by a statute or notified as deemed universities can, and "
            "students who join unrecognised institutions discover the problem only when they "
            "apply for a job or higher studies."
        ),
        "key_points": [
            "Degree-granting power comes only from a Central Act, a State Act, an Institution of National Importance status, or deemed-to-be-university notification.",
            "The UGC publishes a list of fake universities; degrees from them have no legal value.",
            "AICTE approval is required for technical programmes such as engineering, management and pharmacy at the programme level.",
            "Professional courses have their own regulators - Bar Council for law, NMC for medicine, COA for architecture, NCTE for teacher education.",
            "Distance and online programmes need specific UGC recognition, and not all programmes may be offered in that mode.",
            "Institutions cannot withhold original certificates as a means of recovering fees, and the UGC has directed full refund of fees on cancellation within notified timelines.",
            "Students can seek redress through the institution's grievance redressal committee, then the Ombudsperson appointed by the university.",
        ],
        "laws": [
            "University Grants Commission Act, 1956 - Sections 22 and 23 on degree-granting and use of the word 'university'",
            "All India Council for Technical Education Act, 1987",
            "UGC (Redressal of Grievances of Students) Regulations",
            "UGC (Open and Distance Learning Programmes and Online Programmes) Regulations",
        ],
        "steps": [
            "Verify the institution on the UGC and AICTE portals and check the fake university list before paying any fee.",
            "Confirm that the specific programme, mode and campus are approved, not merely the institution.",
            "Keep the prospectus, fee receipts and the admission letter - these are the contract.",
            "For a grievance, approach the institution's Student Grievance Redressal Committee in writing.",
            "Escalate to the university Ombudsperson, then the UGC or the relevant regulator.",
            "For fee refund disputes, cite the UGC refund circular and file a consumer complaint if refused.",
        ],
        "faqs": [
            {
                "q": "Can a college keep my original certificates?",
                "a": "No. The UGC has directed institutions not to retain original documents. They must be returned, and withholding them to force fee payment has been repeatedly held unlawful.",
            },
        ],
        "keywords": ["ugc", "aicte", "university", "deemed university", "fake university", "degree validity", "distance education", "fee refund", "grievance", "ombudsperson"],
    },
    {
        "id": "student-rights-reservation",
        "category": "education",
        "title": "Reservation, Scholarships and Disability Accommodations",
        "summary": (
            "Access to education is shaped by reservation policy and by the duty to provide "
            "reasonable accommodation to students with disabilities. Both are legal entitlements "
            "with defined procedures, not discretionary favours from an institution."
        ),
        "key_points": [
            "Reservation in central educational institutions covers Scheduled Castes, Scheduled Tribes, Other Backward Classes and Economically Weaker Sections, with state percentages varying.",
            "The creamy layer exclusion applies to OBC reservation, based on parental income and status criteria.",
            "The Rights of Persons with Disabilities Act, 2016 mandates a minimum reservation in higher education for benchmark disabilities and requires reasonable accommodation.",
            "Accommodations include a scribe, extra time, accessible venues, alternative formats and relaxed attendance where justified.",
            "Scholarship schemes such as post-matric and merit-cum-means have defined eligibility and timelines, and institutions must forward applications on time.",
            "Discrimination on the basis of caste, disability or gender in an institution is actionable before the relevant commission and the courts.",
            "Every higher education institution must appoint equal opportunity cells and, where required, a disability coordinator.",
        ],
        "laws": [
            "Constitution of India - Articles 15(4), 15(5), 15(6) and 16",
            "Central Educational Institutions (Reservation in Admission) Act, 2006",
            "Rights of Persons with Disabilities Act, 2016 - Sections 16, 17 and 32",
            "Indra Sawhney v. Union of India (1992) - creamy layer and reservation limits",
        ],
        "steps": [
            "Obtain the caste, income, EWS or disability certificate from the competent authority well before admission deadlines.",
            "Apply under the correct category in the admission form - categories usually cannot be changed later.",
            "For accommodations, apply in writing to the examination authority with the disability certificate, well before the exam.",
            "For scholarships, apply on the national scholarship portal within the window and track institution verification.",
            "If denied, obtain written reasons and escalate to the grievance cell, then to the SC/ST or Disability Commissioner.",
            "A writ petition is available where a statutory entitlement is denied without justification.",
        ],
        "faqs": [
            {
                "q": "Can an institution refuse a scribe for an exam?",
                "a": "No. A candidate with a benchmark disability is entitled to a scribe and compensatory time under the RPwD Act and the government's guidelines. Refusal can be challenged before the Disability Commissioner or the High Court.",
            },
        ],
        "keywords": ["reservation", "scholarship", "disability", "rpwd", "scribe", "ews", "obc", "creamy layer", "accommodation", "equal opportunity"],
    },
]

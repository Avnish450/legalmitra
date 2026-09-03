# -*- coding: utf-8 -*-
"""
legal_extras.py
===============
Two smaller pieces of the knowledge base:

GLOSSARY  : an A-to-Z dictionary of legal words, so a first-time visitor can
            understand the language used on the rest of the site.
EMERGENCY : "what do I do right now" cards for situations where a person needs
            an answer in the next five minutes, not a research article.
HELPLINES : official national helpline numbers shown in the footer.
"""

# ---------------------------------------------------------------------------
# A TO Z GLOSSARY
# ---------------------------------------------------------------------------

GLOSSARY = [
    {"term": "Acquittal", "meaning": "A court's finding that the accused is not guilty of the offence charged."},
    {"term": "Adjournment", "meaning": "Postponement of a court hearing to a later date."},
    {"term": "Affidavit", "meaning": "A written statement of facts sworn on oath before a notary or officer authorised to administer oaths."},
    {"term": "Alimony", "meaning": "Financial support paid by one spouse to the other after separation or divorce."},
    {"term": "Anticipatory Bail", "meaning": "An order obtained before arrest, directing that the applicant be released on bail if arrested."},
    {"term": "Appellant", "meaning": "The party who files an appeal against a decision."},
    {"term": "Arbitration", "meaning": "Private dispute resolution where a neutral arbitrator gives a binding award instead of a court."},
    {"term": "Bail", "meaning": "Release of an accused person from custody, usually on furnishing a bond and sureties."},
    {"term": "Bailable Offence", "meaning": "An offence where bail is a matter of right and can be granted at the police station itself."},
    {"term": "Bona Fide", "meaning": "In good faith; honestly and without intention to deceive."},
    {"term": "Breach of Contract", "meaning": "Failure to perform any promise forming part of a contract, without lawful excuse."},
    {"term": "Caveat", "meaning": "A notice filed in court asking that no order be passed against you without hearing you first."},
    {"term": "Caveat Emptor", "meaning": "'Let the buyer beware' - the buyer's duty to examine goods before purchase."},
    {"term": "Cognizable Offence", "meaning": "A serious offence where the police may register an FIR and arrest without a warrant."},
    {"term": "Compoundable Offence", "meaning": "An offence which the complainant may legally compromise, ending the case."},
    {"term": "Consideration", "meaning": "Something of value given in exchange for a promise; without it an agreement is usually void."},
    {"term": "Coparcener", "meaning": "A member of a Hindu Undivided Family who acquires a right in the ancestral property by birth."},
    {"term": "Decree", "meaning": "The formal expression of a court's adjudication conclusively determining the rights of the parties in a suit."},
    {"term": "Defendant", "meaning": "The person against whom a civil suit is filed."},
    {"term": "Deponent", "meaning": "The person who makes and signs an affidavit."},
    {"term": "Ex Parte", "meaning": "An order passed in the absence of one party, usually because that party did not appear."},
    {"term": "Encumbrance", "meaning": "A charge, mortgage, lien or claim attached to a property that affects its transfer."},
    {"term": "Estoppel", "meaning": "A rule preventing a person from denying something they earlier caused another to believe and act upon."},
    {"term": "FIR", "meaning": "First Information Report - the first written record of information about a cognizable offence."},
    {"term": "Force Majeure", "meaning": "A contract clause excusing performance when an extraordinary event beyond a party's control prevents it."},
    {"term": "Fiduciary", "meaning": "A relationship of trust and confidence, requiring the person trusted to act in the other's interest."},
    {"term": "Gratuity", "meaning": "A lump sum paid by an employer as a reward for long service, usually after five years."},
    {"term": "Habeas Corpus", "meaning": "A writ requiring a detained person to be produced before the court to test the legality of the detention."},
    {"term": "Indemnity", "meaning": "A promise to compensate another for a loss they may suffer."},
    {"term": "Injunction", "meaning": "A court order directing a party to do, or to stop doing, a particular act."},
    {"term": "Intestate", "meaning": "Dying without leaving a valid will."},
    {"term": "Jurisdiction", "meaning": "The authority of a court to hear and decide a particular case."},
    {"term": "Judgment Debtor", "meaning": "The party against whom a money decree has been passed and who must pay it."},
    {"term": "Lien", "meaning": "A right to keep possession of another's property until a debt owed by that person is paid."},
    {"term": "Limitation", "meaning": "The time limit within which a case must be filed; after it expires the remedy is barred."},
    {"term": "Locus Standi", "meaning": "The legal right of a person to bring an action before a court."},
    {"term": "Mandamus", "meaning": "A writ commanding a public authority to perform a public duty it is refusing to perform."},
    {"term": "Mesne Profits", "meaning": "Compensation payable by a person in wrongful possession of property to the rightful owner."},
    {"term": "Mutation", "meaning": "The change of the owner's name in the revenue or municipal records after a transfer."},
    {"term": "Natural Justice", "meaning": "The minimum fairness rules: hear the other side, and no one may be a judge in their own cause."},
    {"term": "Negligence", "meaning": "Failure to take the care that a reasonable person would take, causing damage to another."},
    {"term": "Non-Cognizable Offence", "meaning": "A less serious offence where the police need a magistrate's order to investigate."},
    {"term": "Obiter Dicta", "meaning": "Observations made by a judge that are not essential to the decision and are not binding."},
    {"term": "Plaint", "meaning": "The written statement of claim that begins a civil suit."},
    {"term": "Plaintiff", "meaning": "The person who files a civil suit."},
    {"term": "Power of Attorney", "meaning": "A document authorising another person to act on your behalf in specified matters."},
    {"term": "Precedent", "meaning": "A previous decision of a higher court that must be followed in similar later cases."},
    {"term": "Prima Facie", "meaning": "At first sight; sufficient to establish a fact unless disproved."},
    {"term": "Probate", "meaning": "A court's certification that a will is genuine and that the executor may administer the estate."},
    {"term": "Quantum Meruit", "meaning": "'As much as is deserved' - payment for the value of work actually done where no price was fixed."},
    {"term": "Ratio Decidendi", "meaning": "The legal reasoning essential to a decision; this is the part that binds later courts."},
    {"term": "Res Judicata", "meaning": "A matter already finally decided between the same parties cannot be litigated again."},
    {"term": "Res Ipsa Loquitur", "meaning": "'The thing speaks for itself' - negligence inferred because the accident could not otherwise have happened."},
    {"term": "Respondent", "meaning": "The party who responds to an appeal, writ or petition."},
    {"term": "Retrenchment", "meaning": "Termination of a workman's service by the employer for reasons other than punishment."},
    {"term": "Sine Die", "meaning": "Adjourned indefinitely, without fixing a date."},
    {"term": "Solatium", "meaning": "An additional sum paid over and above compensation, to recognise the compulsory nature of an acquisition."},
    {"term": "Specific Performance", "meaning": "A court order compelling a party to actually perform the contract instead of paying damages."},
    {"term": "Stridhan", "meaning": "Property gifted to a woman before, during or after marriage, over which she has absolute ownership."},
    {"term": "Sub Judice", "meaning": "A matter currently under consideration by a court, and therefore not to be publicly prejudged."},
    {"term": "Summons", "meaning": "A court document requiring a person to appear before it on a specified date."},
    {"term": "Suo Motu", "meaning": "On its own motion - action taken by a court or authority without any party asking for it."},
    {"term": "Testator", "meaning": "The person who makes a will."},
    {"term": "Tort", "meaning": "A civil wrong, other than breach of contract, for which the remedy is unliquidated damages."},
    {"term": "Ultra Vires", "meaning": "Beyond the legal power or authority of the person or body acting."},
    {"term": "Vakalatnama", "meaning": "The document by which a party authorises an advocate to appear and act for them in a case."},
    {"term": "Vicarious Liability", "meaning": "Liability of one person, such as an employer, for the wrongful act of another, such as an employee."},
    {"term": "Void", "meaning": "Having no legal effect from the very beginning."},
    {"term": "Voidable", "meaning": "Valid until one of the parties chooses to set it aside."},
    {"term": "Waiver", "meaning": "Voluntarily giving up a known legal right."},
    {"term": "Writ", "meaning": "A formal order issued by a constitutional court, such as habeas corpus or mandamus."},
]


# ---------------------------------------------------------------------------
# EMERGENCY / QUICK HELP CARDS
# ---------------------------------------------------------------------------

EMERGENCY = [
    {
        "id": "arrested",
        "title": "I have been arrested or detained",
        "icon": "\U0001f6a8",
        "immediate": [
            "Do not resist and do not argue - resisting is itself an offence.",
            "Ask the officer for their name, rank and the grounds of arrest.",
            "Ask that a family member or friend be informed immediately - this is your right.",
            "Ask to see and sign the arrest memo, and check that a witness has signed it.",
            "Say clearly that you wish to consult a lawyer before answering questions.",
            "You must be produced before a Magistrate within 24 hours of arrest.",
            "If you cannot afford a lawyer, ask the Magistrate for free legal aid.",
        ],
        "do_not": [
            "Do not sign any blank or unread paper.",
            "Do not confess or make a statement without your lawyer present.",
            "Do not pay any money to anyone for release.",
        ],
        "helpline": "Legal aid: NALSA helpline 15100  |  Emergency: 112",
        "topic": "arrest-and-bail",
    },
    {
        "id": "online-fraud",
        "title": "Money was taken from my account online",
        "icon": "\U0001f4b3",
        "immediate": [
            "Call 1930 immediately - the first few hours decide whether the money can be frozen.",
            "Report on the National Cybercrime Reporting Portal, cybercrime.gov.in.",
            "Call your bank and ask them to freeze the beneficiary account and block your card.",
            "Send the bank a written complaint the same day and keep the acknowledgement.",
            "Take screenshots of the transaction, the SMS alerts and any message from the fraudster.",
            "File an FIR at the local police station or the cyber cell.",
        ],
        "do_not": [
            "Do not share the OTP, CVV, PIN or screen access with anyone, including callers claiming to be from the bank.",
            "Do not install any remote-access app on a caller's instruction.",
            "Do not delete the messages or format the phone - they are evidence.",
        ],
        "helpline": "Cyber fraud: 1930  |  Portal: cybercrime.gov.in",
        "topic": "cybercrime-reporting",
    },
    {
        "id": "police-refuses-fir",
        "title": "The police refuse to register my FIR",
        "icon": "\U0001f4dd",
        "immediate": [
            "Write the complaint out and hand it over, asking for a receiving stamp on your copy.",
            "Remember the Zero FIR rule - any police station must register it regardless of the area.",
            "If refused, send the same complaint by registered post to the Superintendent of Police.",
            "Keep the postal receipt and the tracking printout as proof.",
            "If there is still no action, file a complaint before the Judicial Magistrate, who can order registration and investigation.",
        ],
        "do_not": [
            "Do not leave without a written acknowledgement of your complaint.",
            "Do not lose the postal receipts - they are your proof of escalation.",
        ],
        "helpline": "Emergency: 112  |  NALSA legal aid: 15100",
        "topic": "fir-filing",
    },
    {
        "id": "domestic-violence",
        "title": "I am facing violence at home",
        "icon": "\U0001f6e1️",
        "immediate": [
            "If you are in immediate danger, call 112 or the women's helpline 181.",
            "Move to a safe place - a relative, a friend, or a shelter home.",
            "Get medical attention and ensure the injuries are recorded in the medical record.",
            "Photograph injuries and damaged property, with the date visible if possible.",
            "Contact the Protection Officer of your district, or a registered service provider NGO.",
            "You can apply to the Magistrate for a protection order, a residence order and monetary relief.",
        ],
        "do_not": [
            "Do not delete threatening messages or call recordings.",
            "Do not sign any paper under pressure, including a settlement you do not accept.",
        ],
        "helpline": "Women's helpline: 181  |  Emergency: 112  |  Child helpline: 1098",
        "topic": "women-safety-laws",
    },
    {
        "id": "workplace-harassment",
        "title": "I am being harassed at my workplace",
        "icon": "\U0001f3e2",
        "immediate": [
            "Write down each incident with the date, time, place and the names of anyone present.",
            "Preserve emails, chats and any recordings; forward them to your personal email.",
            "File a written complaint with the Internal Committee within three months of the incident.",
            "If the employer has no Internal Committee, complain to the district Local Committee.",
            "You may ask for interim relief such as a transfer or leave while the inquiry is on.",
            "Your identity and the contents of the complaint must be kept confidential by law.",
        ],
        "do_not": [
            "Do not resign in haste - it weakens your position in the inquiry.",
            "Do not confront the respondent alone or delete any evidence.",
        ],
        "helpline": "Women's helpline: 181  |  SHe-Box portal for POSH complaints",
        "topic": "women-safety-laws",
    },
    {
        "id": "road-accident",
        "title": "I have been in a road accident",
        "icon": "\U0001f699",
        "immediate": [
            "Get medical help first - the law protects a Good Samaritan who helps an accident victim.",
            "Call 112 or the ambulance service 108.",
            "Note the offending vehicle's registration number, and take photographs of the scene.",
            "Ensure an FIR or accident report is registered at the police station.",
            "Collect the medical records, bills and the discharge summary.",
            "A claim can be filed before the Motor Accident Claims Tribunal - there is no time limit, but file early.",
        ],
        "do_not": [
            "Do not accept a cash settlement at the spot before knowing the extent of the injuries.",
            "Do not sign a blank claim form given by any agent.",
            "Do not move the vehicles before photographs are taken, unless it is unsafe.",
        ],
        "helpline": "Emergency: 112  |  Ambulance: 108  |  Highway helpline: 1033",
        "topic": "accident-compensation",
    },
    {
        "id": "cheque-bounced",
        "title": "A cheque given to me has bounced",
        "icon": "\U0001f4c4",
        "immediate": [
            "Collect the original cheque and the bank return memo - note the date you received it.",
            "You have 30 DAYS from the return memo to send the legal demand notice.",
            "Send the notice by registered post AD and by email, and keep the receipts.",
            "The drawer then gets 15 days to pay.",
            "If unpaid, file the complaint in court within the NEXT 30 days - this deadline is fatal.",
        ],
        "do_not": [
            "Do not lose the return memo or the original cheque.",
            "Do not delay the notice - the 30-day clock cannot be extended.",
        ],
        "helpline": "Consult an advocate immediately - this timeline has no exceptions.",
        "topic": "cheque-bounce",
    },
    {
        "id": "landlord-locked-out",
        "title": "My landlord has locked me out or cut the power",
        "icon": "\U0001f511",
        "immediate": [
            "A landlord cannot evict you by force, change the locks, or cut off water and electricity.",
            "Call 112 and report it - the police can prevent a breach of peace.",
            "Send a written complaint to the local police station and keep the acknowledgement.",
            "Photograph the locked premises and the disconnected connection.",
            "Approach the Rent Authority or the civil court for an injunction restoring possession and services.",
        ],
        "do_not": [
            "Do not break the lock yourself - that creates a separate dispute.",
            "Do not vacate without a written handover recording the deposit position.",
        ],
        "helpline": "Emergency: 112",
        "topic": "rent-and-tenancy",
    },
    {
        "id": "ragging",
        "title": "I am being ragged or bullied in college",
        "icon": "\U0001f393",
        "immediate": [
            "Call the national anti-ragging helpline 1800-180-5522 - complaints can be anonymous.",
            "File a complaint on the online anti-ragging portal.",
            "Write to the Anti-Ragging Committee and the head of the institution, and keep an acknowledged copy.",
            "Preserve messages, recordings and the names of witnesses.",
            "For assault or serious threats, file an FIR - the institution cannot stop you.",
        ],
        "do_not": [
            "Do not stay silent hoping it will pass - ragging usually escalates.",
            "Do not accept an informal 'compromise' that leaves no record.",
        ],
        "helpline": "Anti-ragging: 1800-180-5522  |  Emergency: 112",
        "topic": "ragging-and-campus",
    },
    {
        "id": "consumer-cheated",
        "title": "A company has cheated me or refuses a refund",
        "icon": "\U0001f6d2",
        "immediate": [
            "Collect the invoice, warranty card, screenshots of the offer and all chat or email records.",
            "Raise a complaint with the company's customer care and note the ticket number.",
            "Call the National Consumer Helpline 1915 or complain on the INGRAM portal.",
            "Send a legal notice giving 15 days to resolve.",
            "File a complaint on the e-Daakhil portal - you can file where you live, and you do not need a lawyer.",
        ],
        "do_not": [
            "Do not throw away the packaging or the defective product.",
            "Do not wait more than two years - that is the limitation period.",
        ],
        "helpline": "Consumer helpline: 1915  |  Portal: edaakhil.nic.in",
        "topic": "consumer-complaint",
    },
]


# ---------------------------------------------------------------------------
# NATIONAL HELPLINE NUMBERS
# ---------------------------------------------------------------------------

HELPLINES = [
    {"name": "All Emergencies (Police / Fire / Ambulance)", "number": "112"},
    {"name": "Cyber Crime and Online Financial Fraud", "number": "1930"},
    {"name": "Women's Helpline", "number": "181"},
    {"name": "Child Helpline", "number": "1098"},
    {"name": "National Consumer Helpline", "number": "1915"},
    {"name": "NALSA Free Legal Aid", "number": "15100"},
    {"name": "Anti-Ragging Helpline", "number": "1800-180-5522"},
    {"name": "Senior Citizen Helpline", "number": "14567"},
    {"name": "Mental Health (Tele-MANAS)", "number": "14416"},
    {"name": "Road Accident / Highway Emergency", "number": "1033"},
]

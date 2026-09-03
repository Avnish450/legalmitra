# -*- coding: utf-8 -*-
"""
legal_documents.py
==================
The DOCUMENT TEMPLATE library.

Each entry is a fill-in-the-blank draft of a document that ordinary people
actually need. Blanks are written as [SQUARE BRACKETS] so the user can see
exactly what has to be replaced.

Keys used by every document:
    id          slug used in the URL  ->  /document/rental-agreement
    title       name of the document
    category    the CATEGORIES id it belongs to
    purpose     one line - what this document does
    when_to_use when a person actually needs it
    checklist   the information/papers to keep ready before drafting
    stamp       stamp duty / registration / notarisation note
    body        the actual template text
    keywords    extra search words for the chatbot

IMPORTANT: these are educational drafts for a college project. A real
transaction should always be reviewed by a qualified advocate, because stamp
duty and registration requirements differ from state to state.
"""

DOCUMENTS = [

    # ------------------------------------------------------------------
    # PROPERTY
    # ------------------------------------------------------------------
    {
        "id": "rental-agreement",
        "title": "Residential Rent / Lease Agreement (11 Months)",
        "category": "property",
        "purpose": "Records the terms on which a landlord lets a house or flat to a tenant.",
        "when_to_use": "Before handing over possession of any rented residential premises.",
        "checklist": [
            "Full name, age, father's/husband's name and address of both parties",
            "Complete address and description of the premises, with the list of fittings",
            "Monthly rent, security deposit, and the date rent is payable each month",
            "Lock-in period, notice period and escalation on renewal",
            "Who pays electricity, water, maintenance and property tax",
            "Photographs of the premises and meter readings on the date of handover",
        ],
        "stamp": (
            "Executed on stamp paper of the value prescribed by the State Stamp Act. "
            "A lease of 12 months or more must be compulsorily registered, which is why "
            "the 11-month format is commonly used. Two witnesses should sign."
        ),
        "body": """RENT AGREEMENT

This Rent Agreement is made at [CITY] on this [DAY] day of [MONTH], [YEAR]

BETWEEN

[LANDLORD FULL NAME], aged about [AGE] years, son/daughter of [FATHER'S NAME],
residing at [LANDLORD ADDRESS], hereinafter called the "LANDLORD"
(which expression shall include his/her heirs, legal representatives and assigns)
of the ONE PART

AND

[TENANT FULL NAME], aged about [AGE] years, son/daughter of [FATHER'S NAME],
residing at [TENANT ADDRESS], hereinafter called the "TENANT"
(which expression shall include his/her heirs and legal representatives)
of the OTHER PART

WHEREAS the Landlord is the absolute owner of the premises described in the
Schedule below, and the Tenant has approached the Landlord to take the same on
rent for residential purposes, and the Landlord has agreed on the following
terms and conditions:

1.  PREMISES: The Landlord lets out the premises described in the Schedule
    below, together with the fixtures and fittings listed in Annexure A.

2.  TERM: The tenancy shall be for a period of ELEVEN (11) MONTHS commencing
    from [START DATE] and ending on [END DATE], renewable by mutual written
    consent with an escalation of [PERCENTAGE]% on the then prevailing rent.

3.  RENT: The Tenant shall pay a monthly rent of Rs. [AMOUNT]/-
    (Rupees [AMOUNT IN WORDS] only) on or before the [DAY] day of every English
    calendar month, by bank transfer to Account No. [ACCOUNT NUMBER],
    [BANK NAME], IFSC [IFSC CODE].

4.  SECURITY DEPOSIT: The Tenant has paid an interest-free refundable security
    deposit of Rs. [AMOUNT]/- (Rupees [AMOUNT IN WORDS] only) vide
    [CHEQUE/UPI/NEFT REFERENCE] dated [DATE], the receipt of which the Landlord
    acknowledges. The deposit shall be refunded within [NUMBER] days of the
    Tenant handing over vacant and peaceful possession, after deducting any
    unpaid rent, unpaid utility bills, and the cost of damage beyond normal wear
    and tear.

5.  UTILITIES: The Tenant shall pay the electricity, water and gas charges as
    per actual meter readings, and the monthly maintenance of Rs. [AMOUNT]/-.
    The Landlord shall pay the property tax and any society corpus charges.

6.  USE: The premises shall be used only for residential purposes by the Tenant
    and the family members named in Annexure B, and shall not be used for any
    illegal, immoral or commercial activity.

7.  NO SUBLETTING: The Tenant shall not sublet, assign or part with possession
    of the premises or any part of it without the prior written consent of the
    Landlord.

8.  MAINTENANCE AND REPAIRS: Day-to-day minor repairs shall be borne by the
    Tenant. Major and structural repairs shall be borne by the Landlord.

9.  ALTERATIONS: The Tenant shall not make any structural alteration or
    permanent addition without the prior written consent of the Landlord.

10. INSPECTION: The Landlord or an authorised representative may inspect the
    premises after giving at least 24 hours' prior notice, at a mutually
    convenient time.

11. LOCK-IN AND NOTICE: There shall be a lock-in period of [NUMBER] months.
    Thereafter either party may terminate this Agreement by giving [NUMBER]
    months' prior written notice, or rent in lieu of the notice period.

12. HANDOVER: On expiry or earlier termination, the Tenant shall hand over
    vacant, peaceful possession of the premises in the same condition in which
    it was taken, normal wear and tear excepted, along with all keys.

13. DEFAULT: If the rent remains unpaid for [NUMBER] consecutive months, or if
    any term of this Agreement is breached and not cured within [NUMBER] days of
    written notice, the Landlord may terminate this Agreement.

14. STAMP DUTY: The cost of stamp duty and of preparing this Agreement shall be
    borne by [LANDLORD / TENANT / BOTH EQUALLY].

15. JURISDICTION: The courts at [CITY] shall have exclusive jurisdiction over
    any dispute arising out of this Agreement.

SCHEDULE OF PROPERTY
Flat/House No. [NUMBER], [FLOOR], [BUILDING/APARTMENT NAME], [STREET],
[LOCALITY], [CITY] - [PIN CODE], admeasuring approximately [AREA] square feet
carpet area, consisting of [NUMBER] bedrooms, [NUMBER] bathrooms, a kitchen and
a hall, bounded as follows:
    North by : [BOUNDARY]        South by : [BOUNDARY]
    East by  : [BOUNDARY]        West by  : [BOUNDARY]

IN WITNESS WHEREOF the parties have signed this Agreement on the day, month and
year first written above.


____________________                          ____________________
LANDLORD                                      TENANT
[NAME]                                        [NAME]

WITNESSES:
1. Name: [NAME], Address: [ADDRESS]           Signature: ____________
2. Name: [NAME], Address: [ADDRESS]           Signature: ____________
""",
        "keywords": ["rent agreement", "lease", "tenant", "landlord", "11 month", "rental", "house rent", "security deposit"],
    },
    {
        "id": "sale-deed",
        "title": "Sale Deed for Immovable Property",
        "category": "property",
        "purpose": "The registered document that actually transfers ownership of land or a flat.",
        "when_to_use": "At the time of completing a property purchase, before the Sub-Registrar.",
        "checklist": [
            "Chain of title documents for the last 30 years and the mother deed",
            "Encumbrance Certificate and latest property tax receipts",
            "Approved plan, occupancy certificate and khata/mutation extract",
            "PAN of both parties and TDS challan where consideration is Rs 50 lakh or more",
            "Identity proof and photographs of both parties and two witnesses",
        ],
        "stamp": (
            "Stamp duty is a percentage of the market value or consideration, whichever is "
            "higher, and varies by state; many states give a concession to a woman buyer. "
            "Registration under Section 17 of the Registration Act is COMPULSORY and must be "
            "done within four months of execution."
        ),
        "body": """SALE DEED

This Deed of Sale is executed at [CITY] on this [DAY] day of [MONTH], [YEAR]

BY

[SELLER FULL NAME], aged about [AGE] years, son/daughter of [FATHER'S NAME],
PAN [PAN], residing at [SELLER ADDRESS], hereinafter called the "VENDOR"

IN FAVOUR OF

[BUYER FULL NAME], aged about [AGE] years, son/daughter of [FATHER'S NAME],
PAN [PAN], residing at [BUYER ADDRESS], hereinafter called the "PURCHASER"

WHEREAS the Vendor is the absolute and lawful owner in possession of the
property more fully described in the Schedule hereunder, having acquired the
same by virtue of [SALE DEED / GIFT DEED / INHERITANCE / PARTITION] dated
[DATE], registered as Document No. [NUMBER] of [YEAR] in the office of the
Sub-Registrar, [PLACE];

AND WHEREAS the Vendor has agreed to sell and the Purchaser has agreed to
purchase the said property free from all encumbrances for a total consideration
of Rs. [AMOUNT]/- (Rupees [AMOUNT IN WORDS] only);

NOW THIS DEED WITNESSETH AS FOLLOWS:

1.  CONSIDERATION: In consideration of the sum of Rs. [AMOUNT]/- paid by the
    Purchaser to the Vendor as detailed below, the receipt of which the Vendor
    hereby acknowledges, the Vendor hereby sells, conveys and transfers unto the
    Purchaser the property described in the Schedule, absolutely and forever.

    Payment details:
      Advance paid on [DATE] : Rs. [AMOUNT] vide [MODE / REFERENCE]
      Balance paid on [DATE] : Rs. [AMOUNT] vide [MODE / REFERENCE]
      TDS deducted under Section 194-IA : Rs. [AMOUNT], Challan No. [NUMBER]

2.  POSSESSION: The Vendor has this day delivered vacant, peaceful and physical
    possession of the said property to the Purchaser.

3.  TITLE COVENANTS: The Vendor covenants that -
    (a) the Vendor has a clear, marketable and absolute title to the property;
    (b) the property is free from all encumbrances, charges, mortgages, liens,
        attachments, court injunctions, acquisition proceedings and claims;
    (c) there are no arrears of property tax, electricity, water or maintenance
        charges up to the date of this Deed;
    (d) the Vendor has not entered into any prior agreement to sell with any
        other person in respect of the said property.

4.  INDEMNITY: The Vendor shall indemnify and keep the Purchaser indemnified
    against any loss, claim or demand arising from any defect in title or from
    any breach of the above covenants.

5.  DOCUMENTS: The Vendor has handed over all original title documents relating
    to the said property to the Purchaser on this day.

6.  MUTATION: The Vendor shall cooperate with and sign all papers required for
    transfer of khata/mutation, electricity and water connections in the name of
    the Purchaser.

7.  EXPENSES: The stamp duty, registration charges and incidental expenses of
    this Deed have been borne by the [PURCHASER / VENDOR].

SCHEDULE OF PROPERTY
All that piece and parcel of [LAND / FLAT / HOUSE] bearing No. [NUMBER],
Survey No. [NUMBER], situated at [LOCALITY], [VILLAGE/TALUK], [DISTRICT],
[STATE], admeasuring [AREA] square feet / square metres, together with the
undivided share of land measuring [AREA], and bounded by:
    North : [BOUNDARY]           South : [BOUNDARY]
    East  : [BOUNDARY]           West  : [BOUNDARY]

IN WITNESS WHEREOF the parties have set their hands on the day, month and year
first above written.


____________________                          ____________________
VENDOR                                        PURCHASER
[NAME]                                        [NAME]

WITNESSES:
1. Name: [NAME], Address: [ADDRESS]           Signature: ____________
2. Name: [NAME], Address: [ADDRESS]           Signature: ____________
""",
        "keywords": ["sale deed", "property transfer", "conveyance", "registration", "stamp duty", "buy property", "vendor", "purchaser"],
    },
    {
        "id": "gift-deed",
        "title": "Gift Deed",
        "category": "property",
        "purpose": "Transfers property voluntarily and without any payment, usually within a family.",
        "when_to_use": "When a person wants to give property to a relative during their lifetime.",
        "checklist": [
            "Title documents proving the donor's ownership",
            "Relationship proof if claiming concessional stamp duty for a family transfer",
            "Acceptance by the donee during the donor's lifetime - this is essential",
            "Identity proof and photographs of donor, donee and two witnesses",
        ],
        "stamp": (
            "A gift of immovable property must be by a registered instrument attested by two "
            "witnesses under Section 123 of the Transfer of Property Act. Most states charge "
            "concessional stamp duty for gifts to specified close relatives."
        ),
        "body": """GIFT DEED

This Deed of Gift is executed at [CITY] on this [DAY] day of [MONTH], [YEAR]

BY

[DONOR NAME], aged about [AGE] years, son/daughter of [FATHER'S NAME], residing
at [ADDRESS], hereinafter called the "DONOR"

IN FAVOUR OF

[DONEE NAME], aged about [AGE] years, son/daughter of [FATHER'S NAME], residing
at [ADDRESS], who is the [RELATIONSHIP, e.g. daughter] of the Donor, hereinafter
called the "DONEE"

WHEREAS the Donor is the absolute owner of the property described in the
Schedule below, having acquired it by [MODE OF ACQUISITION] dated [DATE];

AND WHEREAS the Donor, out of natural love and affection for the Donee, and
without any monetary consideration, coercion or undue influence, desires to
gift the said property to the Donee;

NOW THIS DEED WITNESSETH:

1.  The Donor, out of natural love and affection and without any consideration,
    hereby transfers, conveys and gifts absolutely unto the Donee the property
    described in the Schedule below, together with all rights, easements and
    appurtenances belonging to it.

2.  The Donor has this day delivered possession of the said property to the
    Donee, and the Donee has accepted the gift during the lifetime of the Donor,
    which acceptance is hereby recorded.

3.  The Donor declares that the property is free from all encumbrances, charges
    and claims, and that the Donor has a clear and marketable title to it.

4.  This gift is absolute and irrevocable. The Donor shall have no right, title,
    interest or claim over the said property from the date of this Deed.

5.  The Donee shall be entitled to have the property mutated in her/his name in
    the revenue and municipal records, and the Donor shall sign all papers
    necessary for that purpose.

6.  The market value of the property for the purposes of stamp duty is
    Rs. [AMOUNT]/-.

SCHEDULE OF PROPERTY
[FULL DESCRIPTION OF THE PROPERTY WITH SURVEY NUMBER, AREA, LOCATION AND THE
FOUR BOUNDARIES]

IN WITNESS WHEREOF the Donor has signed this Deed and the Donee has signed in
token of acceptance, on the day, month and year first above written.


____________________                          ____________________
DONOR                                         DONEE (in acceptance)
[NAME]                                        [NAME]

WITNESSES:
1. Name: [NAME], Address: [ADDRESS]           Signature: ____________
2. Name: [NAME], Address: [ADDRESS]           Signature: ____________
""",
        "keywords": ["gift deed", "gift property", "donor", "donee", "family transfer", "natural love and affection"],
    },
    {
        "id": "eviction-notice",
        "title": "Notice to Vacate / Eviction Notice to Tenant",
        "category": "property",
        "purpose": "Formally ends a tenancy and asks the tenant to hand over possession.",
        "when_to_use": "When the tenancy period is ending, rent is unpaid, or the landlord needs the premises.",
        "checklist": [
            "A copy of the rent agreement and the rent payment record",
            "The exact amount of arrears with a month-wise computation",
            "The notice period required by the agreement or by law",
            "Proof of service - registered post AD, courier and email",
        ],
        "stamp": "No stamp duty. Send by registered post with acknowledgement due and keep the receipt.",
        "body": """NOTICE TO VACATE

From:
[LANDLORD NAME]
[ADDRESS]
[PHONE] | [EMAIL]

To:
[TENANT NAME]
[TENANTED PREMISES ADDRESS]

Date: [DATE]

Sent by: Registered Post A.D. and Email

Subject: Notice to vacate the premises at [ADDRESS] and to pay arrears of rent

Dear Sir/Madam,

1.  You are in occupation of the premises described above as my tenant under a
    Rent Agreement dated [DATE], at a monthly rent of Rs. [AMOUNT]/- payable on
    or before the [DAY] of every month.

2.  [CHOOSE THE APPLICABLE GROUND]
    (a) The term of the said Agreement expires on [DATE] and I do not wish to
        renew the tenancy; OR
    (b) You have failed to pay the rent for the months of [MONTHS], and a sum of
        Rs. [AMOUNT]/- is due and outstanding as on date, despite repeated oral
        reminders; OR
    (c) You have breached Clause [NUMBER] of the Agreement by [DESCRIBE THE
        BREACH, e.g. subletting the premises without consent]; OR
    (d) I require the premises for my own bona fide occupation.

3.  I hereby terminate your tenancy with effect from [DATE], being the expiry of
    [NUMBER] months from the date of this notice as required by Clause [NUMBER]
    of the Agreement.

4.  You are called upon to:
    (a) pay the outstanding rent of Rs. [AMOUNT]/- together with all unpaid
        electricity, water and maintenance charges; and
    (b) hand over vacant, peaceful and physical possession of the premises,
        together with all keys, on or before [DATE].

5.  On such handover, the security deposit of Rs. [AMOUNT]/- will be refunded to
    you after deducting any dues and the cost of damage beyond normal wear and
    tear, and a joint inspection will be conducted.

6.  Please note that if you fail to comply within the notice period, I shall be
    constrained to initiate appropriate legal proceedings for eviction, arrears
    of rent, mesne profits and damages, entirely at your risk as to cost and
    consequences.

7.  This notice is issued without prejudice to any other rights and remedies
    available to me in law.

Yours faithfully,


____________________
[LANDLORD NAME]
""",
        "keywords": ["eviction notice", "vacate", "tenant", "arrears of rent", "termination of tenancy", "notice to quit"],
    },

    # ------------------------------------------------------------------
    # EMPLOYMENT
    # ------------------------------------------------------------------
    {
        "id": "offer-letter",
        "title": "Employment Offer Letter",
        "category": "labour",
        "purpose": "Offers a job to a candidate and records the headline terms of employment.",
        "when_to_use": "After the selection process is complete and before the candidate joins.",
        "checklist": [
            "Designation, department, reporting manager and place of posting",
            "Complete salary break-up with basic, allowances and employer contributions",
            "Joining date, probation period and notice period",
            "Documents required at joining and the pre-joining conditions",
        ],
        "stamp": "No stamp duty. Issue on company letterhead, signed by an authorised signatory.",
        "body": """[COMPANY LETTERHEAD]

Date: [DATE]
Ref: [REFERENCE NUMBER]

To,
[CANDIDATE NAME]
[ADDRESS]

Subject: Offer of employment for the position of [DESIGNATION]

Dear [CANDIDATE NAME],

We are pleased to offer you employment with [COMPANY NAME] ("the Company") on
the following terms:

1.  POSITION      : [DESIGNATION], [DEPARTMENT]
2.  REPORTING TO  : [MANAGER NAME AND DESIGNATION]
3.  PLACE OF WORK : [LOCATION]. You may be transferred to any other location or
                    group company as per business requirements.
4.  DATE OF JOINING : [DATE]. This offer stands withdrawn if you do not join on
                    or before this date.

5.  COMPENSATION: Your Cost to Company will be Rs. [AMOUNT]/- per annum, made up
    as follows:

        Basic Salary                     Rs. [AMOUNT] per annum
        House Rent Allowance             Rs. [AMOUNT] per annum
        Special / Other Allowance        Rs. [AMOUNT] per annum
        Employer's Provident Fund        Rs. [AMOUNT] per annum
        Gratuity provision               Rs. [AMOUNT] per annum
        Performance-linked bonus         Rs. [AMOUNT] per annum
        -----------------------------------------------------
        Total Cost to Company            Rs. [AMOUNT] per annum

    Salary will be credited by the [DAY] of the following month, subject to
    deduction of tax at source and other statutory deductions.

6.  PROBATION: You will be on probation for [NUMBER] months from your date of
    joining. Your confirmation is subject to satisfactory performance and will
    be communicated in writing.

7.  NOTICE PERIOD: [NUMBER] days during probation and [NUMBER] days after
    confirmation, by either party, or payment of basic salary in lieu.

8.  WORKING HOURS: [TIMINGS], [DAYS] per week, with leave as per the Company's
    leave policy and the applicable Shops and Establishments Act.

9.  CONFIDENTIALITY AND IP: You will be required to sign the Company's
    Confidentiality and Intellectual Property Assignment Agreement. All work
    product created in the course of your employment shall vest in the Company.

10. CONDITIONS: This offer is subject to (a) verification of the documents and
    references furnished by you, (b) a satisfactory background check, and
    (c) your confirmation that you are not under any restrictive covenant with a
    previous employer.

11. DOCUMENTS AT JOINING: Educational certificates, previous employment
    relieving letter and last three salary slips, PAN, Aadhaar, bank details,
    and [NUMBER] passport-size photographs.

12. This letter and the Employment Agreement to be signed at joining constitute
    the entire understanding between us and supersede all prior discussions.

Please sign and return a copy of this letter as a token of your acceptance
within [NUMBER] days.

We look forward to welcoming you to the team.

Yours sincerely,
For [COMPANY NAME]


____________________
[NAME], [DESIGNATION]
Authorised Signatory

ACCEPTANCE
I, [CANDIDATE NAME], accept the above offer and confirm that I shall join on
[DATE].

Signature: ____________________       Date: ____________
""",
        "keywords": ["offer letter", "job offer", "employment", "ctc", "salary", "probation", "joining", "appointment"],
    },
    {
        "id": "employment-agreement",
        "title": "Employment Agreement",
        "category": "labour",
        "purpose": "The detailed contract governing the whole employment relationship.",
        "when_to_use": "Signed on the joining date, along with or after the offer letter.",
        "checklist": [
            "The agreed offer letter terms, so the two documents do not contradict each other",
            "The Company's leave, POSH, code of conduct and IT policies to annex",
            "Confidentiality, IP assignment and non-solicitation clauses",
            "The correct governing law and jurisdiction",
        ],
        "stamp": "Executed in duplicate on the company's letterhead or on stamp paper as per state practice.",
        "body": """EMPLOYMENT AGREEMENT

This Agreement is made on [DATE] at [CITY]

BETWEEN

[COMPANY NAME], a company incorporated under the Companies Act, 2013, having
CIN [CIN] and its registered office at [ADDRESS] (the "Company")

AND

[EMPLOYEE NAME], son/daughter of [FATHER'S NAME], residing at [ADDRESS]
(the "Employee")

1.  APPOINTMENT AND DUTIES
    1.1 The Company appoints the Employee as [DESIGNATION] with effect from
        [DATE], and the Employee accepts the appointment.
    1.2 The Employee shall perform the duties described in Annexure A and such
        other duties as may reasonably be assigned, shall devote her/his whole
        working time to the Company, and shall not engage in any other paid
        occupation without prior written consent.

2.  COMPENSATION
    2.1 The Employee shall be paid the compensation set out in Annexure B,
        subject to statutory deductions.
    2.2 Compensation is confidential and shall not be disclosed to colleagues.
    2.3 The Employee shall be covered under the Employees' Provident Fund, ESI
        (if applicable) and gratuity as per law.

3.  PROBATION AND CONFIRMATION
    3.1 The Employee shall be on probation for [NUMBER] months, extendable once
        by a further [NUMBER] months by written notice.
    3.2 Confirmation shall be by a written communication from the Company.

4.  WORKING HOURS AND LEAVE
    4.1 Working hours shall be [TIMINGS] on [DAYS], subject to the applicable
        Shops and Establishments Act.
    4.2 Leave entitlement shall be as per the Company's leave policy and the
        applicable law, whichever is more beneficial.

5.  CONFIDENTIALITY
    5.1 The Employee shall not, during or after employment, disclose or use any
        Confidential Information of the Company or its clients.
    5.2 "Confidential Information" includes business plans, client lists,
        pricing, source code, designs, financial data and any information marked
        or reasonably understood to be confidential.
    5.3 On separation, the Employee shall return all Company property, documents
        and data, and delete all Company data from personal devices.

6.  INTELLECTUAL PROPERTY
    6.1 All inventions, works, designs, software and other intellectual property
        created by the Employee in the course of employment, or using Company
        resources, shall be the sole property of the Company.
    6.2 The Employee assigns all such rights to the Company and agrees to sign
        any further documents required to perfect the assignment.

7.  NON-SOLICITATION
    For [NUMBER] months after separation, the Employee shall not solicit any
    employee, client or vendor of the Company with whom the Employee dealt in
    the last twelve months of employment. The parties acknowledge that a
    post-employment restraint on taking up other employment would be void under
    Section 27 of the Indian Contract Act, 1872, and no such restraint is
    imposed.

8.  CODE OF CONDUCT AND POSH
    The Employee shall comply with the Company's Code of Conduct and the Policy
    on Prevention of Sexual Harassment framed under the Sexual Harassment of
    Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013.

9.  TERMINATION
    9.1 Either party may terminate this Agreement by [NUMBER] days' written
        notice, or payment of basic salary in lieu of notice.
    9.2 The Company may terminate without notice for misconduct, fraud,
        breach of confidentiality, or conviction for an offence, after following
        the applicable disciplinary procedure.
    9.3 On separation the Employee shall complete the exit formalities, and the
        Company shall settle all dues within the statutory timeline.

10. GOVERNING LAW AND DISPUTES
    This Agreement shall be governed by the laws of India. Any dispute shall be
    referred to arbitration by a sole arbitrator under the Arbitration and
    Conciliation Act, 1996, seated at [CITY], and the courts at [CITY] shall
    have exclusive jurisdiction.

11. ENTIRE AGREEMENT
    This Agreement together with its Annexures constitutes the entire agreement
    between the parties and supersedes all prior discussions.

IN WITNESS WHEREOF the parties have signed this Agreement on the date first
written above.


For [COMPANY NAME]                            EMPLOYEE


____________________                          ____________________
[NAME], [DESIGNATION]                         [EMPLOYEE NAME]
""",
        "keywords": ["employment agreement", "employment contract", "job contract", "confidentiality", "ip assignment", "non solicitation"],
    },
    {
        "id": "internship-agreement",
        "title": "Internship Agreement",
        "category": "labour",
        "purpose": "Records the terms of a short, learning-focused engagement of a student.",
        "when_to_use": "Before a student or fresher starts an internship, paid or unpaid.",
        "checklist": [
            "Duration, working days and reporting mentor",
            "Whether a stipend is payable and how much",
            "Whether a certificate will be issued and on what conditions",
            "Confidentiality and ownership of work created during the internship",
        ],
        "stamp": "No stamp duty ordinarily. Sign in duplicate; the college may need a copy.",
        "body": """INTERNSHIP AGREEMENT

This Internship Agreement is made on [DATE] between:

[COMPANY NAME], having its office at [ADDRESS] (the "Company")

AND

[INTERN NAME], son/daughter of [FATHER'S NAME], a student of [COURSE] at
[COLLEGE/UNIVERSITY], residing at [ADDRESS] (the "Intern")

1.  ENGAGEMENT: The Company engages the Intern as an intern in the [DEPARTMENT]
    department for a period of [NUMBER] weeks/months, from [START DATE] to
    [END DATE].

2.  NATURE OF RELATIONSHIP: This is a training arrangement for the Intern's
    learning. It does not create an employer-employee relationship, and the
    Intern shall not be entitled to employment benefits. Nothing in this
    Agreement guarantees an offer of employment on completion.

3.  STIPEND: The Company shall pay a stipend of Rs. [AMOUNT]/- per month,
    payable by the [DAY] of the following month, subject to applicable
    deductions. [OR: This is an unpaid internship and no stipend is payable.]

4.  WORKING HOURS: [TIMINGS] on [DAYS]. The Intern shall inform the mentor in
    advance of any planned absence.

5.  MENTOR: The Intern shall work under the guidance of [MENTOR NAME],
    [DESIGNATION].

6.  CONFIDENTIALITY: The Intern shall keep confidential all information
    received during the internship, and shall not publish, post or share any
    Company data, code, designs or client information without written consent.
    This obligation continues after the internship ends.

7.  INTELLECTUAL PROPERTY: All work product created by the Intern during and in
    connection with the internship shall belong to the Company. The Intern may
    describe the work in general terms in a resume or portfolio only with the
    Company's written permission.

8.  CONDUCT: The Intern shall comply with the Company's code of conduct, IT
    policy and POSH policy, and shall behave professionally at all times.

9.  CERTIFICATE: On satisfactory completion of the full internship period, the
    Company shall issue an Internship Completion Certificate.

10. TERMINATION: Either party may terminate this Agreement by [NUMBER] days'
    written notice. The Company may terminate immediately for misconduct or
    breach of confidentiality.

11. COLLEGE REQUIREMENTS: The Company shall cooperate in providing such
    attendance records or evaluation forms as the Intern's institution
    reasonably requires.

12. GOVERNING LAW: This Agreement is governed by Indian law and the courts at
    [CITY] shall have jurisdiction.


For [COMPANY NAME]                            INTERN


____________________                          ____________________
[NAME], [DESIGNATION]                         [INTERN NAME]
""",
        "keywords": ["internship", "intern", "stipend", "training", "student", "certificate", "college internship"],
    },
    {
        "id": "resignation-letter",
        "title": "Resignation Letter",
        "category": "labour",
        "purpose": "Formally records that an employee is resigning and when the notice period starts.",
        "when_to_use": "When leaving a job; keep an acknowledged copy for your own protection.",
        "checklist": [
            "Your notice period as per the appointment letter",
            "Proposed last working day, counted from the date of this letter",
            "List of pending dues - salary, leave encashment, reimbursements, gratuity",
            "An email copy so the date of submission is provable",
        ],
        "stamp": "No stamp duty. Send by email and hand over a signed hard copy with acknowledgement.",
        "body": """RESIGNATION LETTER

Date: [DATE]

To,
[MANAGER NAME]
[DESIGNATION]
[COMPANY NAME]
[ADDRESS]

CC: Human Resources Department

Subject: Resignation from the post of [DESIGNATION] - Employee Code [CODE]

Dear [MANAGER NAME],

1.  I hereby tender my resignation from the post of [DESIGNATION] in the
    [DEPARTMENT] department of [COMPANY NAME], with effect from the close of
    business on [LAST WORKING DAY].

2.  As per Clause [NUMBER] of my appointment letter dated [DATE], my notice
    period is [NUMBER] days. Counted from the date of this letter, my last
    working day will therefore be [DATE].

3.  I shall ensure a complete and orderly handover of all my responsibilities,
    files, credentials and assets to [SUCCESSOR NAME / THE PERSON NOMINATED BY
    YOU] before my last working day, and I remain available for any transition
    support required during the notice period.

4.  I request you to kindly arrange for:
    (a) my full and final settlement, including salary up to the last working
        day, leave encashment, and reimbursement of pending claims;
    (b) my relieving letter and experience certificate;
    (c) Form 16 for the current financial year; and
    (d) the necessary documents for transfer or withdrawal of my Provident Fund
        and, where applicable, payment of gratuity.

5.  I would like to place on record my sincere thanks to you and to the
    organisation for the opportunities, guidance and support extended to me
    during my tenure of [DURATION]. The experience has been valuable to my
    professional growth.

Kindly acknowledge receipt of this letter.

Yours sincerely,


____________________
[EMPLOYEE NAME]
[DESIGNATION] | Employee Code: [CODE]
[PERSONAL EMAIL] | [PHONE]

Received by: ____________________   Date: ____________   (Company seal)
""",
        "keywords": ["resignation", "resign", "notice period", "relieving letter", "last working day", "full and final settlement"],
    },
    {
        "id": "posh-complaint",
        "title": "Complaint to the Internal Committee under the POSH Act",
        "category": "labour",
        "purpose": "Starts a formal workplace inquiry into sexual harassment.",
        "when_to_use": "Within three months of the incident, or of the last incident in a series.",
        "checklist": [
            "Dates, times and places of each incident, in order",
            "Names of the respondent and of any witnesses",
            "Copies of messages, emails, CCTV references or other supporting material",
            "Six copies of the complaint with the annexures, as the Rules require",
        ],
        "stamp": "No stamp duty. Submit to the Presiding Officer of the Internal Committee and keep an acknowledgement.",
        "body": """COMPLAINT UNDER SECTION 9 OF THE SEXUAL HARASSMENT OF WOMEN AT
WORKPLACE (PREVENTION, PROHIBITION AND REDRESSAL) ACT, 2013

To,
The Presiding Officer
Internal Committee
[COMPANY / INSTITUTION NAME]
[ADDRESS]

Date: [DATE]

Subject: Complaint of sexual harassment at the workplace

Respected Madam,

1.  COMPLAINANT DETAILS
    Name              : [YOUR NAME]
    Designation       : [DESIGNATION], [DEPARTMENT]
    Employee Code     : [CODE]
    Place of work     : [LOCATION]
    Contact           : [PHONE] | [EMAIL]

2.  RESPONDENT DETAILS
    Name              : [RESPONDENT NAME]
    Designation       : [DESIGNATION], [DEPARTMENT]
    Relationship      : [e.g. reporting manager / colleague / client
                        representative]

3.  PARTICULARS OF THE INCIDENT(S)
    (Set out each incident separately and in chronological order.)

    Incident 1
      Date and time   : [DATE], approximately [TIME]
      Place           : [PLACE]
      What happened   : [DESCRIBE FACTUALLY WHAT WAS SAID OR DONE, IN YOUR OWN
                        WORDS. AVOID CONCLUSIONS - DESCRIBE THE CONDUCT.]
      Persons present : [NAMES, IF ANY]

    Incident 2
      Date and time   : [DATE], approximately [TIME]
      Place           : [PLACE]
      What happened   : [DESCRIPTION]
      Persons present : [NAMES, IF ANY]

4.  EFFECT ON ME
    [Describe the effect on your work, health, attendance, or the hostile
    environment created - for example reassignment of work, exclusion from
    meetings, threats to your appraisal, or anxiety and inability to work.]

5.  EARLIER STEPS TAKEN
    [State whether you raised it with anyone earlier, when, and what happened.
    If you did not report earlier, you may briefly explain why.]

6.  SUPPORTING MATERIAL (ANNEXURES)
    Annexure 1 : [Screenshots of messages dated ...]
    Annexure 2 : [Email dated ...]
    Annexure 3 : [Any other document]

7.  WITNESSES
    (a) [NAME], [DESIGNATION], [CONTACT]
    (b) [NAME], [DESIGNATION], [CONTACT]

8.  RELIEF SOUGHT
    I request the Internal Committee to:
    (a) inquire into this complaint in accordance with the Act and the Rules;
    (b) during the pendency of the inquiry, grant interim relief by
        [transferring the respondent / transferring me at my request / granting
        me leave of up to three months / restraining the respondent from
        supervising or contacting me];
    (c) ensure that my identity and the contents of this complaint are kept
        confidential as required by Section 16 of the Act; and
    (d) take appropriate action against the respondent on the conclusion of the
        inquiry.

9.  I state that the contents of this complaint are true to the best of my
    knowledge and belief, and I am willing to depose before the Committee.

Yours faithfully,


____________________
[YOUR NAME]

Enclosures: As above (six copies submitted as required under Rule 6)
""",
        "keywords": ["posh", "sexual harassment", "internal committee", "workplace complaint", "ic", "2013 act", "harassment complaint"],
    },

    # ------------------------------------------------------------------
    # CONTRACTS AND BUSINESS
    # ------------------------------------------------------------------
    {
        "id": "nda",
        "title": "Non-Disclosure Agreement (NDA)",
        "category": "ipr",
        "purpose": "Protects confidential information shared between two parties.",
        "when_to_use": "Before pitching to an investor, engaging a vendor, or sharing any business secret.",
        "checklist": [
            "Whether the NDA needs to be one-way or mutual",
            "A clear definition of what counts as Confidential Information",
            "How long the obligation lasts after the discussions end",
            "What must be returned or deleted at the end",
        ],
        "stamp": "Usually executed on stamp paper of nominal value; the amount depends on the state.",
        "body": """MUTUAL NON-DISCLOSURE AGREEMENT

This Agreement is made on [DATE]

BETWEEN

[PARTY A NAME], having its address at [ADDRESS] ("Party A")

AND

[PARTY B NAME], having its address at [ADDRESS] ("Party B")

(each a "Party" and, where receiving information, the "Receiving Party", and
where disclosing information, the "Disclosing Party")

WHEREAS the Parties wish to explore [DESCRIBE THE PURPOSE, e.g. a potential
investment / a supply arrangement / a technology collaboration] (the "Purpose")
and, for that purpose, may disclose confidential information to each other:

1.  CONFIDENTIAL INFORMATION means all non-public information disclosed by one
    Party to the other, in any form, including business plans, financial data,
    customer and supplier lists, pricing, source code, algorithms, designs,
    processes, technical data, and the fact and content of the discussions
    themselves.

2.  EXCLUSIONS. Confidential Information does not include information which:
    (a) is or becomes public through no breach of this Agreement;
    (b) was already lawfully known to the Receiving Party without an obligation
        of confidence;
    (c) is independently developed without use of the Confidential Information;
        or
    (d) is lawfully received from a third party without restriction.

3.  OBLIGATIONS. The Receiving Party shall:
    (a) use the Confidential Information solely for the Purpose;
    (b) not disclose it to any third party without prior written consent;
    (c) disclose it internally only to those employees, directors, advisers and
        contractors who need to know it for the Purpose and who are bound by
        confidentiality obligations at least as protective as these; and
    (d) protect it using at least the same degree of care it uses for its own
        confidential information, and in no event less than reasonable care.

4.  COMPELLED DISCLOSURE. If the Receiving Party is required by law, court order
    or a regulator to disclose any Confidential Information, it shall, to the
    extent legally permitted, give prompt written notice to the Disclosing Party
    so that protective measures may be sought, and shall disclose only the
    minimum required.

5.  NO LICENCE. Nothing in this Agreement transfers any ownership, licence or
    intellectual property right. All Confidential Information remains the
    property of the Disclosing Party.

6.  TERM. This Agreement takes effect on the date above and continues for
    [NUMBER] years. The confidentiality obligations survive for [NUMBER] years
    from the date of disclosure, and indefinitely in respect of trade secrets
    and personal data.

7.  RETURN OR DESTRUCTION. On written request or on termination, the Receiving
    Party shall promptly return or destroy all Confidential Information and
    certify the destruction in writing, except for one archival copy retained
    solely for legal compliance.

8.  NO OBLIGATION TO PROCEED. Nothing in this Agreement obliges either Party to
    proceed with any transaction.

9.  REMEDIES. The Parties agree that damages alone may not be an adequate remedy
    for a breach, and that the Disclosing Party shall be entitled to seek
    injunctive relief in addition to any other remedy.

10. GOVERNING LAW AND DISPUTES. This Agreement is governed by the laws of India.
    Disputes shall be referred to a sole arbitrator under the Arbitration and
    Conciliation Act, 1996, seated at [CITY], with the courts at [CITY] having
    exclusive jurisdiction.

IN WITNESS WHEREOF the Parties have executed this Agreement on the date first
written above.


For [PARTY A]                                 For [PARTY B]


____________________                          ____________________
Name  : [NAME]                                Name  : [NAME]
Title : [DESIGNATION]                         Title : [DESIGNATION]
""",
        "keywords": ["nda", "non disclosure", "confidentiality agreement", "trade secret", "confidential", "mutual nda"],
    },
    {
        "id": "freelance-agreement",
        "title": "Freelance / Consultancy Services Agreement",
        "category": "contract",
        "purpose": "Governs a paid project done by an independent professional for a client.",
        "when_to_use": "Before starting any freelance design, development, writing or consulting project.",
        "checklist": [
            "A precise scope of work and list of deliverables",
            "Milestones, payment schedule and what happens on late payment",
            "Number of revision rounds included, and the rate for extra work",
            "Who owns the IP, and when ownership passes",
        ],
        "stamp": "Nominal stamp paper as per state practice; an email exchange confirming the terms also helps.",
        "body": """SERVICES AGREEMENT (FREELANCE / CONSULTANCY)

This Agreement is made on [DATE]

BETWEEN

[CLIENT NAME], having its address at [ADDRESS] (the "Client")

AND

[FREELANCER NAME], residing at [ADDRESS], PAN [PAN]
(the "Consultant")

1.  SERVICES
    1.1 The Consultant shall provide the services and deliverables described in
        Annexure A (the "Services").
    1.2 Anything not expressly listed in Annexure A is outside scope and shall be
        chargeable separately at Rs. [AMOUNT] per [HOUR/DAY], subject to prior
        written approval.

2.  TERM AND TIMELINES
    2.1 This Agreement commences on [START DATE] and continues until the
        Services are completed or until [END DATE], unless terminated earlier.
    2.2 The milestones and delivery dates are set out in Annexure A. Timelines
        shall be extended by any period of delay caused by the Client's failure
        to provide inputs, approvals or access.

3.  FEES AND PAYMENT
    3.1 The total fee is Rs. [AMOUNT]/- (Rupees [IN WORDS] only), exclusive of
        applicable taxes.
    3.2 Payment schedule:
          [PERCENTAGE]% advance on signing        Rs. [AMOUNT]
          [PERCENTAGE]% on [MILESTONE]            Rs. [AMOUNT]
          [PERCENTAGE]% on final delivery         Rs. [AMOUNT]
    3.3 Invoices are payable within [NUMBER] days. Delayed payment carries
        interest at [PERCENTAGE]% per month.
    3.4 Reasonable out-of-pocket expenses pre-approved in writing shall be
        reimbursed at actuals against receipts.
    3.5 Tax shall be deducted at source as required by law, and the Client shall
        issue the TDS certificate.

4.  REVISIONS
    The fee includes [NUMBER] rounds of revision per deliverable. Further
    revisions shall be charged at Rs. [AMOUNT] per round.

5.  INDEPENDENT CONTRACTOR
    The Consultant is an independent contractor and not an employee, partner or
    agent of the Client. The Consultant is responsible for her/his own taxes and
    statutory contributions and shall not claim employment benefits.

6.  INTELLECTUAL PROPERTY
    6.1 On receipt of full payment, all intellectual property rights in the
        deliverables shall vest in the Client, and the Consultant assigns those
        rights accordingly.
    6.2 The Consultant retains ownership of pre-existing tools, libraries and
        know-how, and grants the Client a perpetual, non-exclusive licence to use
        them to the extent embedded in the deliverables.
    6.3 The Consultant may display the work in a portfolio, unless the Client
        notifies otherwise in writing.

7.  CONFIDENTIALITY
    Each party shall keep the other's confidential information secret and use it
    only for this engagement, both during and for [NUMBER] years after the term.

8.  WARRANTIES
    The Consultant warrants that the deliverables are original, do not infringe
    any third-party rights, and shall be performed with reasonable skill and
    care in accordance with industry standards.

9.  LIMITATION OF LIABILITY
    Except for breach of confidentiality, infringement of intellectual property
    or wilful misconduct, the total liability of either party shall not exceed
    the total fees paid under this Agreement.

10. TERMINATION
    10.1 Either party may terminate on [NUMBER] days' written notice.
    10.2 Either party may terminate immediately on a material breach not cured
         within [NUMBER] days of written notice.
    10.3 On termination, the Client shall pay for all work completed and work in
         progress up to the date of termination.

11. GOVERNING LAW AND DISPUTES
    Indian law governs this Agreement. Disputes shall be resolved by arbitration
    by a sole arbitrator under the Arbitration and Conciliation Act, 1996,
    seated at [CITY]. Courts at [CITY] shall have exclusive jurisdiction.


For the Client                                Consultant


____________________                          ____________________
[NAME], [DESIGNATION]                         [NAME]
""",
        "keywords": ["freelance", "consultancy", "services agreement", "contractor", "scope of work", "milestone", "invoice", "project agreement"],
    },
    {
        "id": "mou",
        "title": "Memorandum of Understanding (MoU)",
        "category": "contract",
        "purpose": "Records the shared understanding of two parties before a binding contract is signed.",
        "when_to_use": "At the start of a collaboration, partnership discussion or institutional tie-up.",
        "checklist": [
            "Whether the parties intend it to be binding, non-binding, or partly binding",
            "The objective of the collaboration in concrete terms",
            "Who does what, who pays what, and for how long",
            "An exit clause and a confidentiality clause, which should always be binding",
        ],
        "stamp": "Nominal stamp paper. Say clearly which clauses are binding, or disputes will follow.",
        "body": """MEMORANDUM OF UNDERSTANDING

This Memorandum of Understanding ("MoU") is entered into on [DATE] at [CITY]

BETWEEN

[PARTY A NAME], [DESCRIPTION - e.g. a company incorporated under the Companies
Act, 2013 / an educational institution], having its office at [ADDRESS]
("First Party")

AND

[PARTY B NAME], [DESCRIPTION], having its office at [ADDRESS] ("Second Party")

(individually a "Party" and collectively the "Parties")

BACKGROUND
A.  The First Party is engaged in [DESCRIBE ACTIVITY].
B.  The Second Party is engaged in [DESCRIBE ACTIVITY].
C.  The Parties wish to record their understanding in relation to
    [DESCRIBE THE PROPOSED COLLABORATION].

NOW THE PARTIES RECORD THEIR UNDERSTANDING AS FOLLOWS:

1.  OBJECTIVE
    The Parties intend to collaborate for the purpose of [STATE THE OBJECTIVE
    SPECIFICALLY].

2.  ROLE OF THE FIRST PARTY
    2.1 [RESPONSIBILITY]
    2.2 [RESPONSIBILITY]
    2.3 [RESPONSIBILITY]

3.  ROLE OF THE SECOND PARTY
    3.1 [RESPONSIBILITY]
    3.2 [RESPONSIBILITY]
    3.3 [RESPONSIBILITY]

4.  FINANCIAL ARRANGEMENT
    4.1 Each Party shall bear its own costs unless otherwise agreed in writing.
    4.2 [OR SET OUT THE AGREED SHARING OF COSTS AND REVENUE.]

5.  TERM
    This MoU shall be effective from [DATE] and shall remain in force for
    [NUMBER] years, unless extended by mutual written agreement or terminated
    earlier.

6.  BINDING NATURE
    6.1 Clauses 7 (Confidentiality), 8 (Intellectual Property), 9 (Termination)
        and 11 (Governing Law) are legally binding on the Parties.
    6.2 The remaining clauses record the Parties' present intention and are not
        intended to create legally enforceable obligations. A definitive
        agreement shall be executed to give effect to the collaboration.

7.  CONFIDENTIALITY
    Each Party shall keep confidential all non-public information received from
    the other and shall use it only for the Objective, during the term and for
    [NUMBER] years afterwards.

8.  INTELLECTUAL PROPERTY
    Each Party retains ownership of its pre-existing intellectual property.
    Ownership of any jointly created intellectual property shall be dealt with
    in the definitive agreement, and until then shall be jointly owned.

9.  TERMINATION
    Either Party may terminate this MoU by giving [NUMBER] days' prior written
    notice. Termination shall not affect the confidentiality obligations or any
    accrued rights.

10. NO EXCLUSIVITY AND NO AGENCY
    This MoU does not create any exclusivity, partnership, joint venture, or
    agency between the Parties, and neither Party may bind the other.

11. GOVERNING LAW AND DISPUTES
    This MoU is governed by Indian law. Disputes shall first be resolved by
    discussion between senior representatives, and failing that by arbitration
    under the Arbitration and Conciliation Act, 1996, seated at [CITY].

IN WITNESS WHEREOF the Parties have signed this MoU on the date first written
above.


For the First Party                           For the Second Party


____________________                          ____________________
Name  : [NAME]                                Name  : [NAME]
Title : [DESIGNATION]                         Title : [DESIGNATION]

WITNESSES:
1. ____________________                       2. ____________________
""",
        "keywords": ["mou", "memorandum of understanding", "collaboration", "partnership", "tie up", "non binding"],
    },
    {
        "id": "partnership-deed",
        "title": "Partnership Deed",
        "category": "corporate",
        "purpose": "Sets out the terms on which two or more people run a business together as a firm.",
        "when_to_use": "When forming a partnership firm, before applying for registration and a PAN.",
        "checklist": [
            "Name and place of business of the firm",
            "Capital contributed by each partner and the profit-sharing ratio",
            "Whether any partner will draw a salary or interest on capital",
            "What happens on death, retirement or admission of a partner",
        ],
        "stamp": (
            "Executed on stamp paper of the value prescribed by the state. Registration with the "
            "Registrar of Firms is optional but strongly advised - an unregistered firm cannot "
            "file a suit to enforce a contractual right."
        ),
        "body": """PARTNERSHIP DEED

This Deed of Partnership is made at [CITY] on this [DAY] day of [MONTH], [YEAR]

BETWEEN

1.  [PARTNER 1 NAME], aged [AGE] years, son/daughter of [FATHER'S NAME],
    residing at [ADDRESS], PAN [PAN]              ... First Party
2.  [PARTNER 2 NAME], aged [AGE] years, son/daughter of [FATHER'S NAME],
    residing at [ADDRESS], PAN [PAN]              ... Second Party
3.  [PARTNER 3 NAME], aged [AGE] years, son/daughter of [FATHER'S NAME],
    residing at [ADDRESS], PAN [PAN]              ... Third Party

(hereinafter collectively called the "Partners")

WHEREAS the Partners have agreed to carry on business in partnership on the
terms recorded below:

1.  NAME OF THE FIRM
    The business shall be carried on under the name and style of
    "M/s [FIRM NAME]" (the "Firm").

2.  PRINCIPAL PLACE OF BUSINESS
    The Firm shall carry on business at [ADDRESS], and at such other places as
    the Partners may agree.

3.  BUSINESS
    The Firm shall carry on the business of [DESCRIBE THE BUSINESS], and any
    other business the Partners may unanimously agree to undertake.

4.  COMMENCEMENT AND DURATION
    The partnership shall commence on [DATE] and shall be a partnership at will,
    continuing until dissolved as provided in this Deed.

5.  CAPITAL
    5.1 The initial capital of the Firm shall be Rs. [AMOUNT]/-, contributed as:
            [PARTNER 1]  Rs. [AMOUNT]
            [PARTNER 2]  Rs. [AMOUNT]
            [PARTNER 3]  Rs. [AMOUNT]
    5.2 Interest at [PERCENTAGE]% per annum shall be payable on the capital
        standing to the credit of each Partner, subject to the limits allowed
        under the Income-tax Act, 1961.

6.  PROFIT AND LOSS SHARING
    The net profits and losses of the Firm shall be shared as follows:
            [PARTNER 1]  [PERCENTAGE]%
            [PARTNER 2]  [PERCENTAGE]%
            [PARTNER 3]  [PERCENTAGE]%

7.  REMUNERATION
    The working partners, namely [NAMES], shall be entitled to remuneration as
    may be mutually agreed, computed within the limits prescribed under Section
    40(b) of the Income-tax Act, 1961.

8.  BANK ACCOUNT
    The Firm shall open a bank account with [BANK NAME], operated jointly by
    [NAMES] / severally by any one Partner.

9.  BOOKS OF ACCOUNT
    Proper books of account shall be maintained at the principal place of
    business and shall be open to inspection by every Partner. Accounts shall be
    closed on 31st March each year.

10. DUTIES OF PARTNERS
    Every Partner shall be just and faithful to the others, shall devote such
    time and attention to the business as is necessary, and shall not without
    the consent of the others:
        (a) lend money or give credit of the Firm to any person of doubtful
            solvency;
        (b) stand surety for any person on behalf of the Firm;
        (c) engage in any competing business; or
        (d) transfer or charge her/his share in the Firm.

11. ADMISSION, RETIREMENT AND DEATH
    11.1 A new partner may be admitted only with the written consent of all
         existing Partners.
    11.2 A Partner may retire by giving [NUMBER] months' written notice, and
         shall be paid the amount standing to her/his credit after taking
         accounts.
    11.3 On the death of a Partner, the Firm shall not be dissolved, and the
         surviving Partners may continue the business, paying the deceased
         Partner's legal heirs the amount due on the date of death.

12. DISSOLUTION
    On dissolution, the assets shall be applied first in paying the debts and
    liabilities of the Firm, then in repaying capital, and the surplus shall be
    divided in the profit-sharing ratio.

13. ARBITRATION
    Any dispute between the Partners shall be referred to a sole arbitrator
    under the Arbitration and Conciliation Act, 1996, seated at [CITY].

IN WITNESS WHEREOF the Partners have signed this Deed on the day, month and year
first above written.


____________________   ____________________   ____________________
[PARTNER 1]            [PARTNER 2]            [PARTNER 3]

WITNESSES:
1. ____________________                       2. ____________________
""",
        "keywords": ["partnership deed", "partnership firm", "partners", "profit sharing", "capital", "registrar of firms"],
    },
    {
        "id": "founders-agreement-doc",
        "title": "Founders Agreement",
        "category": "startup",
        "purpose": "Fixes equity, roles, vesting and exit rules between startup co-founders.",
        "when_to_use": "As early as possible - ideally before the company is even incorporated.",
        "checklist": [
            "Agreed equity split and the reasoning behind it",
            "Vesting schedule and cliff for each founder",
            "Who is full-time, who is part-time, and what the expectations are",
            "What happens to shares if a founder leaves, is removed, or dies",
        ],
        "stamp": "Nominal stamp paper. The key restrictions should also be written into the Articles of Association.",
        "body": """FOUNDERS AGREEMENT

This Founders Agreement is made on [DATE] at [CITY]

AMONG

1.  [FOUNDER 1 NAME], residing at [ADDRESS]                ("Founder 1")
2.  [FOUNDER 2 NAME], residing at [ADDRESS]                ("Founder 2")
3.  [FOUNDER 3 NAME], residing at [ADDRESS]                ("Founder 3")

(collectively the "Founders")

AND

[COMPANY NAME], a company incorporated under the Companies Act, 2013, having its
registered office at [ADDRESS] (the "Company")

1.  BUSINESS
    The Founders shall carry on the business of [DESCRIBE THE BUSINESS] through
    the Company.

2.  EQUITY SHAREHOLDING
    The issued share capital of the Company shall be held as follows:
        Founder 1  : [PERCENTAGE]%    ([NUMBER] equity shares)
        Founder 2  : [PERCENTAGE]%    ([NUMBER] equity shares)
        Founder 3  : [PERCENTAGE]%    ([NUMBER] equity shares)
        ESOP Pool  : [PERCENTAGE]%    (to be created and administered by the
                                       Board)

3.  ROLES AND COMMITMENT
        Founder 1  : [TITLE] - responsible for [AREAS] - [FULL TIME / PART TIME]
        Founder 2  : [TITLE] - responsible for [AREAS] - [FULL TIME / PART TIME]
        Founder 3  : [TITLE] - responsible for [AREAS] - [FULL TIME / PART TIME]
    Each full-time Founder shall devote her/his entire professional time to the
    Company and shall not take up any other employment or engagement without the
    written consent of the other Founders.

4.  VESTING
    4.1 The shares held by each Founder shall vest over [NUMBER] years, with a
        cliff of [NUMBER] months.
    4.2 No shares vest if a Founder leaves before the cliff. After the cliff,
        [FRACTION] vests on the cliff date and the balance vests monthly in
        equal instalments over the remaining period.
    4.3 Unvested shares of a departing Founder shall be transferred to the
        Company or to the continuing Founders at par value.
    4.4 On a change of control, [ALL / NUMBER PER CENT] of the unvested shares
        shall accelerate.

5.  GOOD LEAVER AND BAD LEAVER
    5.1 A "Good Leaver" is a Founder who leaves due to death, permanent
        disability, or by mutual consent. A Good Leaver retains vested shares.
    5.2 A "Bad Leaver" is a Founder who resigns before the agreed commitment
        period without consent, or is removed for fraud, wilful misconduct or
        material breach. A Bad Leaver shall transfer [PERCENTAGE]% of even the
        vested shares at par value.

6.  INTELLECTUAL PROPERTY
    Each Founder assigns to the Company all intellectual property created by
    her/him relating to the business, whether created before or after
    incorporation, and shall execute all documents needed to perfect the
    assignment.

7.  DECISION MAKING
    7.1 Day-to-day decisions shall be taken by the Founder responsible for that
        function.
    7.2 The following require the unanimous written consent of all Founders:
        (a) issue of shares or any change in capital structure;
        (b) borrowing above Rs. [AMOUNT];
        (c) sale of the business or any material asset;
        (d) appointment or removal of a director;
        (e) any related-party transaction;
        (f) change in the nature of the business; and
        (g) winding up of the Company.

8.  TRANSFER RESTRICTIONS
    8.1 No Founder shall transfer any shares without first offering them to the
        other Founders on the same terms (Right of First Refusal).
    8.2 Tag-along and drag-along rights shall apply as set out in Annexure A.

9.  CONFIDENTIALITY AND NON-SOLICITATION
    Each Founder shall keep the Company's information confidential, and shall
    not for [NUMBER] months after ceasing to be associated with the Company
    solicit its employees, customers or vendors. The Founders acknowledge that a
    post-exit restraint on carrying on a trade would be void under Section 27 of
    the Indian Contract Act, 1872.

10. DEADLOCK
    If the Founders are unable to agree on a reserved matter for [NUMBER] days,
    the matter shall be referred to a mutually appointed mediator, and failing
    resolution, to arbitration under Clause 11.

11. GOVERNING LAW AND DISPUTES
    Indian law governs this Agreement. Disputes shall be referred to a sole
    arbitrator under the Arbitration and Conciliation Act, 1996, seated at
    [CITY].

12. ARTICLES OF ASSOCIATION
    The Founders shall procure that the Articles of Association of the Company
    are amended to incorporate the restrictions in Clauses 4, 5 and 8, and in
    the event of any inconsistency the Articles shall be amended to give effect
    to this Agreement.

IN WITNESS WHEREOF the parties have signed this Agreement on the date first
written above.


____________________   ____________________   ____________________
[FOUNDER 1]            [FOUNDER 2]            [FOUNDER 3]

For [COMPANY NAME]
____________________
Authorised Signatory
""",
        "keywords": ["founders agreement", "co founder", "vesting", "cliff", "equity split", "esop", "startup agreement", "good leaver"],
    },
    {
        "id": "vendor-agreement",
        "title": "Vendor / Supply Agreement",
        "category": "contract",
        "purpose": "Governs the ongoing supply of goods or services by a vendor to a buyer.",
        "when_to_use": "Before placing repeat purchase orders on a supplier.",
        "checklist": [
            "Specification, quality standard and inspection rights",
            "Price, taxes, payment terms and price revision mechanism",
            "Delivery schedule, place of delivery and when risk passes",
            "Warranty period, rejection procedure and penalty for delay",
        ],
        "stamp": "Nominal stamp paper as per state practice; annex the specification and rate card.",
        "body": """VENDOR / SUPPLY AGREEMENT

This Agreement is made on [DATE]

BETWEEN

[BUYER NAME], having its office at [ADDRESS], GSTIN [GSTIN] (the "Buyer")

AND

[VENDOR NAME], having its office at [ADDRESS], GSTIN [GSTIN] (the "Vendor")

1.  SCOPE
    The Vendor shall supply the goods and/or services described in Annexure A
    (the "Products") in accordance with the specifications in Annexure B, on the
    basis of Purchase Orders issued by the Buyer from time to time.

2.  PURCHASE ORDERS
    2.1 Each Purchase Order shall specify the quantity, specification, price,
        delivery date and place of delivery.
    2.2 The Vendor shall acknowledge each Purchase Order within [NUMBER] working
        days. The terms of this Agreement shall prevail over any printed terms
        on the Vendor's invoice or acknowledgement.

3.  PRICE AND PAYMENT
    3.1 Prices shall be as per the rate card in Annexure C and shall remain firm
        for [NUMBER] months.
    3.2 Prices are exclusive of GST, which shall be charged at the applicable
        rate on a valid tax invoice.
    3.3 Payment shall be made within [NUMBER] days of receipt of a correct
        invoice and satisfactory delivery.
    3.4 If the Vendor is a micro or small enterprise registered under the MSMED
        Act, 2006, payment shall be made within 45 days of acceptance as
        required by that Act.

4.  DELIVERY
    4.1 Delivery shall be made at [PLACE] on or before the date in the Purchase
        Order. Time is of the essence.
    4.2 Risk in the Products shall pass on delivery and acceptance; title shall
        pass on delivery or payment, whichever is earlier.
    4.3 Delay beyond [NUMBER] days shall attract liquidated damages of
        [PERCENTAGE]% of the value of the delayed Products per week, subject to a
        maximum of [PERCENTAGE]%.

5.  INSPECTION AND REJECTION
    5.1 The Buyer may inspect the Products within [NUMBER] days of delivery.
    5.2 Products not conforming to specification may be rejected by written
        notice, and the Vendor shall replace them at its own cost within
        [NUMBER] days and collect the rejected goods.

6.  WARRANTY
    The Vendor warrants that the Products shall be new, free from defects in
    material and workmanship, conform to the specification, and comply with all
    applicable laws, for a period of [NUMBER] months from delivery.

7.  INDEMNITY
    The Vendor shall indemnify the Buyer against all claims, losses and expenses
    arising from defective Products, breach of warranty, or infringement of any
    third-party intellectual property right.

8.  COMPLIANCE
    The Vendor shall comply with all applicable labour, environmental, safety and
    anti-bribery laws, and shall not employ child labour.

9.  CONFIDENTIALITY
    Each party shall keep the other's confidential information secret during the
    term and for [NUMBER] years afterwards.

10. TERM AND TERMINATION
    10.1 This Agreement shall be valid for [NUMBER] years from [DATE], renewable
         by written agreement.
    10.2 Either party may terminate for convenience on [NUMBER] days' notice, or
         immediately for a material breach not cured within [NUMBER] days.
    10.3 Termination shall not affect Purchase Orders already accepted, unless
         the parties agree otherwise.

11. GOVERNING LAW AND DISPUTES
    Indian law governs this Agreement. Disputes shall be referred to arbitration
    by a sole arbitrator under the Arbitration and Conciliation Act, 1996,
    seated at [CITY], and the courts at [CITY] shall have exclusive
    jurisdiction.


For the Buyer                                 For the Vendor


____________________                          ____________________
[NAME], [DESIGNATION]                         [NAME], [DESIGNATION]
""",
        "keywords": ["vendor agreement", "supply agreement", "purchase order", "supplier", "delivery", "msme payment", "rate card"],
    },
    {
        "id": "ip-assignment",
        "title": "Intellectual Property Assignment Agreement",
        "category": "ipr",
        "purpose": "Transfers ownership of copyright, designs or other IP from a creator to a company.",
        "when_to_use": "With every founder, employee, freelancer and agency who creates anything for the business.",
        "checklist": [
            "A precise description of the works being assigned",
            "Whether the assignment is worldwide, perpetual and for all media",
            "Waiver of moral rights to the extent permitted by law",
            "Consideration - even a nominal sum should be recited and paid",
        ],
        "stamp": "Nominal stamp paper. For registered IP, also file the assignment with the relevant registry.",
        "body": """INTELLECTUAL PROPERTY ASSIGNMENT AGREEMENT

This Agreement is made on [DATE]

BETWEEN

[ASSIGNOR NAME], residing at [ADDRESS] (the "Assignor")

AND

[ASSIGNEE / COMPANY NAME], having its registered office at [ADDRESS]
(the "Assignee")

WHEREAS the Assignor has created or will create the works described in the
Schedule (the "Works") for or in connection with the Assignee's business, and
the parties wish to record the transfer of all rights in the Works to the
Assignee:

1.  ASSIGNMENT
    In consideration of the sum of Rs. [AMOUNT]/- and the other benefits
    received by the Assignor (the receipt of which is acknowledged), the
    Assignor hereby irrevocably assigns to the Assignee, absolutely and
    throughout the world, all right, title and interest in and to the Works,
    including all copyright, design rights, database rights, trade marks,
    patents and any other intellectual property rights in them, for the full
    term of those rights and any renewals or extensions.

2.  SCOPE
    The assignment covers all media and formats, whether now known or later
    developed, and includes the right to reproduce, adapt, translate, modify,
    publish, distribute, communicate to the public and sub-licence the Works.

3.  FUTURE WORKS
    This assignment extends to all Works created by the Assignor for the
    Assignee during the period from [START DATE] to [END DATE], and the Assignor
    agrees to execute a confirmatory assignment for any such Work on request.

4.  MORAL RIGHTS
    To the extent permitted by law, the Assignor waives all moral rights in the
    Works, save that the Assignee shall use reasonable efforts to credit the
    Assignor where it is customary to do so.

5.  WARRANTIES
    The Assignor warrants that:
    (a) she/he is the sole author and owner of the Works;
    (b) the Works are original and do not infringe the rights of any third
        party;
    (c) the Works are free from any encumbrance, licence or claim; and
    (d) no part of the Works was created using any third-party material except
        as disclosed in the Schedule with the applicable licence terms.

6.  FURTHER ASSURANCE
    The Assignor shall, at the Assignee's cost, execute all documents and do all
    acts reasonably required to perfect, register or enforce the Assignee's
    rights in the Works, including filings before the Copyright Office, the
    Trade Marks Registry or the Patent Office.

7.  DELIVERY
    The Assignor shall deliver to the Assignee all source files, working files,
    documentation and passwords relating to the Works, and shall retain no
    copies except as permitted in writing.

8.  INDEMNITY
    The Assignor shall indemnify the Assignee against all losses arising from a
    breach of the warranties in Clause 5.

9.  GOVERNING LAW
    This Agreement is governed by Indian law, and the courts at [CITY] shall
    have exclusive jurisdiction.

SCHEDULE - DESCRIPTION OF THE WORKS
[LIST EACH WORK: e.g. the logo, the website design, the source code of the
mobile application, the product photographs, the written content, together with
dates of creation.]

THIRD-PARTY MATERIAL USED (if any)
[LIST, WITH THE LICENCE UNDER WHICH IT IS USED.]


____________________                          ____________________
ASSIGNOR                                      For the ASSIGNEE
[NAME]                                        [NAME], [DESIGNATION]

WITNESSES:
1. ____________________                       2. ____________________
""",
        "keywords": ["ip assignment", "copyright assignment", "intellectual property", "transfer of rights", "moral rights", "work for hire"],
    },
    {
        "id": "board-resolution",
        "title": "Board Resolution (Template)",
        "category": "corporate",
        "purpose": "Records a decision formally taken by the Board of Directors of a company.",
        "when_to_use": "For opening a bank account, appointing a signatory, borrowing, or any Board decision.",
        "checklist": [
            "Correct company name, CIN and registered office",
            "Date, time and place of the meeting, and the quorum present",
            "The exact wording of the decision, including names and limits",
            "Certification by a director or the company secretary",
        ],
        "stamp": "No stamp duty. Keep it in the minutes book; banks usually want a certified true copy.",
        "body": """CERTIFIED TRUE COPY OF THE RESOLUTION PASSED AT THE MEETING OF THE
BOARD OF DIRECTORS OF [COMPANY NAME] (CIN: [CIN]) HELD ON [DATE] AT [TIME]
AT THE REGISTERED OFFICE OF THE COMPANY AT [ADDRESS]

DIRECTORS PRESENT:
1. [NAME], [DESIGNATION] - in the Chair
2. [NAME], [DESIGNATION]
3. [NAME], [DESIGNATION]

The Chairperson informed the Board of the proposal placed before it. After
discussion, the following resolution was passed unanimously:

--- RESOLUTION 1: OPENING OF A BANK ACCOUNT ---

"RESOLVED THAT a Current Account be opened in the name of the Company with
[BANK NAME], [BRANCH ADDRESS], and that the said bank be and is hereby
requested to honour cheques, bills of exchange and other negotiable instruments
drawn, accepted or made on behalf of the Company.

RESOLVED FURTHER THAT the said account be operated by [NAME], [DESIGNATION] and
[NAME], [DESIGNATION], [JOINTLY / SEVERALLY / ANY ONE OF THEM], up to a limit of
Rs. [AMOUNT] per transaction.

RESOLVED FURTHER THAT [NAME], [DESIGNATION] be and is hereby authorised to sign
and execute the account opening forms and all other documents required by the
bank, and to do all such acts, deeds and things as may be necessary to give
effect to this resolution."

--- RESOLUTION 2: AUTHORISED SIGNATORY ---

"RESOLVED THAT [NAME], [DESIGNATION] be and is hereby authorised, on behalf of
the Company, to:
    (a) sign, execute and deliver [DESCRIBE - e.g. the Services Agreement with
        M/s [NAME] dated [DATE]];
    (b) negotiate and agree the commercial terms thereof within a value of
        Rs. [AMOUNT];
    (c) sign all correspondence, applications, undertakings and declarations in
        connection therewith; and
    (d) do all such acts and things as may be necessary or incidental to give
        effect to this resolution;

and that all acts done by the said authorised person pursuant to this
resolution be and are hereby ratified and confirmed."

--- RESOLUTION 3: CERTIFICATION ---

"RESOLVED FURTHER THAT a certified true copy of this resolution be furnished to
such persons and authorities as may be required, under the signature of any
Director or the Company Secretary of the Company."

There being no other business, the meeting concluded with a vote of thanks to
the Chair.

CERTIFIED TRUE COPY
For [COMPANY NAME]


____________________
[NAME]
[DIRECTOR / COMPANY SECRETARY]
DIN / Membership No.: [NUMBER]
Date: [DATE]
Place: [CITY]
(Company Seal)
""",
        "keywords": ["board resolution", "resolution", "director", "authorised signatory", "bank account opening", "certified true copy"],
    },

    # ------------------------------------------------------------------
    # NOTICES, COMPLAINTS AND APPLICATIONS
    # ------------------------------------------------------------------
    {
        "id": "legal-notice",
        "title": "General Legal Notice",
        "category": "civil",
        "purpose": "A formal written demand sent before filing a case, giving the other side a last chance.",
        "when_to_use": "Before almost any civil suit; it is mandatory against the government under Section 80 CPC.",
        "checklist": [
            "The full facts in date order, with amounts and document references",
            "The exact legal right that has been violated",
            "A specific demand and a deadline (usually 15 or 30 days)",
            "Proof of dispatch - registered post AD receipt and tracking printout",
        ],
        "stamp": "No stamp duty. Send by registered post AD and email; keep the receipts carefully.",
        "body": """LEGAL NOTICE

[ADVOCATE'S LETTERHEAD, OR SEND IN YOUR OWN NAME]

Ref: [REFERENCE NUMBER]
Date: [DATE]

BY REGISTERED POST WITH ACKNOWLEDGEMENT DUE AND BY EMAIL

To,
[NAME OF THE ADDRESSEE]
[COMPLETE ADDRESS]
[EMAIL]

Subject: Legal notice for [STATE THE GRIEVANCE IN ONE LINE, e.g. recovery of
Rs. [AMOUNT] with interest / breach of agreement dated [DATE]]

Dear Sir/Madam,

Under instructions from and on behalf of my client, [CLIENT NAME], residing at
[ADDRESS] (hereinafter "my client"), I hereby serve upon you the following
legal notice:

1.  That my client and you entered into [DESCRIBE THE TRANSACTION OR
    RELATIONSHIP] on [DATE], whereby it was agreed that [SET OUT THE AGREED
    TERMS].

2.  That in pursuance of the said agreement, my client [DESCRIBE WHAT YOUR SIDE
    PERFORMED - e.g. delivered the goods / paid the advance of Rs. [AMOUNT] vide
    [REFERENCE] dated [DATE] / completed and handed over the work].

3.  That you, however, have failed and neglected to [DESCRIBE THE DEFAULT - e.g.
    pay the balance consideration of Rs. [AMOUNT] / deliver the goods / vacate
    the premises], despite repeated oral requests and reminders sent on [DATES].

4.  That your aforesaid acts and omissions amount to a clear breach of the
    agreement dated [DATE] and have caused my client severe financial loss,
    hardship and mental agony.

5.  That my client has been left with no option but to issue this notice.

NOW, THEREFORE, I, through this notice, call upon you to:

    (a) pay to my client a sum of Rs. [AMOUNT]/- (Rupees [IN WORDS] only) being
        [DESCRIBE THE PRINCIPAL], together with interest at [PERCENTAGE]% per
        annum from [DATE] till realisation;
    (b) [ANY OTHER SPECIFIC RELIEF - e.g. hand over possession / deliver the
        goods / withdraw the defamatory post];
    (c) pay a sum of Rs. [AMOUNT]/- towards the cost of this notice;

all within [NUMBER] DAYS of the receipt of this notice, failing which my client
shall be constrained to initiate appropriate civil and/or criminal proceedings
against you before the competent court, entirely at your risk as to costs and
consequences, and you shall be liable for all costs of such litigation.

A copy of this notice is retained in my office for record and further necessary
action.

Yours faithfully,


____________________
[ADVOCATE NAME]
Advocate
Enrolment No.: [NUMBER]
[ADDRESS] | [PHONE] | [EMAIL]
""",
        "keywords": ["legal notice", "notice", "demand notice", "before suit", "advocate notice", "recovery notice", "section 80"],
    },
    {
        "id": "cheque-bounce-notice",
        "title": "Cheque Bounce Demand Notice (Section 138 NI Act)",
        "category": "banking",
        "purpose": "The mandatory notice that must be sent before filing a cheque dishonour complaint.",
        "when_to_use": "Within 30 days of receiving the bank's cheque return memo. This deadline is fatal if missed.",
        "checklist": [
            "The original cheque and the bank's return memo with the reason for dishonour",
            "Proof of the underlying debt - invoice, agreement, loan record",
            "The drawer's correct current address",
            "Registered post AD receipt, tracking printout, and the returned envelope if undelivered",
        ],
        "stamp": (
            "No stamp duty. TIMELINE: notice within 30 days of the return memo; the drawer gets "
            "15 days to pay; the complaint must be filed within the following 30 days."
        ),
        "body": """LEGAL NOTICE UNDER SECTION 138 OF THE NEGOTIABLE INSTRUMENTS ACT, 1881

Ref: [REFERENCE NUMBER]
Date: [DATE]

BY REGISTERED POST WITH ACKNOWLEDGEMENT DUE AND BY EMAIL

To,
[DRAWER NAME]
[COMPLETE ADDRESS]
[EMAIL]

Subject: Notice of demand for payment of Rs. [AMOUNT]/- on dishonour of Cheque
No. [CHEQUE NUMBER] dated [CHEQUE DATE]

Sir/Madam,

Under instructions from my client, [PAYEE NAME], residing/having its office at
[ADDRESS], I serve upon you the following notice:

1.  That you are well acquainted with my client, and in discharge of a legally
    enforceable debt/liability arising out of [DESCRIBE - e.g. the loan of
    Rs. [AMOUNT] advanced on [DATE] / the goods supplied under Invoice No.
    [NUMBER] dated [DATE] / the services rendered under Agreement dated [DATE]],
    you issued the following cheque in favour of my client:

        Cheque Number   : [NUMBER]
        Cheque Date     : [DATE]
        Amount          : Rs. [AMOUNT]/- (Rupees [IN WORDS] only)
        Drawn on        : [BANK NAME], [BRANCH]
        Account Number  : [ACCOUNT NUMBER]

2.  That my client, on the assurance given by you, presented the said cheque for
    encashment through its banker, [BANK NAME], [BRANCH], on [DATE].

3.  That the said cheque was returned unpaid by your banker with the remark
    "[REASON - e.g. FUNDS INSUFFICIENT / ACCOUNT CLOSED / PAYMENT STOPPED]" vide
    Return Memo dated [DATE], which was received by my client on [DATE]. A copy
    of the return memo is enclosed.

4.  That on receiving the information of dishonour, my client contacted you on
    [DATES] and called upon you to make the payment, but you have failed to do
    so.

5.  That by issuing the said cheque which was dishonoured for want of sufficient
    funds, you have committed an offence punishable under Section 138 of the
    Negotiable Instruments Act, 1881, with imprisonment for a term which may
    extend to two years, or with fine which may extend to twice the amount of
    the cheque, or with both.

NOW, THEREFORE, I hereby call upon you to pay to my client the sum of
Rs. [AMOUNT]/- (Rupees [IN WORDS] only), being the amount of the dishonoured
cheque, together with Rs. [AMOUNT]/- being the cost of this notice, WITHIN
FIFTEEN (15) DAYS of the receipt of this notice.

Please note that if you fail to make the payment within the said period of
fifteen days, my client shall be constrained to initiate criminal proceedings
against you under Section 138 of the Negotiable Instruments Act, 1881 before the
competent court, and shall also file a civil suit for recovery of the said
amount with interest and costs, entirely at your risk as to costs and
consequences.

A copy of this notice is retained in my office for record.

Yours faithfully,


____________________
[ADVOCATE NAME]
Advocate
Enrolment No.: [NUMBER]
[ADDRESS] | [PHONE] | [EMAIL]

Enclosures:
1. Photocopy of Cheque No. [NUMBER] dated [DATE]
2. Photocopy of the Bank Return Memo dated [DATE]
""",
        "keywords": ["cheque bounce", "138", "demand notice", "dishonour", "negotiable instruments", "cheque return", "15 days"],
    },
    {
        "id": "consumer-complaint-doc",
        "title": "Consumer Complaint before the District Commission",
        "category": "consumer",
        "purpose": "The formal complaint that starts a consumer case for a defect or deficiency.",
        "when_to_use": "Within two years of the cause of action, after the legal notice has expired.",
        "checklist": [
            "Invoice, warranty card, and proof of payment",
            "Copies of all complaints made to the company and their replies",
            "A copy of the legal notice and the postal receipt",
            "An affidavit verifying the complaint, and a memo of parties",
        ],
        "stamp": (
            "Court fee is low and is fixed by the value of the claim. File on the e-Daakhil "
            "portal or physically. An advocate is not compulsory - you may appear in person."
        ),
        "body": """BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION,
[DISTRICT], [STATE]

CONSUMER COMPLAINT NO. ________ OF [YEAR]

IN THE MATTER OF:

[YOUR NAME], aged [AGE] years,
son/daughter of [FATHER'S NAME],
residing at [FULL ADDRESS],
Mobile: [PHONE], Email: [EMAIL]                            ... COMPLAINANT

VERSUS

1.  [OPPOSITE PARTY 1 NAME]
    [REGISTERED OFFICE ADDRESS]
    Through its Managing Director / Authorised Signatory     ... OPPOSITE PARTY 1

2.  [OPPOSITE PARTY 2 NAME - e.g. the dealer or the platform]
    [ADDRESS]                                                ... OPPOSITE PARTY 2

COMPLAINT UNDER SECTION 35 OF THE CONSUMER PROTECTION ACT, 2019

MOST RESPECTFULLY SHOWETH:

1.  That the Complainant is a consumer within the meaning of Section 2(7) of the
    Consumer Protection Act, 2019, having purchased [DESCRIBE THE GOODS OR
    SERVICES] from the Opposite Party for a consideration of Rs. [AMOUNT]/- vide
    Invoice No. [NUMBER] dated [DATE]. (Annexure A)

2.  That the said [GOODS/SERVICE] was purchased for the Complainant's personal
    use and not for any commercial purpose.

3.  That [SET OUT THE FACTS IN CHRONOLOGICAL ORDER - what was promised, what was
    delivered, when the problem arose, and what happened after].

4.  That the Complainant approached the Opposite Party on [DATES] through
    [CALLS / EMAILS / THE CUSTOMER CARE PORTAL], vide complaint numbers
    [NUMBERS], but the Opposite Party failed to redress the grievance.
    (Annexure B - copies of correspondence)

5.  That the aforesaid acts of the Opposite Party amount to:
    (a) supply of goods suffering from a "defect" as defined in Section 2(10);
        and/or
    (b) "deficiency" in service as defined in Section 2(11); and/or
    (c) an "unfair trade practice" as defined in Section 2(47) of the Act.

6.  That the Complainant issued a legal notice dated [DATE] calling upon the
    Opposite Party to redress the grievance within [NUMBER] days, which was
    duly served but not complied with. (Annexure C)

7.  That as a result of the Opposite Party's conduct, the Complainant has
    suffered a financial loss of Rs. [AMOUNT]/-, besides considerable mental
    agony, harassment, and loss of time and energy.

8.  JURISDICTION: That the Complainant resides / works for gain at [PLACE],
    which is within the territorial jurisdiction of this Hon'ble Commission
    under Section 34(2)(d) of the Act. The value of the goods/services paid as
    consideration is Rs. [AMOUNT]/-, which is within the pecuniary jurisdiction
    of this Hon'ble Commission.

9.  LIMITATION: That the cause of action arose on [DATE] and continued until
    [DATE]. The present complaint is filed within two years and is therefore
    within limitation under Section 69 of the Act.

PRAYER

It is therefore most respectfully prayed that this Hon'ble Commission may be
pleased to:

    (a) direct the Opposite Party to [REPLACE THE GOODS / REFUND
        Rs. [AMOUNT]/- with interest at [PERCENTAGE]% per annum from [DATE] /
        RECTIFY THE DEFICIENCY];
    (b) direct the Opposite Party to pay Rs. [AMOUNT]/- as compensation for the
        mental agony, harassment and financial loss suffered by the Complainant;
    (c) direct the Opposite Party to pay Rs. [AMOUNT]/- towards the cost of
        this litigation;
    (d) direct the Opposite Party to discontinue the unfair trade practice
        complained of; and
    (e) pass such other order as this Hon'ble Commission deems fit in the facts
        and circumstances of the case.

                                                    COMPLAINANT
Place: [CITY]
Date : [DATE]                                       ____________________
                                                    [NAME]

VERIFICATION
I, [YOUR NAME], the Complainant above named, do hereby verify that the contents
of paragraphs 1 to 9 of the above complaint are true and correct to my knowledge
and belief, and that nothing material has been concealed therefrom.

Verified at [CITY] on this [DAY] day of [MONTH], [YEAR].

                                                    ____________________
                                                    COMPLAINANT

LIST OF ANNEXURES
Annexure A : Invoice dated [DATE]
Annexure B : Correspondence with the Opposite Party
Annexure C : Legal notice dated [DATE] with postal receipt
Annexure D : [ANY OTHER DOCUMENT]
""",
        "keywords": ["consumer complaint", "district commission", "e-daakhil", "deficiency", "defect", "refund", "compensation", "consumer court"],
    },
    {
        "id": "rti-application",
        "title": "RTI Application under the RTI Act, 2005",
        "category": "constitutional",
        "purpose": "Asks a government body for information it holds, with a 30-day statutory deadline.",
        "when_to_use": "Whenever a government office refuses to explain a decision, a delay, or a rejection.",
        "checklist": [
            "The correct public authority and its Public Information Officer",
            "Specific, factual questions - not opinions or 'why' questions",
            "Rs 10 fee by IPO, court fee stamp, DD or online payment (free for BPL applicants)",
            "Your postal address for the reply, and proof of dispatch",
        ],
        "stamp": "Fee of Rs 10 only. No stamp paper. Keep the postal receipt or the online registration number.",
        "body": """APPLICATION UNDER SECTION 6(1) OF THE RIGHT TO INFORMATION ACT, 2005

To,
The Public Information Officer (PIO)
[NAME OF THE DEPARTMENT / OFFICE]
[COMPLETE ADDRESS]

Date: [DATE]

Subject: Request for information under the Right to Information Act, 2005

Sir/Madam,

1.  Name of the applicant        : [YOUR FULL NAME]
2.  Father's / Husband's name    : [NAME]
3.  Full postal address          : [ADDRESS WITH PIN CODE]
4.  Mobile number and email      : [PHONE] | [EMAIL]
5.  Whether Below Poverty Line   : [YES / NO]
                                   (If yes, attach a copy of the BPL card;
                                   no fee is payable.)
6.  Details of fee paid          : Rs. 10/- paid by [INDIAN POSTAL ORDER No.
                                   [NUMBER] dated [DATE] / COURT FEE STAMP /
                                   DEMAND DRAFT No. [NUMBER] / ONLINE PAYMENT
                                   REFERENCE [NUMBER]], in favour of
                                   [ACCOUNTS OFFICER, DEPARTMENT NAME].

INFORMATION SOUGHT

Kindly provide the following information relating to [BRIEFLY DESCRIBE THE
SUBJECT, e.g. Application No. [NUMBER] dated [DATE] submitted by me for
[PURPOSE]]:

1.  Please provide the present status of my application/file bearing No.
    [NUMBER] dated [DATE], along with the date on which it was received in your
    office.

2.  Please provide a certified copy of all file notings, correspondence and
    reports relating to the said application/file.

3.  Please state the name, designation and office address of the officer(s) who
    dealt with the said application, and the period for which the file remained
    pending with each such officer.

4.  Please state the prescribed time limit under the applicable rules or
    citizen's charter for disposal of such an application, and the reasons for
    the delay, if any.

5.  Please provide a copy of the rules, guidelines, circulars or orders under
    which the decision dated [DATE] was taken.

6.  Please state the action taken on the complaint/representation dated [DATE]
    submitted by me, along with a copy of the action-taken report.

MODE OF DELIVERY
Kindly send the information by post to the address given above.
[OR: Kindly permit inspection of the relevant records on a convenient date, and
supply certified copies of the documents I identify during the inspection.]

DECLARATION
I state that I am a citizen of India. I am willing to pay the additional fee
prescribed for the photocopies, if any, on being intimated of the amount.

I request that the information be furnished within thirty days as required by
Section 7(1) of the Right to Information Act, 2005. If any part of this
application is held to be exempt, I request that the reasons and the relevant
provision be stated, and that the remaining information be provided under
Section 10.

If this application does not pertain to your office, kindly transfer it to the
appropriate Public Authority under Section 6(3) within five days and inform me
accordingly.

Yours faithfully,


____________________
[YOUR NAME]
[ADDRESS]

Enclosures: 1. Proof of fee payment
            2. [BPL card copy, if applicable]
""",
        "keywords": ["rti", "right to information", "application", "pio", "government information", "30 days", "section 6"],
    },
    {
        "id": "police-complaint",
        "title": "Written Complaint to the Police / Application for FIR",
        "category": "criminal",
        "purpose": "A written complaint asking the police to register an FIR and investigate.",
        "when_to_use": "Immediately after any cognizable offence - theft, assault, fraud, threat, cheating.",
        "checklist": [
            "Exact date, time and place of the incident",
            "Names and descriptions of the accused, and of any witnesses",
            "A list of the property lost, with values and identification marks",
            "Two copies - one to be returned to you with the receiving stamp",
        ],
        "stamp": "No fee. Insist on a receiving acknowledgement and a free copy of the FIR.",
        "body": """WRITTEN COMPLAINT / APPLICATION FOR REGISTRATION OF FIR

To,
The Station House Officer
[NAME OF POLICE STATION]
[ADDRESS]

Date: [DATE]

Subject: Complaint regarding [BRIEFLY STATE THE OFFENCE, e.g. theft of a
two-wheeler / criminal intimidation / cheating and fraud] - request to register
an FIR and investigate

Respected Sir/Madam,

1.  COMPLAINANT DETAILS
    Name              : [YOUR FULL NAME]
    Father's name     : [NAME]
    Age               : [AGE] years
    Occupation        : [OCCUPATION]
    Residential address: [FULL ADDRESS]
    Mobile / Email    : [PHONE] | [EMAIL]

2.  DATE, TIME AND PLACE OF THE INCIDENT
    Date  : [DATE]
    Time  : approximately [TIME]
    Place : [EXACT PLACE WITH LANDMARK]

3.  DETAILS OF THE ACCUSED (if known)
    Name              : [NAME OR "UNKNOWN"]
    Address           : [ADDRESS]
    Description       : [PHYSICAL DESCRIPTION, VEHICLE NUMBER, PHONE NUMBER OR
                        ANY OTHER IDENTIFYING DETAIL]

4.  FACTS OF THE INCIDENT
    [Describe what happened in simple, factual, chronological sentences. State
    only what you saw, heard or know. For example:

    On [DATE] at about [TIME], I had parked my motorcycle bearing registration
    number [NUMBER] outside [PLACE]. When I returned at about [TIME], the
    motorcycle was missing. I searched the surrounding area and enquired with
    the shopkeepers, but could not trace it. The CCTV camera installed at
    [LOCATION] may have recorded the incident.]

5.  PROPERTY INVOLVED / LOSS SUFFERED
        Item                     Description / Identification    Value (Rs.)
        [ITEM]                   [SERIAL NUMBER, MODEL, COLOUR]  [AMOUNT]
        [ITEM]                   [DESCRIPTION]                   [AMOUNT]
        ----------------------------------------------------------------
        Total loss                                               [AMOUNT]

6.  WITNESSES
    (a) [NAME], [ADDRESS], [PHONE]
    (b) [NAME], [ADDRESS], [PHONE]

7.  EVIDENCE AVAILABLE
    [e.g. CCTV footage at [LOCATION], call recordings, WhatsApp messages,
    photographs, bank statements, medical report. State where the evidence is
    and request that it be secured before it is lost.]

8.  PRAYER
    In view of the above facts, which disclose the commission of a cognizable
    offence, I request you to kindly:
    (a) register a First Information Report and investigate the matter;
    (b) secure and preserve the CCTV footage from [LOCATION] before it is
        overwritten;
    (c) take steps to recover the stolen property / arrest the accused; and
    (d) provide me a free copy of the FIR as required by law.

I state that the facts mentioned above are true and correct to the best of my
knowledge and belief, and that I am prepared to give a further statement and to
depose before the court whenever required.

Yours faithfully,


____________________
[YOUR NAME]
[PHONE]

Enclosures:
1. Copy of [RC / invoice / medical report / screenshots], as applicable
2. Identity proof

--------------------------------------------------------------------------
(FOR OFFICE USE) Received on ______________ at __________ hours.
FIR No. ____________ dated ____________  u/s ____________
Signature and seal of the receiving officer: ____________________
--------------------------------------------------------------------------

NOTE: If the police station refuses to register the FIR, send this same
complaint by registered post to the Superintendent of Police. If it is still not
registered, a complaint may be filed before the jurisdictional Judicial
Magistrate, who can direct the police to register and investigate.
""",
        "keywords": ["police complaint", "fir", "criminal complaint", "theft", "shso", "zero fir", "register fir", "cognizable"],
    },

    # ------------------------------------------------------------------
    # PERSONAL / FAMILY
    # ------------------------------------------------------------------
    {
        "id": "will-testament",
        "title": "Last Will and Testament",
        "category": "family",
        "purpose": "Decides who receives your property after your death, and appoints an executor.",
        "when_to_use": "Any adult of sound mind who owns anything should have one; update it after major life events.",
        "checklist": [
            "A complete list of assets and liabilities with account and property numbers",
            "Names, ages and addresses of every beneficiary",
            "An executor who is willing to act, and preferably an alternate",
            "Two witnesses who are NOT beneficiaries, and a doctor's fitness certificate",
        ],
        "stamp": (
            "A Will needs NO stamp duty and can be written on plain paper. Registration is "
            "optional but makes proof far easier. Two attesting witnesses are mandatory."
        ),
        "body": """LAST WILL AND TESTAMENT

I, [YOUR FULL NAME], son/daughter/wife of [FATHER'S/HUSBAND'S NAME], aged
[AGE] years, resident of [FULL ADDRESS], holding PAN [PAN] and Aadhaar ending
[LAST FOUR DIGITS], do hereby make, publish and declare this to be my LAST WILL
AND TESTAMENT, executed at [CITY] on this [DAY] day of [MONTH], [YEAR].

1.  DECLARATION
    I declare that I am of sound mind, memory and understanding, that I am
    making this Will voluntarily and without any coercion, undue influence or
    persuasion from any person, and that I fully understand the contents and
    effect of this Will.

2.  REVOCATION
    I hereby revoke all Wills, codicils and testamentary dispositions made by me
    at any time heretofore. This is my last and only Will.

3.  APPOINTMENT OF EXECUTOR
    I appoint [EXECUTOR NAME], son/daughter of [FATHER'S NAME], residing at
    [ADDRESS], as the Executor of this Will. If he/she is unable or unwilling to
    act, I appoint [ALTERNATE EXECUTOR NAME], residing at [ADDRESS], as the
    alternate Executor. The Executor shall not be required to furnish any
    security.

4.  MY FAMILY
    At the date of this Will my family consists of:
        (a) [NAME], my [RELATIONSHIP], aged [AGE], residing at [ADDRESS]
        (b) [NAME], my [RELATIONSHIP], aged [AGE], residing at [ADDRESS]
        (c) [NAME], my [RELATIONSHIP], aged [AGE], residing at [ADDRESS]

5.  MY ASSETS
    A. IMMOVABLE PROPERTY
       (i)  [DESCRIPTION, ADDRESS, SURVEY/FLAT NUMBER, AREA, AND THE DOCUMENT
            BY WHICH I ACQUIRED IT]
       (ii) [DESCRIPTION]

    B. BANK ACCOUNTS AND DEPOSITS
       (i)  Savings Account No. [NUMBER], [BANK], [BRANCH]
       (ii) Fixed Deposit No. [NUMBER], [BANK]

    C. INVESTMENTS
       (i)  Demat Account No. [NUMBER] with [DEPOSITORY PARTICIPANT]
       (ii) Mutual fund folios: [FOLIO NUMBERS]
       (iii) PPF / EPF / NPS Account No. [NUMBER]

    D. INSURANCE
       (i)  Policy No. [NUMBER] with [INSURER], nominee [NAME]

    E. MOVABLE PROPERTY
       (i)  Gold and silver ornaments as listed in the Annexure
       (ii) Vehicle bearing registration number [NUMBER]

6.  BEQUESTS
    I give, devise and bequeath my property as follows:

    (a) My immovable property described in Clause 5.A(i) shall go absolutely to
        [NAME], my [RELATIONSHIP].
    (b) My bank accounts and fixed deposits described in Clause 5.B shall be
        divided equally between [NAME] and [NAME].
    (c) My investments described in Clause 5.C shall go absolutely to [NAME].
    (d) My gold ornaments listed in the Annexure shall go to [NAME].
    (e) The residue of my estate, whatsoever and wheresoever, not specifically
        disposed of above, shall go to [NAME].

7.  MINOR BENEFICIARIES
    If any beneficiary is a minor at the time of my death, his/her share shall
    be held by [GUARDIAN NAME] as guardian, to be applied for the minor's
    maintenance, education and benefit, and handed over on the minor attaining
    the age of eighteen years.

8.  LIABILITIES
    My Executor shall first discharge all my just debts, funeral expenses and
    testamentary expenses out of my estate before distributing the bequests.

9.  DECLARATION AS TO NOMINATIONS
    I clarify that any nomination made by me in respect of any bank account,
    insurance policy or investment is only for the purpose of receiving the
    proceeds, and the nominee shall hold them for the benefit of the
    beneficiaries named in this Will.

IN WITNESS WHEREOF I have signed this Will consisting of [NUMBER] pages, in the
presence of the two witnesses named below, who have signed in my presence and in
the presence of each other, on the day, month and year first above written.


                                              ____________________
                                              [YOUR NAME]
                                              TESTATOR

ATTESTATION BY WITNESSES
We, the undersigned, state that the Testator signed this Will in our presence,
that the Testator appeared to be of sound mind and understanding, and that we
have signed as attesting witnesses in the presence of the Testator and of each
other. Neither of us is a beneficiary under this Will.

WITNESS 1                                     WITNESS 2
Name    : [NAME]                              Name    : [NAME]
Address : [ADDRESS]                           Address : [ADDRESS]
Signature: ____________________               Signature: ____________________

(RECOMMENDED) Certificate of a registered medical practitioner certifying that
the Testator was of sound mind and disposing capacity on the date of execution
is annexed.
""",
        "keywords": ["will", "testament", "executor", "bequest", "inheritance", "succession", "testator", "attesting witness"],
    },
    {
        "id": "power-of-attorney",
        "title": "Power of Attorney (General / Special)",
        "category": "civil",
        "purpose": "Authorises another person to act on your behalf in specified matters.",
        "when_to_use": "When you cannot be physically present - living abroad, illness, or a specific transaction.",
        "checklist": [
            "Whether you need a General PoA (broad) or a Special PoA (one specific task) - prefer Special",
            "Exact powers to be granted, written narrowly",
            "Validity period and how it can be revoked",
            "Identity proof and photographs of both the principal and the attorney",
        ],
        "stamp": (
            "Stamp duty varies by state and by whether the PoA is for consideration. A PoA "
            "authorising the sale of immovable property should be registered. If executed abroad, "
            "it must be notarised/apostilled and stamped in India within three months."
        ),
        "body": """SPECIAL POWER OF ATTORNEY

KNOW ALL MEN BY THESE PRESENTS that I, [PRINCIPAL NAME], son/daughter of
[FATHER'S NAME], aged [AGE] years, residing at [FULL ADDRESS], holding
PAN [PAN] (hereinafter called the "PRINCIPAL"),

do hereby nominate, constitute and appoint

[ATTORNEY NAME], son/daughter of [FATHER'S NAME], aged [AGE] years, residing at
[FULL ADDRESS], holding PAN [PAN], who is my [RELATIONSHIP] (hereinafter called
the "ATTORNEY"),

as my true and lawful Attorney, to do and execute the following acts, deeds and
things for me, in my name and on my behalf:

1.  To [STATE THE SPECIFIC PURPOSE PRECISELY, e.g. represent me before the
    Sub-Registrar, [PLACE], and to present for registration and admit execution
    of the Sale Deed dated [DATE] in respect of the property described in the
    Schedule below].

2.  To appear before, and to sign, submit and receive documents from, the
    following authorities in connection with the above purpose:
    [LIST THE AUTHORITIES - e.g. the Sub-Registrar, the municipal corporation,
    the electricity board, the housing society, the bank].

3.  To sign, execute, verify and submit all applications, forms, affidavits,
    declarations, indemnities, undertakings and receipts required for the above
    purpose.

4.  To receive and give valid receipt and discharge for any sum of money payable
    to me in connection with the above purpose, and to deposit the same into my
    bank account bearing No. [ACCOUNT NUMBER] with [BANK NAME].

5.  To engage an advocate or authorised agent and to pay their fees, and to
    appear before any court or tribunal in connection with the above purpose,
    to the extent permitted by law.

6.  Generally, to do all such lawful acts as may be necessary and incidental to
    the above purposes as fully and effectively as I could do personally.

CONDITIONS AND LIMITATIONS

(a) The powers granted are strictly limited to the purposes stated above and
    shall not be construed to authorise any other act.
(b) The Attorney shall NOT be entitled to sell, mortgage, gift or otherwise
    alienate any property of the Principal, except as expressly stated above.
(c) The Attorney shall NOT be entitled to sub-delegate any of these powers.
(d) This Power of Attorney shall remain in force from [START DATE] until
    [END DATE], or until revoked by me in writing, whichever is earlier.
(e) This Power of Attorney shall stand automatically revoked upon my death or on
    my becoming of unsound mind.
(f) The Attorney is acting gratuitously and is not entitled to any remuneration.

RATIFICATION
I hereby agree to ratify and confirm all lawful acts done by my said Attorney in
exercise of the powers hereby conferred.

SCHEDULE OF PROPERTY (if applicable)
[FULL DESCRIPTION OF THE PROPERTY WITH BOUNDARIES]

IN WITNESS WHEREOF I have executed this Power of Attorney at [CITY] on this
[DAY] day of [MONTH], [YEAR].


____________________
[PRINCIPAL NAME]
PRINCIPAL

I, [ATTORNEY NAME], accept the appointment and undertake to act faithfully
within the powers conferred.

____________________
[ATTORNEY NAME]
ATTORNEY
(Specimen signature of the Attorney attested above)

WITNESSES:
1. Name: [NAME], Address: [ADDRESS]           Signature: ____________
2. Name: [NAME], Address: [ADDRESS]           Signature: ____________

(To be notarised and, where required by law, registered before the
Sub-Registrar.)
""",
        "keywords": ["power of attorney", "poa", "special power of attorney", "gpa", "authorisation", "attorney", "principal"],
    },
    {
        "id": "general-affidavit",
        "title": "General Affidavit",
        "category": "civil",
        "purpose": "A written statement sworn on oath, used as proof of a fact before an authority.",
        "when_to_use": "For income proof, address proof, gap year, lost documents, or any declaration required by an office.",
        "checklist": [
            "The exact fact you need to declare, in short numbered sentences",
            "Supporting documents to attach, if any",
            "Non-judicial stamp paper of the value your state prescribes",
            "Attestation before a Notary Public or Oath Commissioner",
        ],
        "stamp": (
            "Executed on non-judicial stamp paper (commonly Rs 10 to Rs 100 depending on the "
            "state) and attested by a Notary Public with the notarial stamp and register entry."
        ),
        "body": """AFFIDAVIT

(On non-judicial stamp paper of Rs. [VALUE]/-)

BEFORE THE NOTARY PUBLIC / OATH COMMISSIONER AT [CITY]

I, [YOUR FULL NAME], son/daughter/wife of [FATHER'S/HUSBAND'S NAME], aged
[AGE] years, by occupation [OCCUPATION], permanently residing at
[PERMANENT ADDRESS] and presently residing at [PRESENT ADDRESS], holding
Aadhaar No. ending [LAST FOUR DIGITS] and PAN [PAN],

do hereby solemnly affirm and sincerely state on oath as under:

1.  That I am the deponent above named and am fully competent to swear this
    affidavit, and the facts stated herein are within my personal knowledge.

2.  That [STATE THE FIRST FACT CLEARLY. Examples:
      - my date of birth is [DATE] as recorded in my [DOCUMENT];
      - my name has been recorded differently in different documents, namely as
        [NAME 1] in [DOCUMENT] and as [NAME 2] in [DOCUMENT], and both refer to
        one and the same person, that is myself;
      - my total annual family income from all sources is Rs. [AMOUNT];
      - I have been residing at the above address since [DATE];
      - my original [DOCUMENT] bearing No. [NUMBER] has been lost and despite a
        diligent search it could not be traced.]

3.  That [STATE THE SECOND FACT, IF ANY].

4.  That [STATE THE THIRD FACT, IF ANY].

5.  That this affidavit is being sworn for the purpose of submission to
    [NAME OF THE AUTHORITY / PURPOSE] and for no other purpose.

6.  That I undertake to indemnify [THE AUTHORITY] against any loss or claim
    arising from any statement in this affidavit being found to be false.

7.  That the contents of this affidavit are true and correct to the best of my
    knowledge and belief, no part of it is false, and nothing material has been
    concealed therefrom.

                                              ____________________
Place: [CITY]                                 DEPONENT
Date : [DATE]                                 [NAME]

VERIFICATION

I, the deponent above named, do hereby verify that the contents of paragraphs 1
to 7 of this affidavit are true and correct to my knowledge, that no part of it
is false and that nothing material has been concealed therefrom.

Verified at [CITY] on this [DAY] day of [MONTH], [YEAR].

                                              ____________________
                                              DEPONENT

Solemnly affirmed before me by the deponent, who is identified by
[IDENTIFICATION DOCUMENT], on this [DAY] day of [MONTH], [YEAR].


                                              ____________________
                                              NOTARY PUBLIC
                                              [SEAL AND REGISTER NUMBER]
""",
        "keywords": ["affidavit", "sworn statement", "notary", "declaration", "deponent", "income affidavit", "address proof", "name change"],
    },
    {
        "id": "mutual-divorce-petition",
        "title": "Petition for Divorce by Mutual Consent",
        "category": "family",
        "purpose": "A joint petition by both spouses to dissolve a marriage without a contested trial.",
        "when_to_use": "After at least one year of living separately and once all terms are settled.",
        "checklist": [
            "Marriage certificate and wedding photographs",
            "Proof of separate residence for one year or more",
            "A complete written settlement of alimony, custody, and division of assets",
            "Address proof and identity proof of both parties",
        ],
        "stamp": (
            "Court fee as prescribed by the state. Both parties must appear in person for the "
            "first and second motions. The six-month gap can be waived by the court in a proper "
            "case."
        ),
        "body": """IN THE FAMILY COURT AT [CITY]

H.M.O.P. / PETITION NO. ________ OF [YEAR]

IN THE MATTER OF:

1.  [HUSBAND'S NAME], aged [AGE] years,
    son of [FATHER'S NAME],
    residing at [ADDRESS]                                  ... PETITIONER NO. 1

2.  [WIFE'S NAME], aged [AGE] years,
    daughter of [FATHER'S NAME],
    residing at [ADDRESS]                                  ... PETITIONER NO. 2

JOINT PETITION UNDER SECTION 13B OF THE HINDU MARRIAGE ACT, 1955
FOR DISSOLUTION OF MARRIAGE BY MUTUAL CONSENT

[Use Section 28 of the Special Marriage Act, 1954 where the marriage was
solemnised under that Act.]

MOST RESPECTFULLY SHOWETH:

1.  That the Petitioners were lawfully married to each other on [DATE] at
    [PLACE OF MARRIAGE] according to [HINDU / SPECIAL MARRIAGE ACT] rites and
    ceremonies. The marriage was registered on [DATE] vide Registration No.
    [NUMBER]. A copy of the marriage certificate is annexed as Annexure A.

2.  That after the marriage the Petitioners last resided together as husband and
    wife at [ADDRESS].

3.  That out of the said wedlock [NUMBER] child/children was/were born, namely
    [NAME], aged [AGE] years. [OR: That no child was born out of the said
    wedlock.]

4.  That on account of temperamental differences and incompatibility of
    thoughts, the Petitioners have not been able to live together as husband and
    wife. Serious differences arose between them, and despite the best efforts
    of both the Petitioners and their family members, and mediation attempted on
    [DATE], reconciliation has not been possible.

5.  That the Petitioners have been living separately since [DATE], that is for a
    period of more than one year immediately preceding the presentation of this
    petition, and have not been able to live together.

6.  That the marriage between the Petitioners has irretrievably broken down and
    there is no possibility of reconciliation. The Petitioners have therefore
    mutually and voluntarily agreed to dissolve the marriage.

7.  That the Petitioners have arrived at a full and final settlement of all
    their claims against each other, the terms of which are as follows:

    (a) PERMANENT ALIMONY: Petitioner No. 1 shall pay Petitioner No. 2 a total
        sum of Rs. [AMOUNT]/- as permanent alimony in full and final settlement
        of all past, present and future claims for maintenance, payable as
        [DESCRIBE THE SCHEDULE].
    (b) STRIDHAN AND ARTICLES: All stridhan, jewellery and personal articles of
        Petitioner No. 2 have been returned to and received by her, and she has
        no further claim in that regard.
    (c) CUSTODY: The custody of the minor child [NAME] shall remain with
        [PETITIONER], and the other parent shall have visitation rights as
        follows: [SET OUT THE VISITATION SCHEDULE].
    (d) EDUCATION AND MAINTENANCE OF THE CHILD: [SET OUT THE ARRANGEMENT].
    (e) PROPERTY: [SET OUT THE AGREED DIVISION OF ANY JOINTLY HELD PROPERTY,
        BANK ACCOUNTS AND LOANS.]
    (f) WITHDRAWAL OF CASES: The Petitioners shall withdraw all civil and
        criminal proceedings filed against each other, namely [LIST THE CASES],
        and shall not initiate any fresh proceedings on the same cause.

8.  That this petition is not being presented in collusion with each other for
    any collateral purpose, and there is no coercion, fraud or undue influence
    on either Petitioner.

9.  That this Hon'ble Court has jurisdiction to entertain this petition as the
    Petitioners last resided together within its territorial jurisdiction /
    Petitioner No. 2 resides within its jurisdiction.

10. That the Petitioners have not filed any other petition for divorce in
    respect of the said marriage before any other court.

PRAYER

It is therefore most respectfully prayed that this Hon'ble Court may be pleased
to:

    (a) dissolve the marriage between the Petitioners solemnised on [DATE] by a
        decree of divorce by mutual consent under Section 13B of the Hindu
        Marriage Act, 1955;
    (b) record and give effect to the terms of settlement set out in paragraph 7
        above;
    (c) [where applicable] waive the statutory waiting period of six months
        under Section 13B(2) in the interest of justice, as the marriage has
        irretrievably broken down and the settlement is complete; and
    (d) pass such other orders as this Hon'ble Court deems fit.

Place: [CITY]
Date : [DATE]

____________________                          ____________________
PETITIONER NO. 1                              PETITIONER NO. 2

VERIFICATION
We, the Petitioners above named, do hereby verify that the contents of
paragraphs 1 to 10 of this petition are true and correct to our knowledge, and
that nothing material has been concealed therefrom.

Verified at [CITY] on this [DAY] day of [MONTH], [YEAR].

____________________                          ____________________
PETITIONER NO. 1                              PETITIONER NO. 2
""",
        "keywords": ["divorce", "mutual consent", "13b", "family court", "alimony", "settlement", "separation", "custody"],
    },

    # ------------------------------------------------------------------
    # DIGITAL / MISC
    # ------------------------------------------------------------------
    {
        "id": "privacy-policy",
        "title": "Website / App Privacy Policy",
        "category": "cyber",
        "purpose": "Tells users what personal data you collect, why, and what rights they have.",
        "when_to_use": "On every website or app that collects even an email address.",
        "checklist": [
            "A complete list of the data you actually collect - do not copy someone else's list",
            "The purpose and lawful basis for each category of data",
            "Names of third parties and processors with whom data is shared",
            "Retention period, security measures, and the Grievance Officer's contact",
        ],
        "stamp": "No stamp duty. Publish it on the site with a version date and get affirmative consent.",
        "body": """PRIVACY POLICY

Last updated: [DATE]
Version: [VERSION]

[COMPANY / WEBSITE NAME] ("we", "us", "our") operates [WEBSITE / APP NAME] (the
"Platform"). This Privacy Policy explains what personal data we collect, why we
collect it, how we use it, and the rights available to you under the Digital
Personal Data Protection Act, 2023 and the Information Technology Act, 2000.

By using the Platform you confirm that you have read this Policy.

1.  WHO WE ARE (DATA FIDUCIARY)
    Name             : [LEGAL NAME OF THE ENTITY]
    Registered office: [ADDRESS]
    Email            : [EMAIL]

2.  DATA WE COLLECT
    (a) Information you give us:
        - Name, email address, mobile number
        - [Account credentials, profile photograph]
        - [Billing address and payment reference - we do NOT store full card
          details]
        - Content you submit, such as [queries, uploads, feedback]
    (b) Information collected automatically:
        - IP address, browser type, device identifier, operating system
        - Pages visited, time spent, and referring URL
        - Cookies and similar technologies as described in Clause 7
    (c) Information from third parties:
        - [e.g. authentication data from a social login provider]

3.  WHY WE COLLECT IT (PURPOSE AND LAWFUL BASIS)
        Purpose                              Lawful basis
        Creating and managing your account   Consent / performance of service
        Providing the requested service      Consent
        Responding to your queries           Consent
        Processing payments                  Contractual necessity
        Security, fraud prevention, logs     Legitimate use
        Complying with legal obligations     Legal obligation
        Marketing communications             Separate, withdrawable consent

    We do not use your data for any purpose beyond those stated above without
    obtaining fresh consent.

4.  SHARING OF DATA
    We share personal data only with:
    (a) service providers who process data on our behalf under a written
        agreement - [hosting provider], [payment gateway], [analytics provider];
    (b) authorities, where disclosure is required by law or a valid court or
        government order; and
    (c) a successor entity in the event of a merger or acquisition, subject to
        this Policy.
    We do NOT sell your personal data.

5.  RETENTION
    We retain personal data only as long as necessary for the purpose for which
    it was collected, or as required by law. Account data is deleted within
    [NUMBER] days of account closure, except where retention is legally
    required. Server logs are retained for [NUMBER] days.

6.  YOUR RIGHTS
    You have the right to:
    (a) access a summary of the personal data we process about you;
    (b) request correction, completion or updating of inaccurate data;
    (c) request erasure of your data where it is no longer needed;
    (d) withdraw your consent at any time, as easily as it was given;
    (e) nominate another person to exercise these rights in the event of your
        death or incapacity; and
    (f) file a grievance with us and, if unsatisfied, with the Data Protection
        Board of India.
    To exercise any right, write to the Grievance Officer named in Clause 10.

7.  COOKIES
    We use cookies that are strictly necessary for the Platform to work, and
    [analytics / preference] cookies which you may decline. You can also control
    cookies through your browser settings, though some features may then not
    work.

8.  SECURITY
    We use reasonable security safeguards including [encryption in transit,
    access controls, hashed passwords, regular backups]. No system is completely
    secure, but in the event of a personal data breach we will notify the Data
    Protection Board and affected users as required by law.

9.  CHILDREN
    The Platform is not intended for children below 18 years. We do not
    knowingly process a child's personal data without verifiable parental
    consent, and we do not undertake tracking or targeted advertising directed
    at children.

10. GRIEVANCE OFFICER
    Name    : [NAME]
    Address : [ADDRESS]
    Email   : [EMAIL]
    We acknowledge every grievance within [NUMBER] hours and resolve it within
    [NUMBER] days.

11. CHANGES TO THIS POLICY
    We may update this Policy. The updated version will be posted here with a
    revised "Last updated" date, and material changes will be notified to you.
""",
        "keywords": ["privacy policy", "data protection", "dpdp", "cookies", "personal data", "grievance officer", "website policy", "consent"],
    },
    {
        "id": "terms-of-service",
        "title": "Website / App Terms of Service",
        "category": "cyber",
        "purpose": "The contract between the platform and its users.",
        "when_to_use": "On every website or app before users can register or transact.",
        "checklist": [
            "Eligibility, account rules and prohibited conduct",
            "Payment, refund and cancellation terms, if you charge money",
            "Ownership of your content and of user-generated content",
            "Limitation of liability, termination and governing law",
        ],
        "stamp": "No stamp duty. Use a click-wrap acceptance (an unticked checkbox), not a footer link alone.",
        "body": """TERMS OF SERVICE

Last updated: [DATE]

These Terms of Service ("Terms") govern your use of [WEBSITE / APP NAME] (the
"Platform") operated by [COMPANY NAME] ("we", "us"). By creating an account or
using the Platform, you agree to these Terms. If you do not agree, do not use
the Platform.

1.  ELIGIBILITY
    You must be at least 18 years of age and competent to contract under the
    Indian Contract Act, 1872. If you use the Platform on behalf of an
    organisation, you confirm you are authorised to bind it.

2.  ACCOUNT
    2.1 You must provide accurate information and keep it updated.
    2.2 You are responsible for keeping your credentials confidential and for
        all activity under your account.
    2.3 Notify us immediately at [EMAIL] of any unauthorised use.

3.  SERVICES
    We provide [DESCRIBE THE SERVICE CLEARLY]. We may modify, suspend or
    discontinue any feature with reasonable notice.

4.  FEES, PAYMENT AND REFUNDS
    4.1 Charges are as displayed on the Platform at the time of purchase, and
        are inclusive/exclusive of applicable taxes as indicated.
    4.2 Payments are processed by [PAYMENT GATEWAY]. We do not store full card
        details.
    4.3 Refund and cancellation policy: [SET OUT CLEARLY - within how many days,
        in what circumstances, and how long the refund takes].
    4.4 Subscriptions renew [AUTOMATICALLY / MANUALLY]. You may cancel at any
        time from your account settings, and cancellation takes effect at the
        end of the current billing period.

5.  ACCEPTABLE USE
    You shall not:
    (a) violate any law, or infringe anyone's intellectual property or privacy;
    (b) upload unlawful, obscene, defamatory, misleading or harmful content;
    (c) attempt to gain unauthorised access, probe or disrupt the Platform;
    (d) scrape, reverse engineer, or use automated means without our written
        consent;
    (e) impersonate any person or misrepresent your affiliation; or
    (f) use the Platform to transmit malware or spam.

6.  YOUR CONTENT
    6.1 You retain ownership of the content you submit.
    6.2 You grant us a non-exclusive, worldwide, royalty-free licence to host,
        store, reproduce and display that content solely to operate and improve
        the Platform.
    6.3 You are responsible for your content and confirm you have the rights to
        submit it.

7.  OUR INTELLECTUAL PROPERTY
    The Platform, its software, design, text, graphics and trade marks are owned
    by us or our licensors. You receive only a limited, revocable,
    non-transferable licence to use the Platform for its intended purpose.

8.  THIRD-PARTY LINKS AND SERVICES
    The Platform may link to third-party sites or use third-party services. We
    are not responsible for their content, policies or practices.

9.  DISCLAIMER
    The Platform is provided on an "as is" and "as available" basis. To the
    maximum extent permitted by law, we disclaim all warranties, express or
    implied, including merchantability and fitness for a particular purpose. We
    do not warrant that the Platform will be uninterrupted or error free.

10. LIMITATION OF LIABILITY
    To the maximum extent permitted by law, our aggregate liability arising out
    of or relating to the Platform shall not exceed the amount paid by you to us
    in the [NUMBER] months preceding the claim. We shall not be liable for
    indirect, incidental, special or consequential loss, or loss of profit or
    data. Nothing in these Terms limits liability that cannot be limited by law.

11. INDEMNITY
    You agree to indemnify us against any claim, loss or expense arising from
    your breach of these Terms or your misuse of the Platform.

12. TERMINATION
    We may suspend or terminate your account for breach of these Terms, with
    notice where practicable. You may close your account at any time. Clauses 6,
    7, 9, 10, 11 and 14 survive termination.

13. GRIEVANCE REDRESSAL
    Grievance Officer : [NAME]
    Email             : [EMAIL]
    Address           : [ADDRESS]
    We acknowledge complaints within [NUMBER] hours and resolve them within
    [NUMBER] days, as required by the applicable IT Rules.

14. GOVERNING LAW AND DISPUTES
    These Terms are governed by the laws of India. Subject to any statutory
    right you may have as a consumer to approach a forum where you reside, the
    courts at [CITY] shall have exclusive jurisdiction.

15. CHANGES
    We may update these Terms. Continued use after the updated Terms take effect
    constitutes acceptance. Material changes will be notified to you in advance.
""",
        "keywords": ["terms of service", "terms and conditions", "tos", "user agreement", "click wrap", "refund policy", "liability"],
    },
    {
        "id": "loan-agreement",
        "title": "Personal Loan Agreement",
        "category": "banking",
        "purpose": "Records the terms of money lent between individuals or to a business.",
        "when_to_use": "Whenever money is lent, even to a friend or relative - an oral loan is very hard to prove.",
        "checklist": [
            "Principal amount, interest rate and the exact repayment schedule",
            "Mode of disbursement - always by bank transfer, never cash",
            "Security or guarantee, if any",
            "What counts as default and what happens then",
        ],
        "stamp": (
            "Stamp duty as per the state Stamp Act on loan agreements. Disburse only by bank "
            "transfer - Section 269SS of the Income-tax Act penalises cash loans above the "
            "prescribed limit."
        ),
        "body": """LOAN AGREEMENT

This Loan Agreement is made at [CITY] on this [DAY] day of [MONTH], [YEAR]

BETWEEN

[LENDER NAME], son/daughter of [FATHER'S NAME], residing at [ADDRESS],
PAN [PAN] (the "Lender")

AND

[BORROWER NAME], son/daughter of [FATHER'S NAME], residing at [ADDRESS],
PAN [PAN] (the "Borrower")

1.  LOAN AMOUNT
    The Lender agrees to lend and the Borrower agrees to borrow a sum of
    Rs. [AMOUNT]/- (Rupees [IN WORDS] only) (the "Principal").

2.  DISBURSEMENT
    The Principal shall be disbursed by bank transfer to the Borrower's account
    No. [ACCOUNT NUMBER] with [BANK NAME], IFSC [IFSC], on or before [DATE]. The
    Borrower shall acknowledge receipt in writing.

3.  PURPOSE
    The loan shall be used solely for [STATE THE PURPOSE] and for no other
    purpose.

4.  INTEREST
    The Principal shall carry simple interest at the rate of [PERCENTAGE]% per
    annum, calculated from the date of disbursement until repayment in full.

5.  REPAYMENT
    5.1 The Borrower shall repay the Principal together with interest in
        [NUMBER] equal monthly instalments of Rs. [AMOUNT]/- each, payable on or
        before the [DAY] of each month, commencing from [DATE] and ending on
        [DATE].
    5.2 All payments shall be made by bank transfer to the Lender's account
        No. [ACCOUNT NUMBER] with [BANK NAME], IFSC [IFSC].
    5.3 The Borrower may prepay the whole or part of the loan at any time
        without any prepayment charge, and interest shall then be recomputed up
        to the date of prepayment.

6.  SECURITY
    [CHOOSE ONE]
    (a) The loan is unsecured; OR
    (b) The Borrower has deposited [DESCRIBE THE SECURITY] as security, which
        shall be returned on full repayment; OR
    (c) [GUARANTOR NAME], residing at [ADDRESS], has signed this Agreement as
        Guarantor and undertakes to repay the outstanding amount on the
        Borrower's default.

7.  DEFAULT
    Each of the following is an Event of Default:
    (a) failure to pay any instalment within [NUMBER] days of its due date;
    (b) any statement made by the Borrower being found to be false;
    (c) the Borrower becoming insolvent or having a decree passed against
        her/him; or
    (d) breach of any term of this Agreement.

8.  CONSEQUENCES OF DEFAULT
    On an Event of Default, the Lender may, by written notice, declare the
    entire outstanding Principal and accrued interest immediately due and
    payable, and the outstanding amount shall thereafter carry additional
    interest at [PERCENTAGE]% per annum until realisation.

9.  POST-DATED CHEQUES
    The Borrower has handed over [NUMBER] post-dated cheques bearing numbers
    [NUMBERS] drawn on [BANK], as security for the repayment. The Borrower
    acknowledges that dishonour of any such cheque may attract liability under
    Section 138 of the Negotiable Instruments Act, 1881.

10. ACKNOWLEDGEMENT AND LIMITATION
    The Borrower shall, if requested, sign an acknowledgement of the debt each
    year, and acknowledges that such acknowledgement extends the period of
    limitation under Section 18 of the Limitation Act, 1963.

11. NOTICES
    All notices shall be in writing and sent to the addresses stated above by
    registered post and email.

12. GOVERNING LAW AND DISPUTES
    This Agreement is governed by Indian law. Disputes shall be referred to a
    sole arbitrator under the Arbitration and Conciliation Act, 1996, seated at
    [CITY], and the courts at [CITY] shall have exclusive jurisdiction.

IN WITNESS WHEREOF the parties have signed this Agreement on the day, month and
year first above written.


____________________                          ____________________
LENDER                                        BORROWER
[NAME]                                        [NAME]

____________________
GUARANTOR (if any)
[NAME]

WITNESSES:
1. ____________________                       2. ____________________
""",
        "keywords": ["loan agreement", "lend money", "borrower", "lender", "interest", "repayment", "emi", "guarantor", "promissory"],
    },
    {
        "id": "noc",
        "title": "No Objection Certificate (NOC)",
        "category": "civil",
        "purpose": "A written statement that the issuer has no objection to a specified act.",
        "when_to_use": "For vehicle transfer, employment, tenancy, construction, society permission or travel.",
        "checklist": [
            "Exactly what is being permitted, described narrowly",
            "The name of the person and the authority it is addressed to",
            "Validity period, if any",
            "Signature of a person actually authorised to issue it",
        ],
        "stamp": "Usually plain paper on letterhead; some authorities insist on notarisation or stamp paper.",
        "body": """NO OBJECTION CERTIFICATE

[LETTERHEAD OF THE ISSUER, IF ANY]

Ref: [REFERENCE NUMBER]
Date: [DATE]

To,
[NAME OF THE AUTHORITY / PERSON TO WHOM ADDRESSED]
[ADDRESS]

Subject: No Objection Certificate in favour of [NAME] for [PURPOSE]

TO WHOMSOEVER IT MAY CONCERN

1.  I / We, [ISSUER NAME], son/daughter of [FATHER'S NAME], residing at
    [ADDRESS] / [COMPANY NAME], having its office at [ADDRESS], through its
    authorised signatory, do hereby state as follows:

2.  That [NAME OF THE BENEFICIARY], son/daughter of [FATHER'S NAME], residing at
    [ADDRESS], is [STATE THE RELATIONSHIP - e.g. the registered owner of the
    premises / an employee of our organisation since [DATE] / the tenant of the
    premises described below].

3.  That the said [NAME] has approached me/us seeking a No Objection Certificate
    for the purpose of [STATE THE PURPOSE PRECISELY, e.g.:
      - transfer of the registration of vehicle bearing No. [NUMBER] to another
        State;
      - obtaining an electricity connection at the premises described below;
      - carrying out interior renovation work at Flat No. [NUMBER];
      - taking up higher studies / part-time employment;
      - applying for a passport / visa].

4.  That I/We have examined the request and hereby state that I/We have
    NO OBJECTION to the said [NAME] [STATE THE PERMITTED ACT] subject to the
    following conditions:
    (a) [CONDITION, e.g. all dues to me/us are cleared as on date];
    (b) [CONDITION, e.g. no structural change shall be made to the premises];
    (c) [CONDITION, e.g. all statutory approvals shall be obtained
        independently by the applicant].

5.  That this No Objection Certificate is issued at the request of the said
    [NAME] for the specific purpose stated in paragraph 3 above, and shall not
    be used for any other purpose.

6.  That this certificate is valid up to [DATE].

7.  That the issuance of this certificate does not create any liability on
    me/us, and does not amount to a waiver of any of my/our rights.

DESCRIPTION OF PROPERTY / SUBJECT MATTER (if applicable)
[DESCRIBE THE PROPERTY, VEHICLE OR OTHER SUBJECT MATTER]

Yours faithfully,


____________________
[ISSUER NAME]
[DESIGNATION, IF ANY]
[ADDRESS] | [PHONE]
(Seal, if applicable)

WITNESSES (if required):
1. ____________________                       2. ____________________
""",
        "keywords": ["noc", "no objection certificate", "permission", "consent letter", "vehicle noc", "landlord noc", "employer noc"],
    },
    {
        "id": "work-order",
        "title": "Construction Work Order / Contract",
        "category": "infrastructure",
        "purpose": "Engages a contractor to execute construction or interior work at an agreed price.",
        "when_to_use": "Before any civil, interior or renovation work begins on site.",
        "checklist": [
            "Detailed scope, drawings, specifications and bill of quantities",
            "Rate basis - lump sum or item rate - and the price escalation position",
            "Timeline with milestones and liquidated damages for delay",
            "Retention percentage, defect liability period, and safety and insurance obligations",
        ],
        "stamp": "Stamp duty on works contracts as per the state Stamp Act; annex the BOQ and drawings.",
        "body": """WORK ORDER / CONSTRUCTION CONTRACT

Work Order No. : [NUMBER]
Date           : [DATE]

BETWEEN

[EMPLOYER / OWNER NAME], residing/having its office at [ADDRESS]
(the "Employer")

AND

[CONTRACTOR NAME], having its office at [ADDRESS], GSTIN [GSTIN], PAN [PAN]
(the "Contractor")

1.  SCOPE OF WORK
    The Contractor shall execute and complete [DESCRIBE THE WORK, e.g. the civil
    and interior works for the residential building] at [SITE ADDRESS], strictly
    in accordance with:
        Annexure A : Bill of Quantities and rate schedule
        Annexure B : Drawings numbered [NUMBERS]
        Annexure C : Technical specifications
    Any work not covered by the above is outside scope and requires a written
    variation order before execution.

2.  CONTRACT PRICE
    2.1 The total contract price is Rs. [AMOUNT]/- (Rupees [IN WORDS] only),
        exclusive of GST, on a [LUMP SUM / ITEM RATE] basis.
    2.2 [For item-rate contracts] Payment shall be based on actual measured
        quantities at the rates in Annexure A, jointly measured and recorded in
        the measurement book.
    2.3 Rates are firm and not subject to escalation for [NUMBER] months from
        the date of this Work Order.

3.  TIME OF COMPLETION
    3.1 The Contractor shall commence work within [NUMBER] days of the site
        being handed over, and shall complete the work within [NUMBER] days
        from the date of commencement.
    3.2 Milestones:
            Milestone 1 : [DESCRIPTION] - by [DATE]
            Milestone 2 : [DESCRIPTION] - by [DATE]
            Milestone 3 : [DESCRIPTION] - by [DATE]
    3.3 TIME IS OF THE ESSENCE.

4.  EXTENSION OF TIME
    The Contractor shall be entitled to a reasonable extension of time for delay
    caused by the Employer, by a change in scope, by force majeure, or by any
    other cause beyond the Contractor's control, PROVIDED the Contractor gives
    written notice within [NUMBER] days of the event, failing which the claim
    shall be waived.

5.  LIQUIDATED DAMAGES
    If the Contractor fails to complete within the time allowed, the Contractor
    shall pay liquidated damages of [PERCENTAGE]% of the contract price per week
    of delay, subject to a maximum of [PERCENTAGE]% of the contract price. This
    is a genuine pre-estimate of loss and not a penalty.

6.  PAYMENT
    6.1 The Employer shall pay a mobilisation advance of Rs. [AMOUNT]/-
        ([PERCENTAGE]%), recoverable proportionately from running bills.
    6.2 Running account bills shall be submitted [MONTHLY / ON MILESTONE
        COMPLETION] and paid within [NUMBER] days of certification.
    6.3 Retention of [PERCENTAGE]% shall be deducted from each bill, half
        released on completion and the balance on expiry of the defect liability
        period.
    6.4 Statutory deductions including TDS and GST TDS shall be made as
        applicable.

7.  MATERIALS AND WORKMANSHIP
    7.1 All materials shall be new, of the specified brand and quality, and
        approved by the Employer or the consultant before use.
    7.2 The Employer may reject any material or work not conforming to the
        specification, and the Contractor shall remove and redo it at its own
        cost.

8.  DEFECT LIABILITY
    The Contractor shall rectify, at its own cost, any defect appearing within
    [NUMBER] months from the date of completion, within [NUMBER] days of written
    notice.

9.  LABOUR, SAFETY AND STATUTORY COMPLIANCE
    9.1 The Contractor shall be solely responsible for its workmen, their wages,
        provident fund, ESI and welfare, and shall comply with all applicable
        labour laws.
    9.2 The Contractor shall maintain safety at site, provide protective
        equipment, and shall not employ child labour.
    9.3 The Contractor shall take and maintain workmen's compensation insurance
        and contractor's all-risk insurance, and shall produce the policies on
        demand.
    9.4 The Contractor shall indemnify the Employer against all claims arising
        from any accident, injury or death at site.

10. VARIATIONS
    No variation shall be executed without a written variation order signed by
    the Employer, stating the description, the rate and the time impact.

11. TERMINATION
    The Employer may terminate this Work Order if the Contractor abandons the
    work, fails to proceed with due diligence, or commits a material breach not
    cured within [NUMBER] days of written notice. On termination the Employer
    may complete the work through another agency at the Contractor's risk and
    cost.

12. DISPUTE RESOLUTION
    Disputes shall first be referred to [THE ARCHITECT / PROJECT MANAGER] for a
    decision within [NUMBER] days, and failing resolution, to arbitration by a
    sole arbitrator under the Arbitration and Conciliation Act, 1996, seated at
    [CITY].


For the Employer                              For the Contractor


____________________                          ____________________
[NAME]                                        [NAME], [DESIGNATION]

WITNESSES:
1. ____________________                       2. ____________________
""",
        "keywords": ["work order", "construction contract", "contractor", "boq", "liquidated damages", "retention", "defect liability", "civil work"],
    },
]

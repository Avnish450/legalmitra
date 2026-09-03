# -*- coding: utf-8 -*-
"""
docs/evaluate.py
================
Measures how accurate the offline chatbot engine is.

We wrote 30 test questions the way a real visitor would type them - in plain,
non-legal English - and recorded which knowledge-base page SHOULD be returned.
The script then asks the engine each question and checks whether the correct
page came back first (Top-1) or anywhere in the first three results (Top-3).

Run it from the project folder:

    python docs/evaluate.py
"""

import os
import sys

# Allow this file to import the project modules that sit one folder above.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import chatbot  # noqa: E402

# (question typed by a user, id of the page that should be returned)
TEST_SET = [
    ("what are my rights if the police arrest me",        "arrest-and-bail"),
    ("police is not registering my complaint",            "fir-filing"),
    ("someone gave me a cheque and it bounced",           "cheque-bounce"),
    ("my landlord is not returning my security deposit",  "rent-and-tenancy"),
    ("builder has not given possession of my flat",       "rera"),
    ("my company fired me without any notice",            "termination-law"),
    ("employer has not paid my salary for two months",    "employee-rights"),
    ("how do i protect my brand name",                    "trademark-registration"),
    ("someone copied my website content",                 "copyright-basics"),
    ("i invented a machine how do i protect it",          "patents"),
    ("money was stolen from my bank account online",      "cybercrime-reporting"),
    ("what data can an app collect about me",             "data-protection"),
    ("i want to divorce my husband by mutual consent",    "divorce-maintenance"),
    ("who gets the property if there is no will",         "succession-inheritance"),
    ("i want to adopt a child",                           "child-custody"),
    ("shop sold me a defective phone and refuses refund", "consumer-complaint"),
    ("online seller is not accepting my return",          "ecommerce-consumer"),
    ("insurance company rejected my health claim",        "insurance-claims"),
    ("how do i start a private limited company",          "company-incorporation"),
    ("what compliance does a company have every year",    "corporate-compliance"),
    ("i want to ask the government for information",      "rti-act"),
    ("factory near my house is releasing smoke",          "pollution-control"),
    ("i was hit by a car and injured",                    "accident-compensation"),
    ("traffic police issued me a wrong challan",          "traffic-rules-challan"),
    ("bank is threatening to take my house",              "loans-and-recovery"),
    ("do i need to register for gst",                     "gst-basics"),
    ("i got a notice from the income tax department",     "tax-notices-appeals"),
    ("seniors are ragging me in my college hostel",       "ragging-and-campus"),
    ("doctor operated wrongly and i suffered",            "medical-negligence"),
    ("government is acquiring my land for a highway",     "land-acquisition"),
]


def run():
    top1 = 0
    top3 = 0
    rows = []

    for question, expected in TEST_SET:
        results = chatbot.ENGINE.search(question, limit=3)
        got = [r["entry"]["id"] for r in results]
        score = results[0]["score"] if results else 0.0

        hit1 = bool(got) and got[0] == expected
        hit3 = expected in got

        top1 += 1 if hit1 else 0
        top3 += 1 if hit3 else 0

        rows.append({
            "question": question,
            "expected": expected,
            "returned": got[0] if got else "-",
            "score": round(score, 3),
            "top1": "PASS" if hit1 else "fail",
            "top3": "PASS" if hit3 else "fail",
        })

    total = len(TEST_SET)
    print("=" * 96)
    print("CHATBOT RETRIEVAL ACCURACY TEST".center(96))
    print("=" * 96)
    print("{:<48} {:<26} {:>7} {:>6} {:>6}".format(
        "QUESTION (as a user would type it)", "PAGE RETURNED", "SCORE", "TOP1", "TOP3"))
    print("-" * 96)
    for row in rows:
        print("{:<48} {:<26} {:>7} {:>6} {:>6}".format(
            row["question"][:47], row["returned"][:25],
            row["score"], row["top1"], row["top3"]))
    print("-" * 96)
    print("Top-1 accuracy : {}/{}  =  {:.1f}%".format(top1, total, 100.0 * top1 / total))
    print("Top-3 accuracy : {}/{}  =  {:.1f}%".format(top3, total, 100.0 * top3 / total))
    print("=" * 96)

    return {
        "rows": rows,
        "total": total,
        "top1": top1,
        "top3": top3,
        "top1_pct": round(100.0 * top1 / total, 1),
        "top3_pct": round(100.0 * top3 / total, 1),
    }


if __name__ == "__main__":
    run()

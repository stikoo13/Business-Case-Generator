from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def generate_business_case(inputs, financials, risks, api_key=None):
    key = os.getenv("GROQ_API_KEY") or api_key
    client = Groq(api_key=key)

    risk_text = "\n".join([f"- {r['risk']} (Likelihood: {r['likelihood']}, Impact: {r['impact']})" for r in risks])

    prompt = f"""
You are a business analyst writing a clear and easy-to-understand business case.
Use simple, plain English. Avoid complicated words. Write like you are explaining 
to a manager who is not a technical person. Be clear, direct and specific.

PROJECT DETAILS:
- Company: {inputs['company']}
- Problem: {inputs['problem']}
- Proposed Solution: {inputs['solution']}
- Implementation Cost: {inputs['cost']:,}
- Annual Benefit: {inputs['annual_benefit']:,}
- Time Horizon: {inputs['years']} years
- Risk Level: {inputs['risk_level']}

CALCULATED FINANCIALS:
- ROI: {financials['roi_percent']}%
- NPV: {financials['npv']:,}
- Payback Period: {financials['payback_years']} years

IDENTIFIED RISKS:
{risk_text}

Write these 5 sections. Use simple everyday language. Keep each section short and clear.

## 1. Executive Summary
In 3 simple sentences: what is the problem, what is the solution, and what is the main benefit.

## 2. Problem Statement
Explain clearly what problem the company is facing right now and why it needs to be fixed.

## 3. Proposed Solution
Explain in simple words what we plan to do and how it will fix the problem.

## 4. Financial Justification
Explain the numbers in plain English. What does the ROI mean? When will the company get its money back? Is this a good investment?

## 5. Recommendation
Give a clear yes or no recommendation. State the top 2 reasons why this should be approved.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )

    return response.choices[0].message.content
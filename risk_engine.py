RISK_TEMPLATES = {
    "Low": [
        {"risk": "Minor scope creep", "likelihood": "Low", "impact": "Low", "mitigation": "Weekly scope review meetings with stakeholders."},
        {"risk": "Vendor delays", "likelihood": "Low", "impact": "Medium", "mitigation": "Build 2-week buffer into implementation timeline."},
    ],
    "Medium": [
        {"risk": "User adoption resistance", "likelihood": "Medium", "impact": "High", "mitigation": "Change management plan with training sessions and champions."},
        {"risk": "Data migration issues", "likelihood": "Medium", "impact": "High", "mitigation": "Run parallel systems for 4 weeks before full cutover."},
        {"risk": "Budget overrun", "likelihood": "Low", "impact": "High", "mitigation": "Monthly budget tracking with 10% contingency reserve."},
    ],
    "High": [
        {"risk": "Key stakeholder withdrawal", "likelihood": "Medium", "impact": "Critical", "mitigation": "Executive sponsor agreement signed before project start."},
        {"risk": "Technology failure", "likelihood": "Low", "impact": "Critical", "mitigation": "POC completed before full rollout. Rollback plan documented."},
        {"risk": "Regulatory non-compliance", "likelihood": "Medium", "impact": "Critical", "mitigation": "Legal review at design stage. Compliance officer sign-off required."},
        {"risk": "Data security breach", "likelihood": "Low", "impact": "Critical", "mitigation": "Security audit, penetration testing, encryption at rest and transit."},
    ]
}

def get_risks(risk_level):
    return RISK_TEMPLATES.get(risk_level, RISK_TEMPLATES["Medium"])
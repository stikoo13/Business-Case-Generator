# NEXIQ 🤖📊
### AI-Powered Business Case Generator

> Turn a business idea into a boardroom-ready proposal in minutes.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

---

## 🚀 What is NEXIQ?

NEXIQ is an AI-powered Business Case Generator that automates the entire process of creating a professional business case document. What normally takes a Business Analyst 6-8 hours is done in under 60 seconds.

Simply fill in your business problem, proposed solution, and financial details — NEXIQ handles the rest.

---

## ✨ Features

- 🧠 **AI-Generated Narrative** — Professionally written business case using Llama 3.3 70B via Groq
- 📊 **Automated Financial Modelling** — ROI, NPV, and Payback Period calculated instantly
- 📈 **Visual Charts** — Year-by-year financial projection and Cost vs Benefit comparison
- ⚠️ **Risk Matrix** — Automatically generated risk assessment with mitigation strategies
- 📄 **Export to Word or PDF** — Download a boardroom-ready document in one click
- 🔒 **Secure** — API keys stored safely, never exposed

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | Llama 3.3 70B via Groq API |
| Financial Engine | Custom Python module |
| Document Export | python-docx, ReportLab |
| Charts | Plotly |
| Deployment | Streamlit Cloud |

---

## ⚙️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/stikoo13/NEXIQ.git
cd NEXIQ
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your Groq API key**

Create a `.env` file in the root folder:


Get your free API key at [console.groq.com](https://console.groq.com)

**4. Run the app**
```bash
streamlit run app.py
```

---

## 📊 Sample Output

### What you fill in:
- **Company:** TechSoft Solutions
- **Problem:** Sales team spends 4 hours/day on manual data entry
- **Solution:** Implement Salesforce CRM automation
- **Cost:** ₹5,00,000
- **Annual Benefit:** ₹4,00,000

### What NEXIQ generates:
✅ Executive Summary  
✅ Problem Statement  
✅ Proposed Solution  
✅ Financial Justification (ROI, NPV, Payback Period)  
✅ Risk Matrix with Mitigations  
✅ Final Recommendation  
✅ Downloadable Word / PDF Document  

---

## 💡 Use Cases

- Business Analysts preparing project proposals
- Startups pitching ideas to investors
- Managers justifying new software purchases
- Students learning business case writing
- Consultants automating client deliverables

---

## 👨‍💻 Built By

**Sahir Tikoo** — Aspiring Business Analyst  
[GitHub](https://github.com/stikoo13) • [LinkedIn](http://www.linkedin.com/in/sahir-tikoo)

---

## 📜 License

MIT License — free to use and modify.
---

## 📁 Project Structure

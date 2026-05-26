import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import date
from financial_model import calculate_financials
from risk_engine import get_risks
from ai_generator import generate_business_case
from doc_exporter import export_to_word, export_to_pdf

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.set_page_config(page_title="AI Business Case Generator", layout="wide")

st.title("AI Business Case Generator")
st.caption("Turn a business idea into a boardroom-ready proposal in minutes.")

st.subheader("Fill in the details below")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("Company Name")
    problem = st.text_area("Problem Statement", placeholder="Describe the business problem you want to solve...")
    solution = st.text_area("Proposed Solution", placeholder="Describe what you plan to implement...")

with col2:
    cost = st.number_input("Implementation Cost (₹)", value=0, step=50000, min_value=0)
    st.caption(f"Entered: ₹{cost:,}")

    annual_benefit = st.number_input("Expected Annual Benefit (₹)", value=0, step=25000, min_value=0)
    st.caption(f"Entered: ₹{annual_benefit:,}")

    years = st.slider("Time Horizon (Years)", 1, 7, 3)
    risk_level = st.selectbox("Risk Level", ["Low", "Medium", "High"])

generate_btn = st.button("Generate Business Case", type="primary", use_container_width=True)

if generate_btn:
    if not company or not problem or not solution:
        st.error("Please fill in all the fields before generating.")
    elif cost == 0 or annual_benefit == 0:
        st.error("Please enter the implementation cost and expected annual benefit.")
    else:
        inputs = {
            'company': company,
            'problem': problem,
            'solution': solution,
            'cost': cost,
            'annual_benefit': annual_benefit,
            'years': years,
            'risk_level': risk_level,
            'date': date.today().strftime("%B %d, %Y")
        }

        with st.spinner("Calculating financials..."):
            financials = calculate_financials(cost, annual_benefit, years)

        risks = get_risks(risk_level)

        with st.spinner("AI is writing your business case..."):
            narrative = generate_business_case(inputs, financials, risks)

        # Save everything to session state
        st.session_state['generated'] = True
        st.session_state['inputs'] = inputs
        st.session_state['financials'] = financials
        st.session_state['risks'] = risks
        st.session_state['narrative'] = narrative
        st.session_state['show_download_options'] = False

# Show results if already generated
if st.session_state.get('generated'):

    inputs = st.session_state['inputs']
    financials = st.session_state['financials']
    risks = st.session_state['risks']
    narrative = st.session_state['narrative']

    # KPI cards
    st.subheader("Financial Summary")
    k1, k2, k3 = st.columns(3)
    k1.metric("ROI", f"{financials['roi_percent']}%")
    k2.metric("NPV", f"₹{financials['npv']:,}")
    k3.metric("Payback Period", f"{financials['payback_years']} years")

    # Two charts
    df = pd.DataFrame(financials['yearly_data'])
    total_benefit = inputs['annual_benefit'] * inputs['years']

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        fig1 = go.Figure()
        fig1.add_bar(
            x=df['year'], y=df['annual_benefit'],
            name='Annual Benefit', marker_color='#2ecc71'
        )
        fig1.add_scatter(
            x=df['year'], y=df['cumulative_net'],
            mode='lines+markers', name='Cumulative Net Benefit',
            line=dict(color='#3498db', width=3)
        )
        fig1.add_hline(
            y=0, line_dash="dash", line_color="red",
            annotation_text="Break-even point"
        )
        fig1.update_layout(
            title="Year-by-Year Financial Projection",
            height=380, plot_bgcolor='white'
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col_chart2:
        fig2 = go.Figure()
        fig2.add_bar(
            x=["Implementation Cost", f"Total Benefit over {inputs['years']} yrs"],
            y=[inputs['cost'], total_benefit],
            marker_color=['#e74c3c', '#2ecc71'],
            text=[f"₹{inputs['cost']:,}", f"₹{total_benefit:,}"],
            textposition='outside'
        )
        fig2.update_layout(
            title="Total Cost vs Total Benefit",
            height=380,
            plot_bgcolor='white',
            yaxis_title="Amount (₹)"
        )
        st.plotly_chart(fig2, use_container_width=True)

    # Risk matrix
    st.subheader("Risk Matrix")
    risk_df = pd.DataFrame(risks)
    risk_df.index = range(1, len(risk_df) + 1)
    st.dataframe(risk_df, use_container_width=True)

    # AI narrative
    st.subheader("Generated Business Case")
    st.markdown(narrative)

    # Download section
    st.subheader("Download Your Business Case")

    if st.button("Download", type="primary", use_container_width=True):
        st.session_state['show_download_options'] = True

    if st.session_state.get('show_download_options'):
        st.write("Choose your preferred format:")
        dl_col1, dl_col2 = st.columns(2)

        with dl_col1:
            word_file = export_to_word(inputs, financials, risks, narrative)
            st.download_button(
                label="Word Document",
                data=word_file,
                file_name=f"business_case_{inputs['company'].lower().replace(' ', '_')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )

        with dl_col2:
            pdf_file = export_to_pdf(inputs, financials, risks, narrative)
            st.download_button(
                label="PDF Document",
                data=pdf_file,
                file_name=f"business_case_{inputs['company'].lower().replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
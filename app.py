import streamlit as st
import pandas as pd
from analyzer import calculate_budget, analyze_expenses
from explainer import answer_finance_question, build_summary
from report_generator import make_pdf

st.set_page_config(page_title="Personal Finance Advisor Bot", page_icon="💰", layout="wide")
st.title("💰 Personal Finance Advisor Bot")
st.caption("Simple budgeting, saving and SIP learning — based on your monthly income.")
st.info("Educational tool only. This is not financial advice. SIP returns are market-linked and not guaranteed.")

with st.sidebar:
    st.header("Monthly details")
    income = st.number_input("Monthly take-home income (₹)", min_value=0, value=30000, step=1000)
    st.subheader("Your monthly expenses")
    needs = st.number_input("Needs: rent, groceries, bills (₹)", min_value=0, value=15000, step=500)
    wants = st.number_input("Wants: shopping, outings (₹)", min_value=0, value=6000, step=500)
    savings = st.number_input("Current savings / investments (₹)", min_value=0, value=3000, step=500)
    submitted = st.button("Calculate my budget", type="primary")

if submitted or "budget" not in st.session_state:
    st.session_state.budget = calculate_budget(income, needs, wants, savings)
    st.session_state.expenses = {"Needs": needs, "Wants": wants, "Savings & investments": savings}

budget=st.session_state.budget
st.subheader("Your 50–30–20 budget")
cols=st.columns(3)
for col, label, amount, target in zip(cols, ["Needs (50%)","Wants (30%)","Savings (20%)"],
                                      [budget["needs_target"],budget["wants_target"],budget["savings_target"]],
                                      [50,30,20]):
    col.metric(label, f"₹{amount:,.0f}", f"{target}% of income")
st.write(f"**Monthly income:** ₹{budget['income']:,.0f}  |  **Recommended allocation:** ₹{budget['needs_target']+budget['wants_target']+budget['savings_target']:,.0f}")
st.caption("The 50–30–20 rule is a guideline, not a strict rule. Adjust it for your actual rent, family needs and goals.")

st.subheader("How your current spending compares")
df=analyze_expenses(income, st.session_state.expenses)
st.dataframe(df, use_container_width=True, hide_index=True)
if budget["remaining"] >= 0:
    st.success(f"After the expenses entered, you have ₹{budget['remaining']:,.0f} remaining.")
else:
    st.warning(f"Your entered expenses exceed income by ₹{abs(budget['remaining']):,.0f}. Review flexible spending first.")

st.subheader("Simple explanation")
st.write(build_summary(budget, st.session_state.expenses))

st.subheader("Ask the finance learning bot")
question=st.text_input("Ask about budgeting, savings, emergency funds or SIPs")
if st.button("Ask"):
    st.write(answer_finance_question(question, income))
    st.caption("General education only — not financial advice.")

st.download_button("Download budget report (PDF)", data=make_pdf(budget, st.session_state.expenses),
                   file_name="personal_finance_budget.pdf", mime="application/pdf")

def build_summary(budget, expenses):
    income=budget["income"]
    if income<=0:
        return "Enter a monthly income above ₹0 to see a budget explanation."
    total=budget["total_expenses"]
    if total>income:
        return (f"You entered ₹{total:,.0f} in monthly expenses against ₹{income:,.0f} income. "
                "That means your budget is short by ₹{:.0f}. Try separating essential costs from flexible "
                "spending and make small changes that are realistic.".format(total-income))
    saved=budget["actual_savings"]
    return (f"The 50–30–20 guideline suggests about ₹{budget['needs_target']:,.0f} for needs, "
            f"₹{budget['wants_target']:,.0f} for wants and ₹{budget['savings_target']:,.0f} for savings "
            f"from your income. You currently entered ₹{saved:,.0f} for savings and investments. "
            "Start with a manageable amount and review your budget each month.")

def answer_finance_question(question, income=0):
    q=(question or "").lower().strip()
    if not q: return "Type a question first."
    if any(x in q for x in ["50-30-20","50 30 20","budget"]):
        return "The 50–30–20 rule is a simple guide: around 50% for needs, 30% for wants and 20% for savings or debt goals. It is flexible; adjust it to your circumstances."
    if "sip" in q:
        return "A SIP (Systematic Investment Plan) lets you invest a fixed amount regularly in a mutual fund. The value can rise or fall; returns are not guaranteed. Understand risk, fees and your time horizon before investing."
    if any(x in q for x in ["emergency fund","emergency"]):
        return "An emergency fund is money kept accessible for unexpected costs such as a repair or temporary loss of income. A common learning goal is to build several months of essential expenses gradually."
    if any(x in q for x in ["save","saving"]):
        return "Try saving a small amount soon after receiving income, track spending, and keep savings for planned goals separate from everyday spending. Consistency matters more than starting with a large amount."
    if "expense" in q or "spend" in q:
        return "Record expenses by category for a month. Identify recurring costs and optional purchases, then choose one realistic category to reduce."
    return "I can explain budgeting, the 50–30–20 guideline, saving habits, emergency funds and SIP basics in simple terms. Ask about one of these topics."

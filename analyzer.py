import pandas as pd

def calculate_budget(income, needs=0, wants=0, savings=0):
    income=float(max(0, income))
    needs=float(max(0, needs)); wants=float(max(0, wants)); savings=float(max(0, savings))
    return {
        "income": income,
        "needs_target": income*0.50,
        "wants_target": income*0.30,
        "savings_target": income*0.20,
        "actual_needs": needs,
        "actual_wants": wants,
        "actual_savings": savings,
        "total_expenses": needs+wants+savings,
        "remaining": income-(needs+wants+savings)
    }

def analyze_expenses(income, expenses):
    rows=[]
    targets={"Needs":0.50,"Wants":0.30,"Savings & investments":0.20}
    for category, amount in expenses.items():
        amount=float(amount)
        target=float(income)*targets.get(category,0)
        rows.append({"Category":category,"Entered (₹)":amount,"Suggested (₹)":target,
                     "Difference (₹)":amount-target,
                     "Status":"Within guideline" if amount<=target else "Above guideline"})
    return pd.DataFrame(rows)

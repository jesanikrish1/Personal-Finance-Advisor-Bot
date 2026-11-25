from analyzer import calculate_budget, analyze_expenses

def test_budget_50_30_20():
    b=calculate_budget(30000,15000,6000,3000)
    assert b["needs_target"]==15000
    assert b["wants_target"]==9000
    assert b["savings_target"]==6000
    assert b["remaining"]==6000

def test_negative_values_are_clamped():
    b=calculate_budget(-100,-1,-2,-3)
    assert b["income"]==0
    assert b["total_expenses"]==0

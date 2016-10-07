def calc_total_bill(bill, tax, tip):
    return bill_with_tax(bill, tax), bill_with_tax_and_tip(bill, tax, tip)

def bill_with_tax(bill, tax):
    return bill+bill*tax

def bill_with_tax_and_tip(bill, tax, tip):
    return bill+bill*tax+bill*tip

cost_with_tax, cost_with_tax_and_tip = calc_total_bill(140, 0.10, 0.10)
print cost_with_tax
print cost_with_tax_and_tip

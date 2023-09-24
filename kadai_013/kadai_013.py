def calc_tax(money,tax):
    tax_included = money * ((tax / 100) + 1)
    return tax_included

print(str(calc_tax(100,10))+'円')

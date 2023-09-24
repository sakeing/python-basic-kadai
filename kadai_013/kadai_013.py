def calc_tax(money,tax):
    tax_included = money * ((tax / 100) + 1)
    print(tax_included)

calc_tax(100,10)

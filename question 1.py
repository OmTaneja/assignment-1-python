GrossIncome = float(input('your gross income :- '))
dependents = int(input('enter number of dependents :- '))
taxable_income = round(GrossIncome) - 10000 -dependents*3000
a =taxable_income *0.2
print('tax is:',round(a,2))

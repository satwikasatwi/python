'''calculate EMI'''
p =int(input('principal amount:'))
t=int(input('time peroid'))
r=float(input('rate of intrest'))
si=(p*t*r)/100
EMI=(p+si)/t
print('EMI:',EMI)

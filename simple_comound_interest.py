
principal = float(input('Enter principal amount: '))
time = float(input('Enter time: '))
rate = float(input('Enter rate: '))
si = (principal * time * rate) / 100
print('Simple interest is: %f' % (si))
ci = principal * ( (1 + rate/100 )**time - 1)
print('Compound interest is: %f' %(ci))
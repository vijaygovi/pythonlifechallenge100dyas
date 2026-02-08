#simple_intrest
# Simple_intrest=P*T*R/100
P=int(input("Enter the Princple :"))
T=int(input("Enter the Time :"))
R=int(input("Enter the Ratio :"))
amount =P*T*R/100
Simple_intrest=amount
print(Simple_intrest)


# p=2000
# r=5
# t=3
# si=(p*t*r)/100
# print(si)

2.# compound_intrest

p=int(input("Enter the Princple :"))              #compound_intrest=p*(1+r/100)**t-p
t=int(input("Enter the Time :"))
r=int(input("Enter the Ratio :"))
amount =p*(1+r/100)**t
Compound_intrest=amount
print(Compound_intrest)
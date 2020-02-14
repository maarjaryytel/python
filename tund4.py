thislist = [1, 78, 25, 100, 56,]
muutuja=0
muutuja2=0
muutuja3=101

for x in thislist:
    if x> muutuja:
        muutuja2= muutuja
        muutuja=x
    if x< muutuja3:
        muutuja3=x

print(muutuja)
print(muutuja2)   
print(muutuja3)

x=max(thislist)
print(x)

x=min(thislist)
print(x)
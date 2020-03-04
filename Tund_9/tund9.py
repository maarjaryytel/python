kasutajaList = []

for x in range(5):
   kasutajaArv = int(input("Sisesta mingi number: "))
   kasutajaList.append(kasutajaArv)
print(kasutajaList)

kontrolliArv = int(input("Sisesta mingi arv: "))

for x in kasutajaList:
    if kontrolliArv > x:
        print("Suurem")
    if kontrolliArv < x:
        print("Väiksem")
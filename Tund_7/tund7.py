'''sisestus=int(input("sisesta: ")) #sisestan numbri

for x in range (sisestus):
    for x in range(sisestus):
        print("*", end =" ")
    print()'''

'''sisestus=int(input("sisesta number: ")) 
x= 1
for y in range(sisestus):
    for z in range(sisestus):
        print(z + x, end= " ")
    x= x + sisestus
    print()'''

'''for y in range(1,11):
    for x in range (1,11):
        #print(x*y, end=" ") #korrutamine
        print(y / x, end= " ") #jagamine
    print()'''

#meieList =[1, 2, 3, 4, 5]
#mitmeDim = [ [1, 2, 3],[4, 5, 6]]
#print(mitmeDim[0] [2])
#print(mitmeDim[1]) #kuvab teise listi

teiseDim = [[1,2], [3, 4]]
uusList= []
for x in range(0,2):
    for y in range(0,2):
        uusList.append(teiseDim[x] [y])
        print(teiseDim[x] [y])
print(uusList)
    
from math import *
#print("Hello \nWorld!")
##print("Minu nimi on Maarja", end=" ")
#print(23)
#print(5+5)
##pindala=20.34666
##print(pindala)
##print(pindala, "on pindala")
#kala=30
#print(pindala + kala)
#kokku=pindala*kala
#print(kokku)
#print("Pindala on %0.2f" %(pindala)) #2.f tähendab 2 kohta peale koma, 
#f tähendab floati; #tähendab vormindust

#kasutaja=input("Mis on su nimi? - ")
#print(kasutaja)

#arvEsimene=int(input("Esimene arv? - ")) #need on sõnad mitte numbrid, sellepärast paneb kokku, esialgses ei olnud ees inti
#arvTeine=int(input("Teine arv? - "))
#print(arvEsimene + arvTeine)

#meieEsimene= ["politsei", "tuletõrje", "kiirabi"]
##print(meieEsimene[])

#meieTeine=["haige", "terve"]
#print(meieTeine[])
#print(meieEsimene,meieTeine)

##külg =int(input("Sisesta ruudu külg: - "))
#print("Pindala: ", külg * 4)
#print(külg * külg)

#külgEsimene= int(input("Sisesta ristküliku esimene külg: - "))
#külgTeine= int(input("Sisesta ristküliku teine külg: - "))
#print(külgEsimene * külgTeine)

#külgEsimene = int(input("Sisesta kolmnurga külg: - "))
#kõrgus = int(input("Sisesta kolmnurga kõrgus: - "))
#print(külgEsimene * kõrgus / 2)

#matemaatika jaoks on vaja lisateeki, vt esimest rida
#print(abs(-3))
#print(round(2.6375,2))
#print(round(2.675)) #kui kohti ei näita, siis kuvab täisarvu
#print(5**3) #astendamine
#print(5//3) #mitu korda 5 jaguneb täisravulisena 3-ga, ehk 1

#tester = False
#topelt = True

#if 5+1==6:
    #print(topelt) 
#if 5+3==2:
    #print (topelt)

#värv= (input("Sisesta oma värv: "))

#if värv=="sinine":
    #print(1)

#if värv=="punane":
    #print(2)

#if värv=="must":
    #print(3)

#kasutaja sisestab mingi sõna vähemalt 8 tähte
#nimi="tester"
#print(len(nimi)) #len ehk pikkus
#if len(nimi)>8:
    #print("Liiga pikk")

nimi = (input("Sisesta oma nimi: - "))
print(len(nimi))

if len(nimi)>20:
    print("Liiga pikk nimi")

if len(nimi)<8:
    print("Liiga lühike nimi")

elif len(nimi)>3:
    print("Tõene")

else:
    print("Nojah")

if(2==2):
    print("test1")

    #shorthand if
if 3>2: print("shorthand")
if 2==3 or / and 2==2 

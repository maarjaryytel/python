#import random as rand
#suvaline=rand.randint(1,20)
#print(suvaline)

'''from random import randint
arvutiarv= randint (0, 101)

muutuja=True

kasutajaArv=int(input("Paku oma arv: "))

while muutuja:

    if kasutajaArv > arvutiarv:
        print("Liiga suur number!")
        kasutajaArv=int(input("Paku oma arv: "))

    if kasutajaArv < arvutiarv:
        print("Liiga vaike number!")
        kasutajaArv=int(input("Paku oma arv: "))

    if kasutajaArv == arvutiarv:
        print("Õige vastus!")
        muutuja=False'''

'''thisdict={
    "mark": "Audi",
    "mudel":"Quattro",
    "aasta":1996
}
print(thisdict)

x=thisdict["mudel"]
print(x)

y=thisdict.get("mudel") #sama mis eelmine
print(y)

thisdict["värv"]="punane" # lisab uue elemendi massiivi ehk värvi
print(thisdict)  

thisdict["aasta"]=2018 #muudab aastat
print(thisdict)


thisdict.pop("mudel") #eemaldab mudeli, kui mul on mingi spets. väärtus, siis eemaldan removega j kui tahan kõik tühjaks teha, siis clear
print(thisdict)

#koosta programm, mis annab ette sõnastiku tühjade väärtustega ja 
#ja laske kasutajal see täita

tuhi={} ##tühi sõnastik

for x in range (6):
    kategooria= input("kategooria") #küsime kasutajalt kat ja salvestamise muutujasse
    vaartus= input("väärtus")
    tuhi[kategooria]=vaartus
print(tuhi)'''

'''thisdict={
    "tõug":"Puudel",
    "sugu":"isane",
    "vanus":5
}
print(thisdict)

for x in thisdict: 
    inputVariable= input(" - ")
    if inputVariable == "ALL":
        break

    else:
        thisdict[x]=inputVariable
print(thisdict)'''

#lambda on anonüümne üksikfuntksioon, tavaliselt üherealine

'''x=lambda a: a+10  #a on sisend, a+10 on see mida ta teeb
print(x(5))
##seda lambdat saan hiljem välja kutsuda

teine=lambda a,b: a+b
print(teine(10,20))

kolm=lambda a,b,c: a*b*c
print(kolm(1,2,3))

neli=lambda a,b,v: a*b*v
print(neli(20,30,10,), "cm3")'''


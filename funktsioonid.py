#koodiplokid mis jooksevad ainutl siis kui kutsutakse
#saab edastada infot

##def hello(sisend, muuSisend): ##sisend on sulgudes
    ##print(sisend + muuSisend)
#def hello(**sisend) kasutame tärne kui me ei tea,palju infot tuleb
##hello(10,10)

#def hello(**sisend):
    #print(sisend["aasta"])
#hello(mudel="kala", aasta=1990)

#def vastus(x): #funtk ise vastu midagi ei anna
    #kui tahame midagi kätte saada, siis kasutame returni
    #return 20*x
#tester =vastus(30) #vastus 30 asendub 20*x
#print(tester)

#skoop- kui me teeme funkts, siis funtk sees olevat muutujat kätte ei saa,
#selleks et muutujat kätte saada peame selle def funkt väljas 

#def ruuduPindala(a):
    #return a*a

#print(ruuduPindala(10)) #väärtuse anname alles siis kui kutsume välja

#def numbrid():
    #for x in range(1,11):
        #print(x)

#numbrid() #kutsume välja

#anname ette mingi 1-9
#loeb sealt edasi 100-ni


#def numbrid(algus):
 #   for x in range(algus,101):
  #      print(x)
#kasutajaArv=int(input("Sisesta arv: "))

#numbrid(kasutajaArv)

thislist = []
def sonad():
    
    for x in range(1,11):
        kasutajaSõna=input("Sisesta mingi sõna: ")
        
        thislist.append(kasutajaSõna)
        print(thislist)
sonad()
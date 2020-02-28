import os
#f on muutuja
#f = open("demo.txt", "r") #kutsume välja funkts open r täh read
#print(f.read(20)) #read prindib rea kaupa välja
#print(f.readline()) #esimese rea prindib

#tekstiSisu = f.read(100)
#print(tekstiSisu)

#testiList =[]
#for x in f:
    #print(x) # x on rida
    #testiList.append(x)
#print(testiList) #saame iga rea mingiks elemendiks listis

#fail oleks hea sulgeda, võtab mälu kui ei sulge
#f.close()
#x = open("teginfaili.txt", "x") #on create, teeb mulle ise uue faili

#f= open("teginfaili.txt", "a")
#f.write("LISASIN SELLE JUURDE FAILI!!!!") #lisab uude faili
#f.close()

'''f = open ("teginfaili.txt", "w") #write
f.write ("KIRJUTASIN ÜLE")
f.close()'''

#kustutame faili ära, on vaja lisateeki import os
#kontr kus fail asub
#if os.path.exists("teginfaili.txt"): #tagast booleani
    #print("olemas fail")
    #os.remove("teginfaili.txt")
    #print("fail kustutatud")
#else:
    #print ("Faili ei ole")

#tekitada 3 faili ja neile midagi sisse kirjutada

'''f = open ("teginfaili1.txt", "w")
k = open ("teginfaili2.txt", "w")
l = open ("teginfaili3.txt", "w")

f.write("ESIMENE TEKST!!!!")
k.write("TEINE TEKST!!!!")
l.write("KOLMAS TEKST!!!!")

f.close()
k.close()
l.close()

f= open("teginfaili1.txt", "w")
k= open("teginfaili2.txt", "w")
l= open("teginfaili3.txt", "w")

f.write ("KIRJUTASIN ÜLE")
k.write ("KIRJUTASIN ÜLE")
l.write ("KIRJUTASIN ÜLE")

f.close() #enne kustutamist tuleb sulgeda fail

if os.path.exists("teginfaili1.txt"): 
    print("olemas fail")
    os.remove("teginfaili1.txt")
    print("fail kustutatud")'''

#kuidas teha kausta ja kust kausta
os.mkdir("tegin kausta")
#os.rmdir("tegin kausta") #remove directory
os.chdir("./tegin kausta/") #change direc #peaksime õige pathi andma

#testimine, selleks on olemas käsklused

#try:
    #print(veatekst)
    #mingifunktsioon() #seda f pole olemas
    #print("hjkashfkh")

#except NameError: #nameerrorit kasutatakse kui muutujat pole olemas/nimi on valesti kirjutatud ehk see hjkashfkh rida
    #print("On tekkinud viga")
    #print("Muutujat pole olemas")
    #mingiArv = 10
    #print(mingiArv)
#except: 
    #print("on tekkinud mingi muu viga")
#except jookseb siis kui mingi viga on

#else: #kui ühtegi viga ei tekkinud
    #print("Ei tekkinud ühtegi viga")
#else jookseb siis kui ühtegi viga ei teki

#kui tekib viga, aga soovime mingit osa teha,
#siis on olemas finally
#finally:
   # print("Nüüd saan teha seda.")


'''try:
    f = open("testimine.py")
    f.write("ei saa kirjutada")

except:
    print("faili kirjutamisel tekkis probleem")

finally:
    f.close()'''

'''number = 20
if number > 10:
    raise Exception("Sorry see number ei sobi")
#annab veal informatsiooni juurde, print ei anna lisainfot'''

tekst = "tervist"

if not type(tekst) is int:
    raise TypeError("Ainult numbrid on lubatud")
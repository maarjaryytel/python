kasutajaValik= int(input("Vali number: 1- kivi, 2- paber, 3- käärid\n"))

from random import randint
arvutiValik= randint(1,3)
print(arvutiValik)
  
if kasutajaValik == 1 & arvutiValik == 1:
    print("Viik")

if kasutajaValik == 1 & arvutiValik == 2:
    print ("Kasutaja võit")

if kasutajaValik == 1 & arvutiValik == 3:
    print ("Arvuti võit")

if kasutajaValik == 2 & arvutiValik == 1:
    print("Arvuti võit")

if kasutajaValik == 2 & arvutiValik == 2:
    print ("Viik")

if kasutajaValik == 2 & arvutiValik == 3:
    print ("Kasutaja võit") 

if kasutajaValik == 3 & arvutiValik == 1:
    print ("Kasutaja võit")

if kasutajaValik == 3 & arvutiValik == 2:
    print ("Arvuti võit")

if kasutajaValik == 3 & arvutiValik == 3:
    print ("Viik")


#if kasutajaValik == 4 or kasutajaValik >4:
    #raise Exception("Sorry see number ei sobi")

#kasutajaValik= " " see on vale
#if type(kasutajaValik) is string:
   # raise TypeError("Ainult numbrid on lubatud")

try: #see on vale
    print(kasutajaValik)
except NameError: 
    print("On tekkinud viga")

    
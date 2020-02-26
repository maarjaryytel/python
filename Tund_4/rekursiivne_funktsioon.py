#on suuteline ennast välja kutsuma- rekursiivne
#arv astmes n

#stopper = True
#sygavus= 0
#def recursive(x):
    #while stopper:
        #if x<10:
            #print(x)
            #x=x+1
            #recursive(x) #funktsiooni sisse tuleb uuesti kirj funkt nimi

#recursive(sygavus)
#kasutame seda:
#kui on vaja uurida mingit objekti, mis ei ole numbritega
##meil on nö puu  ja siis ta käib seda harukaupa läbi 
# ja jätab juba käidud harud meelde ning
#liigub järgmise haru suunas
#ctr-c tuleb vajutada, et terminali
#töö ära lõpetada

#stopper = True
#sygavus2= 0
#def recursive(y):
    #while stopper:
        #if y<1000:
            #print(y)
            #y=y+12
            #recursive(y) 

#recursive(sygavus2)

#faktoriaali kaks varianti
#!6
#6!
#6x5x4x3x2x1

def faktoriaal(x):
    #elimineerime mida arvutama ei #peaks
    if x== 1:
        return 1
    else:
        return (x * faktoriaal(x-1))

number = 6
print("Numbri ", number, "\nfaktoriaal on", faktoriaal(number))

#eelnevate arvude summa
def summad(n):
    if n==1:
        return 1
    return n+summad(n-1)
print(summad(16))
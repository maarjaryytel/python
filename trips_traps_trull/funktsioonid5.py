'''globaalneMuutuja = 1

 def kordamisFunktsioon():
     print("hello")

def YheMuutujaga(tuhiMuutuja): #def ajal ei pea sellel väärtust olema, placeholder
    tuhiMuutuja = tuhiMuutuja + 1
    return(tuhiMuutuja) #returni väärtus läheb sinna funkts väjakutsumisse

YheMuutujaga(globaalneMuutuja)

listTest = [1,2,3]
print(YheMuutujaga(listTest))

def kaheMuutujaga(esimene, teine):
    retunr esimene + teine

print(kaheMuutujaga("kala", "karu"))

def parseList(listMillegaTeeme, mituKordaTeeme):
    for x in range(len(mituKordaTeeme)):
        print(listMillegaTeeme)

parseList(listTest, 10)'''


def tulemasFunktsioon():
    print("Tore et oled tulemas!")
    print()
        
    print("Millal sa tuled?")
        
    kasutajaVastus= input("jõuan 3 tundi hiljem")
    print(kasutajaVastus)
    
    arvutiKysimus =input("Küsimus: ")
    print(arvutiKysimus)
    
def minemasFunktsioon():
    print("Kahju, et oled minemas")

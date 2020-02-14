def kolmnurga_funktsioon():
    kolmnurgaAlus=int(input("Sisesta kolmnurga alus (cm): "))
    kolmnurgaKõrgus= int(input("Sisesta kolmnurga kõrgus (cm): "))
    kolmnurgaPindala=kolmnurgaAlus*kolmnurgaKõrgus/2
    ##print("Vastus on: ", kolmnurgaPindala) #parem on returni kasutada
    return kolmnurgaPindala


def ruudu_funktsioon():
    ruuduKylg=int(input("Sisesta ruudu külg (cm): "))
    ruuduPindala= ruuduKylg*ruuduKylg
    return ruuduPindala

def ristkyliku_funktsioon():
    kyljePikkus=int(input("Sisesta ristküliku külje pikkus (cm): "))
    kyljeLaius=int(input("Sisesta ristküliku külje laius (cm): "))
    ristkylikuPindala= kyljePikkus*kyljeLaius
    return ristkylikuPindala

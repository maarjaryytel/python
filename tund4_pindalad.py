from kolmnurk import kolmnurga_funktsioon
from kolmnurk import ruudu_funktsioon #see kolmnurk on faili nimi
from kolmnurk import ristkyliku_funktsioon

vastus=input("Vali: kolmnurk, ruut või ristkülik ")

if vastus=="kolmnurk":    
    print(kolmnurga_funktsioon())


if vastus=="ruut":
    print(ruudu_funktsioon())

if vastus=="ristkülik":
    print(ristkyliku_funktsioon())




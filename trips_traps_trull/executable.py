#meil on vaja mängijaid
#mängulauda
#xja 0
#reeglistik
#võitja
#jaotame mida meil kõigepealt oleks vaja

from functions import *

mangija = "x"
arvuti = "O"
mangKaib = True
#mis numbri ta sisestas
kaiguVaartus = 0

manguLaud =[".",".",".",".",".",".",".",".",".","." ]
#tahame joonistada mangulauda, teemf funktsi
sygavus = 0 #kui 9 käiku on tehtud, siis on viik

joonista(manguLaud)

#mangu ennast on vaja
#manguprotsess
while mangKaib:
    if sygavus < 9:
        joonista(manguLaud)
        kaiguVaartus = int(input("Sisesta käik -"))
        if manguLaud[kaiguVaartus] == ".": #kui seal on punkt, siis saab käia
            if sygavus %2:
                teeKaik(manguLaud, kaiguVaartus, arvuti) #kordamööda käivad
            else:
                teeKaik(manguLaud, kaiguVaartus, mangija)
        else:
            continue
        sygavus = sygavus + 1
    else:
        joonista(manguLaud)
        print("VIIK")
        mangKaib = False




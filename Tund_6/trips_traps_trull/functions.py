#mangulaua funtks
#meil on need 9 kasti listis  kõik üksteise järel
#peame saame 3x3
#nummerdame kastid ära 1-9

def joonista(laud):
    print(laud[7] + "|" + laud[8] + "|" + laud [9]) #saame kätte 7-nda kasti jne
    print(laud[4] + "|" + laud[5] + "|" + laud [6])
    print(laud[1] + "|" + laud[2] + "|" + laud [3])

def teeKaik(laud, kaik, kelle):
    if kaik < 10:
        laud[kaik] = kelle

def voidukontroll(laud, mangija):
    #see on sama mis iffidega
    return((laud[1] == mangija and laud [2] == mangija and laud [3] == mangija) or
    (laud[4] == mangija and laud [5] == mangija and laud [6] == mangija) or
    laud[7] == mangija and laud [8] == mangija and laud [9] == mangija or
    laud[1] == mangija and laud [4] == mangija and laud [7] == mangija or
    laud[2] == mangija and laud [5] == mangija and laud [8] == mangija or
    laud[3] == mangija and laud [6] == mangija and laud [9] == mangija or
    laud[1] == mangija and laud [5] == mangija and laud [9] == mangija or
    laud[3] == mangija and laud [5] == mangija and laud [7] == mangija)
    


    
    
    )
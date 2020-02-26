import os
x = open("teginfaili4.txt", "x")
#x= open("teginfaili4.txt", "a")
#x.close()
i = True
while i:    
    kasutajaTekst=input("Sisesta mingi tekst: ")
    if kasutajaTekst == "x": #kui kasutaja vajutab x,siis väljub
        i= False        
    else:
        x.write(kasutajaTekst)  #panin else, et ei kuvaks kasutaja sisestatud x-i
        print(kasutajaTekst)
x.close()
#terminalist ei jookse see kood
import requests #lheme selle req html koodi jrele
from bs4 import BeautifulSoup
page = requests.get('https://ilm.ee/')
print(page.content) #saame lehe info katte html

#nuud oleme lehekylje  katte saanud
#laseme selle sisu labi html parseri ja
#valja tuleb html sarnane kood, aga ta on paremini loetav

soup = BeautifulSoup(page.content, 'html.parser')

#nyyd otsin selle div kus on minu soovitud info sees
#otsime id-ga elemendi sealt html koodist
#hakkame otsingut kitsmaks tegema
#eemaldame yleliigse
result = soup.find(id="header-weather") #see id on htmli koodist
#print(result.prettify()) #prettify teeb loetavamaks

#otsime teksti klassiga div ylesse
#votame id-ga otsitud objekti ja otsime sealt seest div classiga ..
hetkeIlmList= result.find("div", class_="row nopadding tana")
#nyyd on vaja kattesaadud tekst valjaprintida
vastus=hetkeIlmList.text
print(vastus)

#funkt, mis teeb stringist listi
def convert(lst):
    return(lst[0].split())
    #kogu string yhte listi
vastusListSegane = [vastus]
vastusList = convert(vastusListSegane)
print(vastusList)

#funtk-tekitasin muutuja, otsisin meetodi, et saaks read eraldada Kui on .- siis on lause
#kui lopeb punktiga, siis lisab new line ja lisab lopliku lause stringi
#punkt ei pruugi igal pool olla, oleneb lehest
parseTester = "."
LoplikLause = ""
for x in vastusList:
    if x.endswith(parseTester):
        x=x+"\n"
    LoplikLause = LoplikLause + " " + x
print(LoplikLause)
import datetime

x= datetime.datetime.now()

print(x.strftime("%a"))#sisseehitatud strtime
#%a on päev, on tabelis kõik päevad, kuud

print(x.strftime("%H"))
print(x.strftime("%M"))
print(x.strftime("%X"))
print(x.strftime("%x"))
print(x.strftime("%d.%m.%Y"))
import datetime
import inspect

a = datetime.datetime.now()
b = datetime.datetime(2024,2,28)
a = a.date()
b = b.date()
def jourdif(a,b):
    j1 = a.strftime("%j")
    j2 = b.strftime("%j")

    if(j1 >= j2):
        return int(j1)-int(j2)
    else:
        return int(j2)-int(j1)    
  

print(f"différence de jours entre {a} et {b} est de {jourdif(a,b)} jours")


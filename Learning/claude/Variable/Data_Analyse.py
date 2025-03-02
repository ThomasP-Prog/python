def convert(a):
    a =  a.split(',') #change str separated with ',' into list
    return list(map(int,a)) #change str list into int list
def calcule(a):
    avr = 0
    for i in range(len(a)):
        avr = avr+(a[i])
    avr = avr/(i+1)
    print(f"Average : {avr}")
    print(f"Mini : {min(a)}")
    print(f"Maxi : {max(a)}")
    print(f"Somme : {sum(a)}")


def checkneg(a):
    for i in range(len(a)):
        if a[i] < 0:
            return True
    return False

    

comma = "3,-7,2,8,5"
print(comma)
comma = convert(comma)
calcule(comma)
print(checkneg(comma))
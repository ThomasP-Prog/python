def fahrenheit_to_celsius(fahrenheit) -> float:
    '''change fahrenheit into celsius
    '''
    return round((fahrenheit - 32) * 5 / 9, 1)

try:
    print("Entrez une température en fahrenheit :")
    f = float(input())
    c = fahrenheit_to_celsius(f)
    print(f"{f} degrés F = {c} degrés C")
except ValueError:
    print("Erreur: Veuillez entrer un nombre valide.")
print(fahrenheit_to_celsius.__doc__)
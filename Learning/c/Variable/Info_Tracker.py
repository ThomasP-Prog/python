# Utilisation d'un dictionnaire
def nouvelleListe():
    nom = input("Nom: ")
    age = input("age: ")
    taille = float(input("taille : "))
    prog = input("aimez vous programmer ? oui/non : ").lower()
    progbool = prog == "oui"
    info = {
        "nom": nom,
        "age": age,
        "taille": taille,
        "aime prog": progbool
    }

    return info

liste = []
liste.append(nouvelleListe())
liste.append(nouvelleListe())

for i, personne in enumerate(liste):
    print(f"\n--- Résumé des Informations: Personne {i+1} ---")
    print(f"Nom: {personne['nom']}")
    print(f"Age: {personne['age']} ans")
    print(f"Taille: {personne['taille']} mètres")
    print(f"Aime programmer: {'Oui' if personne['aime prog'] else 'Non'}")
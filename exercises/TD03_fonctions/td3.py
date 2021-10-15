#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    secondes = int(temps[0]) * (24 * 3600)
    secondes += int(temps[1]) * 3600
    secondes += int(temps[2]) * 60
    secondes += int(temps[3])
    return(secondes, "secondes")

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    secondes = seconde % 60
    minute = seconde  // 60
    minutes = minute % 60
    heure = minute // 60
    heures = heure % 24
    jours = heure // 24
    return(jours, heures, minutes, secondes)

temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

# Créer une fonction d'affichage d'un temps `afficheTemps`. Attention, les mots jour, heure et seconde doivent être au pluriel
# s'il y en a plusieurs. S'il y en a zéro, ils ne doivent pas apparaître. print(message, end="")` permet de ne pas sauter une
# ligne après un print. Vous pouvez écrire une fonction qui affiche un mot au pluriel ou non, appelée ensuite plusieurs fois
# par `afficheTemps` pour simplifier votre code.

def afficheTemps(temps):
    jour = int(temps[0])
    heure = int(temps[1])
    minute = int(temps[2])
    seconde = int(temps[3])
    if jour > 1:
        j = str(jour) + " jours"
    elif jour == 1:
        j = "1 jour"
    elif jour == 0:
        j = ""
    if heure > 1:
        h = str(heure) + " heures"
    elif heure == 1:
        h = "1 heure"
    elif heure == 0:
        h = ""
    if minute > 1:
        m = str(minute) + " minutes"
    elif minute == 1:
        m = "1 minute"
    elif minute == 0:
        m = ""
    
afficheTemps((1,0,14,23)) 
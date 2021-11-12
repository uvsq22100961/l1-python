#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    secondes = int(temps[0]) * (24 * 3600)
    secondes += int(temps[1]) * 3600
    secondes += int(temps[2]) * 60
    secondes += int(temps[3])
    return(secondes)

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
        print(str(jour) + " jours", end = " ")
    elif jour == 1:
        print("1 jour", end = " ")
    if heure > 1:
        print(str(heure) + " heures", end = " ")
    elif heure == 1:
        print("1 heure", end = " ")
    if minute > 1:
        print(str(minute) + " minutes", end = " ")
    elif minute == 1:
        print("1 minute", end = " ")
    if seconde > 1:
        print(str(seconde) + " secondes")
    elif seconde == 1:
        print("1 seconde")
    
afficheTemps((1,0,14,23)) 

#Ecrire une fonction qui demande à l'utilisateur de rentrer un nombre de jours, d'heures, de minutes et
#de secondes et qui renvoie un temps. Attention, si l'entrée utilisateur n'est pas correcte, par exemple 80 minutes,
#afficher un message d'erreur et s'arrêter.
#(Optionnel) Au lieu d'arêter le programme, demander de rentrer une nouvelle valeur, tant que 
#ce n'est pas une valeur correcte.

def demandeTemps():
    """Demande à l'utilisateur de rentrer un nombre de jours, d'heures, de minutes et de secondes et renvoie un temps"""
    jours = -1
    heures = 70
    minutes = 70
    secondes = 70
    while jours < 0 :
        jours = int(input("Rentrer un nombre de jours vallide!"))
    while heures > 24 or heures < 0:
        heures = int(input("Rentrer un nombre d'heures valide!"))
    while minutes > 60 or minutes < 0:
        minutes = int(input("Rentrer un nombre de minutes valide!"))
    while secondes > 60 or secondes < 0:
        secondes = int(input("Rentrer un nombre de secondes valide!"))
    return(jours, heures, minutes, secondes)
    
#afficheTemps(demandeTemps())

#On veut être capable d'additionner deux temps. Donner une fonction qui fait ce calcul,
#en utilisant les fonctions précédentes.

def sommeTemps(temps1,temps2):
    secondes1 = tempsEnSeconde(temps1)
    secondes2 = tempsEnSeconde(temps2)
    somme = secondes1 + secondes2
    somme = afficheTemps(secondeEnTemps(somme))
    return(somme)

sommeTemps((2,3,4,25),(5,22,57,1))

#On veut maintenant calculer un pourcentage d'un temps. Par exemple, 20% de 2 jours et 36 minutes correspond
 #à 9 heures, 43 minutes et 12 secondes.
#Implémenter la fonction `proportionTemps` puis appeler cette fonction en échangeant l'ordre des arguments mais en les nommant.

def proportionTemps(temps,proportion):
    secondes = tempsEnSeconde(temps)
    secondes *= proportion
    tempsFinal = secondeEnTemps(secondes)
    return(tempsFinal)

afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments

def echangeOrdre(temps):
    jours = str(int(temps[0]))
    heures = str(int(temps[1]))
    minutes = str(int(temps[2]))
    secondes = str(int(temps[3]))
    return(secondes + " secondes", minutes + " minutes", heures + " heures", jours + " jours")

print(echangeOrdre(proportionTemps((2,0,36,0),0.2)))

#On veut maintenant afficher un temps sous forme de date, en supposant que le temps 0 est le 1 janvier 1970 à 00:00:00.
#* Implémenter une fonction `tempsEnDate`qui donne la date sous la forme (année, jour, heure, minute, seconde).
#* Implémenter la fonction `afficheDate`qui affiche la date. 
#* (Optionnel) Gérer également les mois.

def tempsEnDate(temps):
    temps0 = (1970, 1, 0, 0, 0, 0)
    annee = 0
    mois = 1
    m1 = 0
    i = -1
    fevrier = 27
    m = 30
    a = 0
    b = 0
    c = 0
    while b < temps[0]:
        i = i ** a
        if i == 1:
            m = m + 1
        if temps[0] >= 59:
            m = fevrier
        m += m1
        if temps[0] >= m1:
            mois += 1
        m1 = m
        a += 1
        b += 1
    jours = temps[0] - m1
    print(temps[0])
    print(m1)
    annee = mois // 12
    mois %= 12
    c = (annee, mois, jours, temps[1], temps[2], temps[3])
    date = (temps0[0] + c[0], temps0[1] + c[1], temps0[2] + c[2], temps0[3] + c[3], temps0[4] + c[4], temps0[5] + c[5])
    return(date)


def afficheDate(date = -1):
    pass
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
print(tempsEnDate(temps))
afficheDate(tempsEnDate(temps))
afficheDate()
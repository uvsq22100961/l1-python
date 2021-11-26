#En partant d'un entier `n` de départ, on définit une suite d'entiers en obtenant chaque nouveau terme à partir du précédent
#  soit en le divisant par 2 s'il est pair, soit en le multipliant par 3 et en ajoutant 1 s'il est impair. 
#1. Sans écrire de programme, calculer les premières valeurs de la suite en chosissant `n = 3`.

n = 3
n = n*3+1
#print(n)
n = n/2
#print(n)

#2. Ecrire la fonction qui, à partir d'un entier initial, renvoie la liste des valeurs successives jusqu'à ce que la valeur
#  `1` soit atteinte (le dernier élément de la liste est donc toujours 1).

def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else: n = n*3+1
        l.append(n)
    return(l)

#print(syracuse(3))

#3. La conjecture de Collatz (ou problème de Syracuse) affirme que, quel que soit l’entier `n` que l’on choisisse
#  au départ, on finit toujours par arriver à 1 (ce résultat est une *conjecture*, c'est-à-dire qu'il n'a pas été
#  démontré, mais qu'il n'existe pas de contre-exemple connu). Écrire une fonction qui, en appelant la fonction précédente,
#  va vérifier si la conjecture est vraie pour `n` de 1 à `n_max`, où `n_max` est un paramètre de la fonction. 
#*Remarque*: si tout se passe bien, la fonction doit juste se terminer et renvoyer `True` par exemple. Sinon, c’est qu’on
#  sera entré dans une boucle infinie.

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(2,n_max + 1):
        syracuse(n_max)
    return("True")

#print(testeConjecture(10000))

#4. On appelle *temps de vol* de l’entier `n` le nombre d’étapes pour aller de `n` jusqu’à 1. Le temps de vol de 1 est 0,
#  le temps de vol de 3 est 7. Écrire une fonction qui, étant donné un paramètre `n`, renvoie son temps de vol.

def tempsVol(n):
    """ Retourne le temps de vol de n """
    t = len(syracuse(n)) - 1
    return(t)

#print("Le temps de vol de", 3, "est", tempsVol(3))

#5. Ecrire une fonction qui, étant donné un paramètre `n_max` renvoie la liste des temps de vol de tous les entiers
#  de 1 à `n_max`. *Indication*: utiliser une liste en compréhension.

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    l1 = []
    for i in range(1,n_max + 1):
        a = tempsVol(i)
        l1.append(a)
    return(l1)
    l1 = [tempsVol(i) for i in range(1, n_max +1)]

#print(tempsVolListe(100))

#6. Déterminer quel entier entre 1 et 10000 a le plus grand temps de vol (réponse 6171 qui a le temps de vol 261).

def PGTV(n):
    a = n
    n = tempsVolListe(n)
    pgtv = 0
    indice = 0
    for i in range(len(n)):
        if n[i] > pgtv:
            pgtv = n[i]
            indice = i+1
    print('l entier entre 1 et', a, 'qui a le plus grand temps de vol est', indice, 'qui a le temps de vol ', pgtv)

#PGTV(10000)

#7. L’altitude maximale de l'entier `n` est la plus grande valeur par laquelle passe `n` au cours de son vol.
#  Déterminer quel entier entre 1 et 10000 a la plus grande altitude maximale (réponse 27114424, atteint par
#  l'entier 9663). Ne pas hésiter à écrire de nouvelles fonctions pour cela.

def altitudeMaximale(n):
    '''Retourne la plus grande valeur par laquelle passe `n` au cours de son vol'''
    return(max(syracuse(n)))

def PGAM(n):
    '''Retourne l entier entre 1 et 10000 qui a la plus grande altitude maximale'''
    a = 0
    for i in range(1, n):
        b = altitudeMaximale(i)
        if b > a:
            a = b
            indice = i
    return(indice, a)

#print(PGAM(10000))

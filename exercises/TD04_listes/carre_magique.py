#3. Carré magique

#1. Sans écrire de programme, vérifier qu'il s'agit bien d'un carré magique, et donner sa constante magique.

34

#Les questions qui suivent doivent être traitées dans un script, qui peut s'appeler `carre_magique.py`. Pensez à utiliser
#  [PythonTutor](http://pythontutor.com/) et les outils de programmation pour résoudre les problèmes qui pourraient survenir.

#2. Créer une liste à deux dimensions affectée à  la variable `carre_mag` contenant ce carré magique.

carre_mag = [[0] * 4 for i in range(4)]
carre_mag[0] = [4, 14, 15, 1]
carre_mag[1] = [9, 7, 6, 12]
carre_mag[2] = [5, 11, 10, 8]
carre_mag[3] = [16, 2, 3, 13]

#3. Créer une deuxième liste affectée à la variable `carre_pas_mag` qui ne soit pas magique à partir
#  du carré magique en changeant le 3 en 7. 

carre_pas_mag = []

#import copy
#carre_pas_mag = copy.deepcopy(carre_mag)

for i in carre_mag:
    carre_pas_mag.append(list(i))

#for i in carre_mag:
#    carre_pas_mag.append(i.copy())

carre_pas_mag[3][2] = 7
#print(carre_pas_mag)

#4. Créer une fonction qui affiche la liste comme un carré.

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print(' '.join([str(j) for j in i]))

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)

#5. Ecrire une fonction qui teste si les lignes du carré ont toutes la même somme. Cette fonction renvoie
#  cette somme si c'est le cas, et `-1` sinon.

def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    a = 0
    for b in carre[0]:
        a += b
    for i in carre:
        c = 0
        for j in i:
            c += j
        if c != a:
            return(-1)
    return(a)

#print(testLignesEgales(carre_mag))
#print(testLignesEgales(carre_pas_mag))

#6. Même question mais en testant les colonnes.

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    test = 0
    for lignes in carre:
        test += lignes[0]
    e = 0
    for i in carre[0]:
        e += 1
    for element in range(len(carre[0])):
        somme = 0
        for ligne in range(len(carre)):
            somme += carre[ligne][element]
        if somme != test:
            return(-1)
    return(test)

#print(testColonnesEgales(carre_mag))
#print(testColonnesEgales(carre_pas_mag))

#7. Même question mais en testant les 2 diagonales.

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    somme1 = 0
    somme2 = 0
    for ligne in range(len(carre)):
        for element in range(len(carre[0])):
            if element == ligne:
                somme1 += carre[ligne][element]
            if element == len(carre[0]) - element:
                somme2 += carre[ligne][element]
    if somme1 != somme2:
        return(-1)
    return(somme1)

#print(testDiagonalesEgales(carre_mag))
#print(testDiagonalesEgales(carre_pas_mag))

#8. Créer une fonction qui teste si un carré est magique. Elle retourne `True` si c'est le cas et `False` sinon.

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testLignesEgales(carre) == testColonnesEgales(carre) == testDiagonalesEgales(carre) != -1:
        return(True)
    else: return(False)

#print(estCarreMagique(carre_mag))
#print(estCarreMagique(carre_pas_mag))

#9. Un carré d'ordre $n$ est *normal* s'il contient tous les entiers de 1 à $n^2$. Ecrire une fonction qui teste
#  si un carré est normal (pas nécessairement magique).

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    for entier in range(1, (len(carre[0])) ** 2 + 1):
        a = 0
        for ligne in range(len(carre)):#pour toutes les lignes du carre
            for element in range(len(carre[0])):#pour tous les elements de chaque lignes du carre
                if entier == carre[ligne][element]:
                    a = 1
                if (ligne == len(carre) - 1) and (a == 0):#== à la derniere ligne
                    if element == len(carre[0]) - 1:#== au dernier element
                        if carre[ligne][element] != entier:
                            return(entier, False)
    return(True)

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
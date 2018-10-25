#-*-coding:utf-8-*-
'''
fonctions:
 qui détermine si un nombre est premier (itératif + récursif)
 qui affiche les nombres premiers entre 10^13 et 10^13+100
        donner le temps de calcul: t1 = time.clock()
                                t2 = time.clock()
                                   print(t2-t1)
 qui affiche la décomposition en puissances de (1/2) d'un réel < 1
   ex:0.625 -> 101 (en se limitant aux 23 premiers termes)
      =1*0.5 + 0*0.25 + 1*0.125
'''
import time

def is_premier_iteratif(n):
    """
        Détermine si le nb est premier
    """
    boucler = True
    res = True
    diviseur = 2
    while boucler:
        if n%diviseur == 0:
            boucler = False
            res = False
        elif diviseur*diviseur > n:
            boucler = False
        else:
            diviseur += 1
    return res

def is_premier_recursif(n, a=2):
    """
        Détermine si le nb est premier
    """
    b = n/2
    res = False
    if b < a:
        res = True
    elif n%a == 0:
        res = False
    else:
        res = is_premier_recursif(n, a+1)
    return res

def affiche_premiers():
    """
        Affiche les nombres premiers entre 10^13 et 10^13+100
    """
    t1 = time.clock()
    start = pow(10, 13)
    i = start
    while i <= start+100:
        if is_premier_iteratif(i): # recuring algorithm not working: maximum recursion depth exceeded
            print(i, "est un nombre premier.")
        i += 1
    t2 = time.clock()
    print("Temps de calcul :", t2-t1, "secondes.")

def decomposition_recursif_correction(m, c, i):
    if i > 23:
        print("", end="")
    elif m == 0:
        print("0", end="")
    elif m == c:
        print("1", end="")
    else:
        if m > c:
            print("1", end="")
            decomposition_recursif_correction(m-c, c*0.5, i+1)
        else:
            print("0", end="")
            decomposition_recursif_correction(m, c*0.5, i+1)

def decomposition_recursif(n, i=0.5, res=""):
    """
        Retourne la décomposition en puissances de (1/2) d'un réel < 1
        n: nombre à décomposer
        i = 0.5 au premier appel de la fonction
        res: résultat sous forme de chaine de caractères. res = "" au premier appel de la fonction
    """
    if n != 0:
        res += str(int(n//i))
        if i <= n:
            n -= i
        res = decomposition_recursif(n, i/2, res)

    return res[:23]

def decomposition_iteratif(n):
    """
        Retourne la décomposition en puissances de (1/2) d'un réel < 1
        n: nombre à décomposer
        res: résultat sous forme de chaine de caractères
    """
    i = 0.5
    res = ""
    while n != 0:
        res += str(int(n//i))
        if i <= n:
            n -= i
        i /= 2

    return res[:23]

def main():
    """
        Fonction principale
    """
    n = 5
    m = 0.543
    print("Le nombre", n, "est-il premier ?", is_premier_iteratif(n))
    print("Le nombre", n, "est-il premier ?", is_premier_recursif(n))
    affiche_premiers()
    print(decomposition_recursif(m))
    print(decomposition_iteratif(m))
    decomposition_recursif_correction(m,0.5,1)
    return

if __name__ == '__main__':
    main()

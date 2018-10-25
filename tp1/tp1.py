#-*-coding:utf-8-*-

import os, math

# TP 1 Algorithmique et Programmation
# 12/09/2018
# Auteur :
# Geoffrey Delval


# -------------------------------------------------
# Fonction volumeCubeTroue
# Calcul du volume d'un cube troué par 3 parallélépipèdes de section carrée,
# orthogonaux à chaque face du cube.
# c : nombre réel, longueur d'une arête du cube
# u, v, w : nombres réels, longueurs des côtés des sections carrées des 3 parallélépipèdes
# Traitement des cas non conformes
# -------------------------------------------------

def volumeCubeTroue (c, u, v, w) :
    # insérer votre code ici
    res = -1.0

    volC = math.pow(c, 3)
    volU = u * u * c
    volV = v * v * c
    volW = w * w * c

    if (volC < volU) or (volC < volV) or (volC < volW):
       return "Erreur : le volume du cube est inferieur aux parallelepipedes definis." 

    # define highest volume
    highestVol = 0
    if (volU >= volV) and (volU >= volW):
        highestVol = volU
    elif (volV >= volU) and (volV >= volW):
        highestVol = volV
    else:
        highestVol = volW

    # substract other volumes from their truncated part
    if (highestVol == volU):
        volV = volV - (v*v*u)
        volW = volW - (w*w*u)
    elif (highestVol == volV):
        volU == volU - (u*u*v)
        volW == volW - (w*w*v)
    else:
        volU == volU - (u*u*v)
        volV = volV - (v*v*u)

    # holed cube volume calculation
    res = volC - volU - volV - volW

    return res

# -------------------------------------------------
# Fonction de test de la fonction "volumeCubeTroue"
# -------------------------------------------------

def testvolumeCubeTroue () :
    
    print("Tests de la fonction \"volumeCubeTroue\"")
    
    volume = volumeCubeTroue(4,3,2,1)
    print("testvolumeCubeTroue, test1 : ", volume)

    volume = volumeCubeTroue(4,2,2,2)
    print("testvolumeCubeTroue, test2 : ", volume)

    volume = volumeCubeTroue(4,0,0,0)
    print("testvolumeCubeTroue, test3 : ", volume)
    
    volume = volumeCubeTroue(4,4,4,4)
    print("testvolumeCubeTroue, test4 : ", volume)

    volume = volumeCubeTroue(1, 2, 3, 4)
    print("testvolumeCubeTroue, test5 : ", volume)
    
    print("fin des tests de la fonction \"volumeCubeTroue\"\n")

    return


# -------------------------------------------------
# Fonction de calcul de la hauteur de marée à une heure donnée, en fonction de
# h1, m1 : heure de la marée (haute ou basse)
# l1 = hauteur d'eau à l'horaire h1, m1
# h2, m2 : heure de la marée opposée suivante
# l2 = hauteur d'eau à l'horaire h2, m2
# h, m : heure à laquelle on veut connaître la hauteur d'eau
# Traitement des cas non conformes
# -------------------------------------------------

def hauteurMaree (h1, m1, l1, h2, m2, l2, h, m) :
    # insérer votre code ici
    res = -1.0

    # identify high and low tide in parameters
    if (l1 >= l2):
        heureMareeHaute, minuteMareeHaute, hauteurMareeHaute = h1, m1, l1
        heureMareeBasse, minuteMareeBasse, hauteurMareeBasse = h2, m2, l2
    else:
        heureMareeHaute, minuteMareeHaute, hauteurMareeHaute = h2, m2, l2
        heureMareeBasse, minuteMareeBasse, hauteurMareeBasse = h1, m1, l1

    # compute tidal hour (heure-marée)
    heureMareeHaute_minutes = heure2minutes(heureMareeHaute, minuteMareeHaute)
    heureMareeBasse_minutes = heure2minutes(heureMareeBasse, minuteMareeBasse)
    dureeMaree = max(heureMareeHaute_minutes, heureMareeBasse_minutes) - min(heureMareeHaute_minutes, heureMareeBasse_minutes)
    heureMaree = float(dureeMaree) / 6

    # compute tidal range (marnage)
    marnage = hauteurMareeHaute - hauteurMareeBasse

    # compute tidal height at given hour
    heureRecherchee_minutes = heure2minutes(h, m)
    difference = heureRecherchee_minutes - min(heureMareeHaute_minutes, heureMareeBasse_minutes)
    if (difference <= heureMaree):
        res = round(hauteurMareeBasse + (marnage/12), 2)
    elif (difference <= 2*heureMaree):
        res = round(hauteurMareeBasse + (marnage/4), 2)
    elif (difference <= 3*heureMaree):
        res = round(hauteurMareeBasse + (marnage/2), 2)
    elif (difference <= 4*heureMaree):
        res = round(hauteurMareeHaute - (marnage/4), 2)
    else: 
        res = round(hauteurMareeHaute - (marnage/12), 2)

    return res

# -------------------------------------------------
# Fonction qui retourne le nombre de minutes que représente une heure donnée
# h : heure
# m : minutes
# -------------------------------------------------
def heure2minutes(h, m) :

    return (h*60 + m)

# -------------------------------------------------
# Fonction de test de la fonction "hauteurMaree"
# ------------------------------------------------
def testHauteurMaree () :
    
    print("Tests de la fonction \"hauteurMaree\"")

    hauteur = hauteurMaree(11, 15, 3.5, 17, 30, 12, 14, 0)
    print("testHauteurMaree, test1 : ", hauteur)
    
    hauteur = hauteurMaree(6, 53, 1.0, 11, 59, 8.30, 10, 0)
    print("testHauteurMaree, test2 : ", hauteur)
    
    hauteur = hauteurMaree(18, 54, 6.45, 0, 15, 1.75, 20, 15)
    print("testHauteurMaree, test3 : ", hauteur)
    
    hauteur = hauteurMaree(14, 41, 1.85, 20, 7, 11.85, 16, 0)
    print("testHauteurMaree, test4 : ", hauteur)

    print("fin des tests de la fonction \"hauteurMaree\"\n")

    return

# -------------------------------------------------
# Fonction de calcul de l'émittance à l'aide de la formule de Planck E=2hC2 -5/(e((hC/KT)/)-1)
# emittance(T, lambda)
# T réel, la température (en degrés Kelvin)
# lambda (λ) la longueur d’onde du rayonnement (en m).
# Traitement des cas non conformes
# On définira les constantes :
# h=6.6256e-34 (constante de Planck),
# C=2.998e8m/s (célérité de la lumière),
# K=1.38054e-23 (constante de Boltzmann),
# -------------------------------------------------

def emittance (T, longueurDonde) :
    # insérer votre code ici
    res = -1.0
    PI = math.pi
    #os.system("echo "+str(pi))
    h = (6.6256 * math.pow(10,-34))
    C = (2.998 * math.pow(10,8))
    K = (1.38054 * math.pow(10,-23))

    res = 2 * PI * h * math.pow(C,2) * math.pow(longueurDonde,-5) / (math.exp(((h*C)/(K*T))/longueurDonde)-1)
    return res


# -------------------------------------------------
# Fonction de test de la fonction "emittance"
# ------------------------------------------------
def testEmittance () :

    print("Test de la fonction \"emittance\"")
    
    dFile = open("spectre.txt", 'w')
    for i in range (400, 800) :
        e = emittance(6500.0, float(i)/1000000000.0)
        dFile.write(str(i)+" "+str(e)+"\n")
    dFile.close()

    os.system("echo \"set terminal png\" > gscript")
    os.system("echo \"set output \'spectre.png\'\" >> gscript")
    os.system("echo \"plot \'spectre.txt\' w l\" >> gscript")
    os.system("gnuplot gscript")
    os.system("eog spectre.png")

    print("fin des tests de la fonction \"emittance\"\n")
    
    return

def main() :
    testvolumeCubeTroue()
    testHauteurMaree()
    testEmittance()
    return

if __name__ == '__main__':
    main()

/*
 
 ######  #     #   ###     #       #     ######
 #       ##    #  #   #                  #
 #       # #   #   #      ##      ##     #
 #####   #  #  #    #      #       #     #####
 #       #   # #     #     #       #     #
 #       #    ##  #   #    #       #     #
 ######  #     #   ###   #####   #####   ######    
 
 2017-2018
 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "effets_photom.h"

/*!
 \file effets-couleur.c
 \author
 \date
 \brief module des fonctions de correction de la couleur et de la luminosité des images
 */

/*!
 \fn void inversion_video(unsigned char *img, int n)
 \brief transforme l'image en "négatif"
 \param img : adresse du bitmap
 \param n : nombre d'octets de l'image = largeur * hauteur * taille de pixel

 */

unsigned char * inversion_videoNB(unsigned char *img, int xs, int ys)
{
    unsigned char *res=NULL;
    int i;
    
    res = calloc(xs*ys,1);
    for(i=0;i<xs*ys;i=i+1)
        res[i]=255-img[i];
    return res;
}

/*!
 \fn void plusClair(unsigned char *img, int n, int nbplan)
 \brief rend l'image plus claire en augmentant les niveaux de 5%. Les niveaux sont tronqués à 255.
 \param img : adresse du bitmap
 \param xs : largeur de l'image 
 \param ys : hauteur de l'image
 \param nbplan : 1 si image à niveaux de gris, 3 si image couleur
 */

/*
 unsigned char * plusClairNB(unsigned char *img, int xs, int ys)
{
    unsigned char *res=NULL;
    
    return res;
}
*/

/*!
 \fn unsigned char deriv1x(unsigned char *img, int sx, int sy, int nbplan)
 \param img : adresse du bitmap
 \param sx : largeur de l'image
 \param sy : hauteur de l'image
 \brief remplace chaque pixel à partir de la 2ème colonne par sa différence avec son voisin de gauche
 \brief les valeurs <= -128 sont ramenées à 0, celles >=127 à 255.
 \brief si image couleur traitement de chaque composante.
 */

/*
unsigned char * deriv1xNB(unsigned char *img, int sx, int sy)
{
    unsigned char *res=NULL;
    
    return res;
}
 */





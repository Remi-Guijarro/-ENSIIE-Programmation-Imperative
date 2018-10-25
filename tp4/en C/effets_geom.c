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

#include "effets_geom.h"

/*!
 \file effets-geom.c
 \author 
 \date
 \brief module contenant les fonctions de traitement géométrique des images
 
 */



/*!
 \fn void effetFonteNB(unsigned char *img, int sx, int sy, int nbplan)
 \param img : adresse du bitmap
 \param sx : largeur de l'image
 \param sy : hauteur de l'image
 \brief transforme l'image pour donner l'illusion que les parties sombres "fondent"
 \brief Principe : choisir aléatoirement (sx*sy) pixels (certains seront choisis plusieurs fois, d'autres 0)
 \brief si le pixel en dessous est plus clair, alors le remplacer par le pixel choisi
 */

/*
unsigned char * effetFonteNB(unsigned char *img, int sx, int sy)
{
    unsigned char *res=NULL;
 
    return res;
}
*/

/*!
 \fn unsigned char * quartImageNB(unsigned char *img, int sx, int sy, int nbplan)
 \param img : adresse du bitmap
 \param sx : largeur de l'image
 \param sy : hauteur de l'image
 \param nbplan : 1 si image à niveaux de gris, 3 si image couleur
 \brief Crée une image dehauteur sy/2 et de largeur sx/2 (en prenant un pixel sur 2)
 */

/*
unsigned char * quartImageNB(unsigned char *img, int sx, int sy)
{
    unsigned char * res = NULL;
    
    return res;
}
*/





#ifndef __EFFETS_COULEUR_H
#define __EFFETS_COULEUR_H

extern unsigned char * inversion_videoNB(unsigned char *img, int xs, int ys);
extern unsigned char * plusClairNB(unsigned char *img, int xs, int ys);
extern unsigned char * deriv1xNB(unsigned char *img, int xs, int ys);

extern unsigned char * plusClairRVB(unsigned char *img, int xs, int ys);
extern unsigned char * enNiveauxDeGris(unsigned char *img, int xs, int ys);


#endif
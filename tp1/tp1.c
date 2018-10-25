#include <stdio.h>
#include <math.h>

int max(int a, int b)
{
	int res;
	if(a >= b)
		res = a;
	else
		res = b;
	return res;
}

int min(int a, int b)
{
	int res;
	if(a <= b)
		res = a;
	else
		res = b;
	return res;
}

int heure2minutes(int h, int m) 
{
	return (h*60 + m);
}

float hauteurMaree (int h1, int m1, float l1, int h2, int m2, float l2, int h, int m)
{
    float res = -1.0;
    int heureMareeHaute, minuteMareeHaute;
    float hauteurMareeHaute;
    int heureMareeBasse, minuteMareeBasse;
    float hauteurMareeBasse;

    // identify high and low tide in parameters
    if (l1 >= l2)
    {
    	heureMareeHaute = h1, minuteMareeHaute = m1, hauteurMareeHaute = l1;
        heureMareeBasse = h2, minuteMareeBasse = m2, hauteurMareeBasse = l2;
    }
        
    else
    {
    	heureMareeHaute = h2, minuteMareeHaute = m2, hauteurMareeHaute = l2;
        heureMareeBasse = h1, minuteMareeBasse = m1, hauteurMareeBasse = l1;
    }
        
    // compute tidal hour (heure-marée)
    int heureMareeHaute_minutes = heure2minutes(heureMareeHaute, minuteMareeHaute);
    int heureMareeBasse_minutes = heure2minutes(heureMareeBasse, minuteMareeBasse);
    float dureeMaree = max(heureMareeHaute_minutes, heureMareeBasse_minutes) - min(heureMareeHaute_minutes, heureMareeBasse_minutes);
    float heureMaree = dureeMaree / 6;

    // compute tidal range (marnage)
    float marnage = hauteurMareeHaute - hauteurMareeBasse;

    // compute tidal height at given hour
    int heureRecherchee_minutes = heure2minutes(h, m);
    int difference = heureRecherchee_minutes - min(heureMareeHaute_minutes, heureMareeBasse_minutes);
    if (difference <= heureMaree)
        res = hauteurMareeBasse + (marnage/12.);
    else if (difference <= 2*heureMaree)
        res = hauteurMareeBasse + (marnage/4.);
    else if (difference <= 3*heureMaree)
        res = hauteurMareeBasse + (marnage/2.);
    else if (difference <= 4*heureMaree)
        res = hauteurMareeHaute - (marnage/4.);
    else 
        res = hauteurMareeHaute - (marnage/12.);

    return res;
}

int testHauteurMaree () 
{    
    printf("Tests de la fonction \"hauteurMaree\"\n");
    float hauteur;

    hauteur = hauteurMaree(11, 15, 3.5, 17, 30, 12, 14, 0);
    printf("testHauteurMaree, test1 : %1.2f\n", hauteur);
    
    hauteur = hauteurMaree(6, 53, 1.0, 11, 59, 8.30, 10, 0);
    printf("testHauteurMaree, test2 : %1.2f\n", hauteur);
    
    hauteur = hauteurMaree(18, 54, 6.45, 0, 15, 1.75, 20, 15);
    printf("testHauteurMaree, test3 : %1.2f\n", hauteur);
    
    hauteur = hauteurMaree(14, 41, 1.85, 20, 7, 11.85, 16, 0);
    printf("testHauteurMaree, test4 : %1.2f\n", hauteur);

    printf("fin des tests de la fonction \"hauteurMaree\"\n\n");

    return 0;
}

double volumeCubeTroue(double c, double u, double v, double w){  
    double volumeInitial = c * c * c;
    double volume1;
    double volume2;
    double volume3;
    if(u > v && u > w){
        volume1 = u * u  * c; 
        volume2 =  v * v *(c - u);
        volume3 = w * w * (c - u);
    }else if(v > u && v > w){
        volume1 = v * v  * c; 
        volume2 = u * u  *(c - v);
        volume3 = w * w * (c - v);
    }else{
        volume1 = w * w  * c; 
        volume2 = u * u  * (c - w);
        volume3 = v * v  * (c - w);
    }
    if(volume1 > volumeInitial){
        return -1;
    }
    volumeInitial -= volume1;
    volumeInitial -= volume2;
    volumeInitial -= volume3;
    
    if(volumeInitial < 0){
        return -1;
    }else{
        return volumeInitial;
    }
}

int testvolumeCubeTroue ()
{
    float volume;
    printf("Tests de la fonction \"volumeCubeTroue\"\n");
    
    volume = volumeCubeTroue(4,3,2,1);
    printf("testvolumeCubeTroue, test1 : %1.1f\n", volume);

    volume = volumeCubeTroue(4,2,2,2);
    printf("testvolumeCubeTroue, test2 : %1.1f\n", volume);

    volume = volumeCubeTroue(4,0,0,0);
    printf("testvolumeCubeTroue, test3 : %1.1f\n", volume);
    
    volume = volumeCubeTroue(4,4,4,4);
    printf("testvolumeCubeTroue, test4 : %1.1f\n", volume);

    volume = volumeCubeTroue(1, 2, 3, 4);
    printf("testvolumeCubeTroue, test5 : %1.1f\n", volume);
    
    printf("fin des tests de la fonction \"volumeCubeTroue\"\n\n");

    return 0;
}

double emittance (double T, double longueurDonde)
{
    double res = -1.0;

    double h = (6.6256 * pow(10,-34));
    double C = (2.998 * pow(10,8));
    double K = (1.38054 * pow(10,-23));

    res = 2 * M_PI * h * pow(C,2) * pow(longueurDonde,-5) / (exp(((h*C)/(K*T))/longueurDonde)-1);
    return res;
}

int testEmittance ()
{

    printf("Test de la fonction \"emittance\"\n");
    
    double e;
    FILE *f = fopen("spectre_c.txt", "w");
    if (f == NULL)
    {
        printf("Error opening file!\n");
        exit(1);
    }

    int i;
    for (i = 400 ; i < 800 ; i++)
    {
        e = emittance(6500.0, double(i)/1000000000.0);
        fprintf(f, "%d %e\n", i, e);
    }

    fclose(f);

    printf("fin des tests de la fonction \"emittance\"\n\n");
    
    return -1;
}

int main()
{
	testvolumeCubeTroue();
	testHauteurMaree();
    testEmittance();
	return 0;
}
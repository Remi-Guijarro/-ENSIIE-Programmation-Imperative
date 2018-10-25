/*
fonctions:
 qui détermine si un nombre est premier (itératif + récursif)
 qui affiche les nombres premiers entre 10^13 et 10^13+100
        donner le temps de calcul: t1 = time.clock()
                                t2 = time.clock()
                                   print(t2-t1)
 qui affiche la décomposition en puissances de (1/2) d'un réel < 1
   ex:0.625 -> 101 (en se limitant aux 23 premiers termes)
      =1*0.5 + 0*0.25 + 1*0.125
*/
//import time
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"
#include "time.h"

#define true 1
#define false 0
typedef int bool;

// Détermine si le nb est premier
bool is_premier_iteratif(unsigned long long n)
{
    bool boucler = true, res = true;
    unsigned long long diviseur = 2;

    while(boucler)
    {
      if(n%diviseur == 0)
      {
        boucler = false;
        res = false;
      }
      else if(diviseur * diviseur > n)
      {
        boucler = false;
      }
      else
      {
        diviseur++;
      }
    }
    return res;
}

// Détermine si le nb est premier
// a, b: intervalle
// a = 2
// b = n-1
bool is_premier_recursif(unsigned int n, unsigned int a)
{
  int b = n/2;
  bool res = false;
  if(b < a)
  {
    res = true;
  }
  else if(n%a == 0)
  {
    res = false;
  }
  else
  {
    res = is_premier_recursif(n, a+1);
  }
  return res;
}

// Affiche les nombres premiers entre 10^13 et 10^13+100
void affiche_premiers()
{
  clock_t t1 = clock();
  unsigned long long start = pow(10,13);
  unsigned long long i;
  for(i = start ; i < start+100 ; i++)
  {
    if(is_premier_iteratif(i)) // recuring algorithm not working: maximum recursion depth exceeded
    {
      printf("%llu est un nombre premier.\n", i);
    }
  }
  clock_t t2 = clock();
  printf("Temps de calcul : %f secondes", (double)(t2-t1) / CLOCKS_PER_SEC);
}

void decomposition_recursif(float n, float c, int i)
{
  if(i>23) printf("\n");
  else if(n == 0) printf("0");
  else if(n == c) printf("1");
  else
  {
    if(n > c) { printf("1"); decomposition_recursif(n-c, c*0.5, i+1); }
    else { printf("0"); decomposition_recursif(n, c*0.5, i+1); }
  }
}

void decomposition_iteratif(float n)
{
  double c = 0.5;
  int i = 1;
  bool boucler = true;
  while(boucler)
  {
    if(n < c)
    {
      printf("1");
      c *= 0.5;
      n-=c;
    }
    else if (i == 13)
    {
      boucler = false;
    }
    else
    {
      printf("0");
      c*=0.5;
    }
    i++;
  }
}

/*
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


*/

// Fonction principale
int main()
{
  unsigned int n = 5;
  float m = 0.625;
  printf("Le nombre %u est-il premier ? %s\n", n, (is_premier_iteratif(n) ? "True" : "False"));
  printf("Le nombre %u est-il premier ? %s\n", n, (is_premier_recursif(n, 2) ? "True" : "False"));
  affiche_premiers();
  printf("\n");
  decomposition_iteratif(m);
  decomposition_recursif(m,0.5,1);

  return 1;
}

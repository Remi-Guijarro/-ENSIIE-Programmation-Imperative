#include "stdio.h"
#include "stdlib.h"

#define SIZEOF(x) ( sizeof x / sizeof x[0] )

void printArray(int *array, size_t size)
{
  printf("[");
  for(size_t i = 0 ; i < size ; i++)
  {
    printf("%d", array[i]);
    if(i < size-1) printf(", ");
  }
  printf("]\n");
}

double max(double a, double b)
{
  double res = a;
  if(a<b) res = b;
  return res;
}

double sumArray(double *array, size_t size)
{
  double res = 0;
  for(size_t i = 0 ; i < size ; i++)
    res += array[i];
  return res;
}

char* conversionHeure(double heureDecimale)
{
  int heures = (int) heureDecimale;
  int minutes = (int)(heureDecimale*60)%60;
  int secondes = (int)(heureDecimale*3600)%60;

  char *res = malloc(sizeof(char) * 15);
  sprintf(res, "%dh %dmin %dsec", heures, minutes, secondes);
  return res;
}

int distanceTotale(int *parcours, size_t size)
{
  int res = 0;
  for(size_t i = 0 ; i < size ; i++)
  {
    res += parcours[i];
  }
  return res;
}

double tempsSurVelo(int *parcours, size_t size, int vitesse)
{
  return distanceTotale(parcours, size) / (double)vitesse;
}

double tempsTotalGeorges(int *parcours, size_t size)
{
  double res = tempsSurVelo(parcours, size, 25);

  for(size_t i = 0 ; i < size-1 ; i++)
  {
    if(parcours[i] > 10) res += 10./60;
    else res += 5./60;
  }

  return res;
}

double tempsTotalPopeye(int *parcours, size_t size)
{
  double res = tempsSurVelo(parcours, size, 15);
  for(size_t i = 0 ; i < size-1 ; i++)
    res += 10./60;
  return res;
}

void parcoursCoursiers(int *parcours, size_t size, int *georges, int *popeye)
{
  int pos = 0;
  for(size_t i = 0 ; i < size ; i++)
  {
    if(i % 2 == 0)
      georges[pos] = parcours[i];
    else
    {
      popeye[pos] = parcours[i];
      pos++;
    }
  }
}

double tempsLivraison(int *parcours, size_t size)
{
  double tempsFinal = 0;
  double *tempsGeorges = NULL;
  int sizeTempsGeorges = 0;
  double *tempsPopeye = NULL;
  int sizeTempsPopeye = 0;
  int reposGeorges = 0;

  if(parcours[0] > 10) reposGeorges = 10;
  else reposGeorges = 5;

  sizeTempsGeorges++;
  tempsGeorges = realloc(tempsGeorges, sizeof(double) * sizeTempsGeorges);
  tempsGeorges[0] = parcours[0]/25. + (reposGeorges/60.);
  sizeTempsPopeye++;
  tempsPopeye = realloc(tempsPopeye, sizeof(double) * sizeTempsPopeye);
  tempsPopeye[0] = parcours[1]/15. + (10./60);

  for(size_t i = 2 ; i < size ; i++)
  {
    if(sumArray(tempsGeorges, sizeTempsGeorges)
        <= sumArray(tempsPopeye, sizeTempsPopeye))
    {
      if(parcours[i] > 10) reposGeorges = 10;
      else reposGeorges = 5;
      sizeTempsGeorges++;
      tempsGeorges = realloc(tempsGeorges, sizeof(double) * sizeTempsGeorges);
      tempsGeorges[sizeTempsGeorges-1] = parcours[i]/25. + (reposGeorges/60.);
      if(i == size-1)
      {
        tempsGeorges = realloc(tempsGeorges, sizeof(double) * sizeTempsGeorges);
        tempsGeorges[sizeTempsGeorges-1] -= reposGeorges/60.;
      }
    }
    else
    {
      sizeTempsPopeye++;
      tempsPopeye = realloc(tempsPopeye, sizeof(double) * sizeTempsPopeye);
      tempsPopeye[sizeTempsPopeye-1] = parcours[i]/15. + (10./60);
      if(i == size-1)
      {
        tempsPopeye = realloc(tempsPopeye, sizeof(double) * sizeTempsPopeye);
        tempsPopeye[sizeTempsPopeye-1] -= 10./60;
        printf("okp\n" );
      }
    }
  }

  tempsFinal = max(sumArray(tempsGeorges, sizeTempsGeorges),
  sumArray(tempsPopeye, sizeTempsPopeye));
  free(tempsGeorges); free(tempsPopeye);
  return tempsFinal;
}

void Q1(int *parcours, size_t size)
{
  char *temps = conversionHeure(tempsSurVelo(parcours, size, 25));
  printf("1. Temps passé à vélo : %s\n", temps);
  free(temps);
}

void Q2(int *parcours, size_t size)
{
  char *temps  = conversionHeure(tempsTotalGeorges(parcours, size));
  printf("2. Temps total du parcours : %s\n", temps);
  free(temps);
}

void Q3(int *parcours, size_t size)
{
  size_t sizeGeorges, sizePopeye;
  if(size % 2 == 0)
    sizeGeorges = sizePopeye = size / 2;
  else
  {
    sizeGeorges = size / 2 + 1;
    sizePopeye = size / 2;
  }

  int georges[sizeGeorges];
  int popeye[sizePopeye];
  parcoursCoursiers(parcours, size, georges, popeye);

  printf("3. Parcours de Georges : ");
  printArray(georges, sizeGeorges);
  printf("   Parcours de Popeye : ");
  printArray(popeye, sizePopeye);
}

void Q4(int *parcours, size_t size)
{
  size_t sizeGeorges, sizePopeye;
  if(size % 2 == 0)
    sizeGeorges = sizePopeye = size / 2;
  else
  {
    sizeGeorges = size / 2 + 1;
    sizePopeye = size / 2;
  }

  int georges[sizeGeorges];
  int popeye[sizePopeye];
  parcoursCoursiers(parcours, size, georges, popeye);

  char *tempsGeorges = conversionHeure(tempsTotalGeorges(georges,sizeGeorges));
  char *tempsPopeye = conversionHeure(tempsTotalPopeye(popeye,sizePopeye));

  printf("4. Temps pour que Georges ait fini ses tournées : %s\n",
          tempsGeorges);
  free(tempsGeorges);
  printf("   Temps pour que Popeye ait fini ses tournées : %s\n",
          tempsPopeye);
  free(tempsPopeye);

}

void Q5(int *parcours, size_t size)
{
  char *temps = conversionHeure(tempsLivraison(parcours, size));
  printf("5. Temps de livraison : %s", temps);
  free(temps);
}

int main()
{
  int parcours[] = {19, 14, 4, 15, 21, 23, 23, 17, 12, 18, 10, 11, 5, 9, 16, 12, 18, 21};
  size_t size = SIZEOF(parcours);
  printArray(parcours, size);

  Q1(parcours, size);
  Q2(parcours, size);
  Q3(parcours, size);
  Q4(parcours, size);
  Q5(parcours, size);

  return EXIT_SUCCESS;
}

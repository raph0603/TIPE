// Langage : C
// Path: batiment.c

#include <time.h>
#include <stdbool.h> 
#include <stdlib.h>
#include <stdio.h>

double fmod(double x, double y) { // renvoie le reste de la division euclidienne de x par y sous forme de double
		return x - y * (int)(x / y);
		return x - y * (int)(x / y);
	double q = (int)x/(int)y;
	printf("fmod(%f, %f) = %f\n", x, y, x - y*q);
	return x - y*q;
}


typedef struct batiment batiment;
struct batiment
{
	int id;
	double consommation;
	bool etat;
};

batiment *batiment_new(int id, double consommation)
{
	batiment *b = malloc(sizeof(batiment));
	b->id = id;
	b->consommation = consommation;
	b->etat = true;
	return b;
}

void batiment_free(batiment *b)
{
	free(b);
}

void batiment_set_etat(batiment *b, bool etat)
{
	b->etat = etat;
}

bool batiment_get_etat(batiment *b)
{
	return b->etat;
}

double batiment_get_consommation(batiment *b)
{
	return b->consommation;
}

void batiment_print(batiment *b)
{
	printf("Batiment %d : %.2f %s \n", b->id, b->consommation, b->etat ? "ON" : "OFF");
}

void batiment_set_consommation_random(batiment *b)
{
	b->consommation = (fmod((double)rand(), (double)8000) + (double)10300)/(double) 100; // consommation: (taille moyenne) 71.4m² * 8 logement par batiments * 6kWh par jours / 24h ~= 143kWh => [103, 183]
}

// Example of use, batiments:

// int main(int argc, char const *argv[])
// {
// 	srand(time(NULL));
// 	batiment* b[10];
// 	for (int i = 0; i < 10; i++)
// 	{
// 		b[i] = batiment_new(i, 0);
// 		batiment_set_consommation_random(b[i]);
// 	}
// 	// Initialise des valeurs au hasard
// 	for (int i = 0; i < 10; i++)
// 	{
// 		batiment_set_etat(b[i], true);
// 		batiment_print(b[i]);
// 	}
// 	return 0;
// }
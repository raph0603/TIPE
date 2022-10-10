// Langage : C
// Path: batiment.c

#include <time.h>
#include <stdbool.h> 
#include <stdlib.h>
#include <stdio.h>



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
	printf("Batiment %d : %lf %s \n ", b->id, b->consommation, b->etat ? "ON" : "OFF");
}

// Example of use, batiments:

int main(int argc, char const *argv[])
{
	srand(time(NULL));
	batiment* b[10];
	for (int i = 0; i < 10; i++)
	{
		b[i] = batiment_new(i, rand() % 100);
	}
	// Initialise des valeurs au hasard
	for (int i = 0; i < 10; i++)
	{
		batiment_set_etat(b[i], true);
		batiment_print(b[i]);
	}
	return 0;
}

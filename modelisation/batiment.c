// Langage : C
// Path: batiment.c

#include <stdbool.h> 

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

int batiment_get_id(batiment *b)
{
	return b->id;
}

void batiment_print(batiment *b)
{
	printf("Batiment %d : %f %s \r ", b->id, b->consommation, b->etat ? "ON" : "OFF");
}

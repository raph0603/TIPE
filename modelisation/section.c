// Langage : C
// Path: section.c

#include <stdbool.h>
#include <stdlib.h>
#include "batiment.c"

typedef struct section section;
struct section
{
	int id;
	double consommation;	
	bool etat;
	batiment **batiments;
};


section *section_new(int id)
{
	section *s = malloc(sizeof(section));
	s->id = id;
	s->consommation = 0;
	s->etat = true;
	s->batiments = NULL;
	return s;
}

void section_free(section *s)
{
	free(s);
}

void section_set_etat(section *s, bool etat)
{
	s->etat = etat;
}

bool section_get_etat(section *s)
{
	return s->etat;
}

double section_get_consommation(section *s)
{
	return s->consommation;
}

int section_get_id(section *s)
{
	return s->id;
}

void section_print(section *s)
{
	printf("Section %d : %f %s \n ", s->id, s->consommation, s->etat ? "ON" : "OFF");
}

void section_add_batiment(section *s, batiment *b)
{
	s->batiments = realloc(s->batiments, sizeof(batiment *) * (s->id + 1));
	s->batiments[s->id] = b;
	s->id++;
}

void section_update_consommation(section *s)
{
	s->consommation = 0;
	for (int i = 0; i < s->id; i++)
	{
		if (batiment_get_etat(s->batiments[i]))
		{
			s->consommation += batiment_get_consommation(s->batiments[i]);
		}
	}
}

void section_print_batiments(section *s)
{
	for (int i = 0; i < s->id; i++)
	{
		batiment_print(s->batiments[i]);
	}
}

// Example of use:

// int main(int argc, char const *argv[])
// {
// 	section *s = section_new(0);
// 	section_add_batiment(s, batiment_new(0, 10));
// 	section_add_batiment(s, batiment_new(1, 20));
// 	section_add_batiment(s, batiment_new(2, 30));
// 	section_add_batiment(s, batiment_new(3, 40));
// 	section_add_batiment(s, batiment_new(4, 50));
// 	section_add_batiment(s, batiment_new(5, 60));
// 	section_add_batiment(s, batiment_new(6, 70));
// 	section_add_batiment(s, batiment_new(7, 80));
// 	section_add_batiment(s, batiment_new(8, 90));
// 	section_add_batiment(s, batiment_new(9, 100));
// 	section_print_batiments(s);
// 	section_update_consommation(s);
// 	section_print(s);
// 	section_set_etat(s, false);
// 	section_update_consommation(s);
// 	section_print(s);
// 	section_free(s);
// 	return 0;
// }
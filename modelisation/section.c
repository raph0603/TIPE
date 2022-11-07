// Langage : C
// Path: section.c

#include <stdbool.h>
#include <stdlib.h>
#include "batiment.c"

const int MAX_BATIMENTS = 100;

typedef struct section section;
struct section
{
	int id;
	int batiments_count;
	double consommation;	
	bool etat;
	batiment **batiments;
};


section *section_new(int id)
{
	section *s = malloc(sizeof(section));
	s->id = id;
	s->batiments_count = 0;
	s->consommation = 0;
	s->etat = true;
	s->batiments = NULL;
	return s;
}

void section_free(section *s)
{
	for (int i = 0; i < s->batiments_count; ++i)
	{
		batiment_free(s->batiments[i]);
	}
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
	printf("Verifying section %d...\n", s->id);
	printf("Section %d : %.2f %s \n ", s->id, s->consommation, s->etat ? "ON" : "OFF");
	printf("\n");
}

int section_add_batiment(section *s, batiment *b)
{
	if (s->batiments_count < MAX_BATIMENTS)
	{
		s->batiments = realloc(s->batiments, (s->batiments_count + 1) * sizeof(batiment *));
		b->id = s->batiments_count;
		s->batiments[s->batiments_count] = b;
		s->batiments_count++;
		return 0;
	}
	else return 1;
}

void section_update(section *s)
{
	printf("Updating section %d... \n", s->id);
	s->consommation = 0;
	for (int i = 0; i < s->batiments_count; i++)
	{
		if (batiment_get_etat(s->batiments[i]))
		{
			s->consommation += batiment_get_consommation(s->batiments[i]);
		}
	}
	printf("\n");
}

void section_print_batiments(section *s)
{
	printf("Printing batiments of section %d... \n", s->id);
	for (int i = 0; i < s->batiments_count; i++)
	{
		batiment_print(s->batiments[i]);
	}
	printf("\n");
}

void section_set_consommation_random(section *s)
{
	for (int i = 0; i < s->batiments_count; i++)
	{
		batiment_set_consommation_random(s->batiments[i]);
	}
}

// Example of use:

// int main(int argc, char const *argv[])
// {
// 	srand(time(NULL));
// 	printf("\n");
// 	section *s = section_new(0);
// 	for (int i = 0; i < 120; i++)
// 	{
// 		section_add_batiment(s, batiment_new(i, 0)) ? printf("Error adding batiment %d to section %d, max batiments reached\n", i, s->id) : printf("Batiment %d added to section %d \n", i, s->id);
// 	}
// 	section_set_consommation_random(s);
// 	section_print_batiments(s);
// 	section_print(s);
// 	section_update(s);
// 	section_print(s);
// }
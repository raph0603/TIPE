// Langage : C
// Path: ville.c

#include <stdbool.h>
#include <stdlib.h>
#include "section.c"

const int MAX_SECTIONS = 100;

typedef struct ville ville;
struct ville
{
	int id;
	int sections_count;
	double consommation;
	bool etat;
	section **sections;
};


ville *ville_new(int id)
{
	ville *v = malloc(sizeof(ville));
	v->id = id;
	v->sections_count = 0;
	v->consommation = 0;
	v->etat = true;
	v->sections = NULL;
	return v;
}

void ville_free(ville *v)
{
	for (int i = 0; i < v->sections_count; ++i)
	{
		section_free(v->sections[i]);
	}
	free(v);
}

void ville_set_etat(ville *v, bool etat)
{
	v->etat = etat;
}

bool ville_get_etat(ville *v)
{
	return v->etat;
}

double ville_get_consommation(ville *v)
{
	return v->consommation;
}

int ville_get_id(ville *v)
{
	return v->id;
}

void ville_print(ville *v)
{
	printf("Verifying ville %d...\n", v->id);
	printf("Ville %d : %f %s \n ", v->id, v->consommation, v->etat ? "ON" : "OFF");
	printf("\n");
}

int ville_add_section(ville *v, section *s)
{
	if (v->sections_count < MAX_SECTIONS)
	{
		v->sections = realloc(v->sections, (v->sections_count + 1) * sizeof(section *));
		v->sections[v->sections_count] = s;
		v->sections_count++;
		return 0;
	}
	else return 1;
}

void ville_print_sections(ville *v)
{
	printf("Printing batiments of section %d... \n", v->id);
	for (int i = 0; i < v->sections_count; i++)
	{
		section_print(v->sections[i]);
	}
	printf("\n");
}

void ville_print_batiments(ville *v)
{
	printf("Printing batiments of section %d... \n", v->id);
	for (int i = 0; i < v->sections_count; i++)
	{
		for (int j = 0; j < v->sections[i]->batiments_count; j++)
		{
			batiment_print(v->sections[i]->batiments[j]);
		}
	}
	printf("\n");
}

void ville_set_etat_sections(ville *v, bool etat)
{
	for (int i = 0; i < v->sections_count; i++)
	{
		section_set_etat(v->sections[i], etat);
	}
}

void ville_update(ville *v)
{
	printf("Updating ville %d... \n", v->id);
	v->consommation = 0;
	for (int i = 0; i < v->sections_count; i++)
	{
		section_update(v->sections[i]);
		v->consommation += section_get_consommation(v->sections[i]);
	}
	printf("\n");
}

void section_of_ville_add_batiment(ville *v, int id_section, batiment *b)
{
	section_add_batiment(v->sections[id_section], b) ? printf("Error adding batiment to section %d of ville %d \n", id_section, v->id) : printf("Batiment added to section %d of ville %d \n", id_section, v->id);
}

void ville_add_batiment(ville *v, batiment *b)
{
	for (int i = 0; i < v->sections_count; i++)
	{
		if (v->sections[i]->batiments_count < MAX_BATIMENTS)
		{
			section_add_batiment(v->sections[i], b);
			return;
		}
	}
	v->sections = realloc(v->sections, sizeof(section *) * (v->sections_count + 1));
	v->sections[v->sections_count] = section_new(v->sections_count);
	section_of_ville_add_batiment(v, v->sections_count, b);
	v->sections_count++;
}

int ville_add_batiment_section(ville *v, batiment *b, int id_section)
{
	return section_add_batiment(v->sections[id_section], b);
}

void ville_set_consommation_random(ville *v)
{
	v->consommation = 0;
	for (int i = 0; i < v->sections_count; i++)
	{
		section_set_consommation_random(v->sections[i]);
		v->consommation += section_get_consommation(v->sections[i]);
	}
}


// Example of use:

// int main(){
// 	srand(time(NULL));
// 	printf("\n");
// 	ville *v = ville_new(0);
// 	for (int i = 0; i < 3; i++)
// 	{
// 		ville_add_section(v, section_new(i)) ? printf("Error adding section %d to ville %d, max batiments reached\n", i, v->id) : printf("Section %d added to ville %d \n", i, v->id);
// 		for (int j = 0; j < 120; j++)
// 		{
// 			section_add_batiment(v->sections[i], batiment_new(j, 0)) ? printf("Error adding batiment %d to section %d, max batiments reached\n", j, i) : printf("Batiment %d added to section %d \n", j, i);
// 		}
// 	}
// 	ville_set_consommation_random(v);
// 	ville_print_sections(v);
// 	ville_print(v);
// 	ville_update(v);
// 	ville_print_sections(v);
// 	ville_print(v);
// }
// Langage : C
// Path: ville.c

#include <stdbool.h>
#include <stdlib.h>
#include "section.c"

typedef struct ville ville;
struct ville
{
	int id;
	double consommation;
	bool etat;
	section **sections;
};


ville *ville_new(int id)
{
	ville *v = malloc(sizeof(ville));
	v->id = id;
	v->consommation = 0;
	v->etat = true;
	v->sections = NULL;
	return v;
}

void ville_free(ville *v)
{
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
	printf("Ville %d : %f %s \r ", v->id, v->consommation, v->etat ? "ON" : "OFF");
}

void ville_add_section(ville *v, section *s)
{
	v->sections = realloc(v->sections, sizeof(section *) * (v->id + 1));
	v->sections[v->id] = s;
	v->id++;
}

void ville_print_sections(ville *v)
{
	for (int i = 0; i < v->id; i++)
	{
		section_print(v->sections[i]);
	}
}

void ville_print_batiments(ville *v)
{
	for (int i = 0; i < v->id; i++)
	{
		section_print_batiments(v->sections[i]);
	}
}

void ville_set_etat_sections(ville *v, bool etat)
{
	for (int i = 0; i < v->id; i++)
	{
		section_set_etat(v->sections[i], etat);
	}
}

void ville_set_etat_batiments(ville *v, bool etat)
{
	for (int i = 0; i < v->id; i++)
	{
		section_set_etat_batiments(v->sections[i], etat);
	}
}

void ville_set_consommation(ville *v)
{
	double consommation = 0;
	for (int i = 0; i < v->id; i++)
	{
		consommation += section_get_consommation(v->sections[i]);
	}
	v->consommation = consommation;
}

void ville_set_consommation_sections(ville *v)
{
	for (int i = 0; i < v->id; i++)
	{
		section_set_consommation(v->sections[i]);
	}
}

void ville_set_consommation_batiments(ville *v)
{
	for (int i = 0; i < v->id; i++)
	{
		section_set_consommation_batiments(v->sections[i]);
	}
}

void ville_add_batiment(ville *v, batiment *b)
{
	v->sections = realloc(v->sections, sizeof(batiment *) * (v->id + 1));
	v->sections[v->id] = b;
	v->id++;
}

void ville_add_batiment_section(ville *v, batiment *b, int id_section)
{
	section_add_batiment(v->sections[id_section], b);
}

void ville_add_section_batiment(ville *v, section *s, int id_batiment)
{
	batiment_add_section(v->sections[id_batiment], s);
}

void ville_add_batiment_section_batiment(ville *v, batiment *b, int id_section, int id_batiment)
{
	batiment_add_section(v->sections[id_batiment], s);
	section_add_batiment(v->sections[id_section], b);
}


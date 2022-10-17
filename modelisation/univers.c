// Langage : C
// Path: ville.c

#include <stdbool.h>
#include <stdlib.h>
#include "ville.c"

typedef struct univers univers;
struct univers
{
    double consommation;
    int nb_villes;
    ville **villes;
};

univers *univers_new(void)
{
    univers *u = malloc(sizeof(univers));
    u->consommation = 0;
    u->nb_villes = 0;
    u->villes = NULL;
    return u;
}

void univers_free(univers *u)
{
    for (int i = 0; i < u->nb_villes; ++i)
    {
        ville_free(u->villes[i]);
    }
    free(u);
}

double univers_get_consommation(univers *u)
{
    return u->consommation;
}

int univers_add_ville(univers *u, ville *v)
{
    u->villes = realloc(u->villes, (u->nb_villes + 1) * sizeof(ville *));
    u->villes[u->nb_villes] = v;
    u->nb_villes++;
    return 0;
}

void univers_update(univers *u)
{
    u->consommation = 0;
    for (int i = 0; i < u->nb_villes; ++i)
    {
        ville_update(u->villes[i]);
        u->consommation += ville_get_consommation(u->villes[i]);
    }
}

void univers_set_consommation_random(univers *u)
{
    for (int i = 0; i < u->nb_villes; ++i)
    {
        ville_set_consommation_random(u->villes[i]);
    }
    univers_update(u);
}

void univers_print_ville(univers *u)
{
    for (int i = 0; i < u->nb_villes; ++i)
    {
        ville_print(u->villes[i]);
    }
}

void univers_print(univers *u)
{
    printf("Univers : %f\n", u->consommation);
}

int main(int argc, char const *argv[])
{
    srand(time(NULL));
	printf("\n");
    univers *u = univers_new();
    for (int i = 0; i < 100; i++)
	{
		univers_add_ville(u, ville_new(i)) ? printf("Error adding ville %d to univers, max ville reached\n", i) : printf("Ville %d added to the univers \n", i);
		for (int j = 0; j < 100; j++)
        {
            ville_add_section(u->villes[i], section_new(j)) ? printf("Error adding section %d to ville %d, max batiments reached\n", j, i) : printf("Section %d added to ville %d \n", j, i);
            for (int k = 0; k < 10; k++)
            {
                section_add_batiment(u->villes[i]->sections[j], batiment_new(k, 0)) ? printf("Error adding batiment %d to section %d, max batiments reached\n", k, j) : printf("Batiment %d added to section %d \n", k, j);
            }
        }
	}
    univers_set_consommation_random(u);
    univers_print_ville(u);
    univers_print(u);
    return 0;
}

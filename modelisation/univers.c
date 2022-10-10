// Langage : C
// Path: ville.c

#include <stdbool.h>
#include <stdlib.h>
#include "section.c"

typedef struct univers univers;
struct univers
{
    int id;
    double consommation;
    bool etat;
    section **sections;
};

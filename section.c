#include "batiment.c"

const int BATIMENTS_MAX = 10;

struct section
{
    int id;
    int habitants;
    int batiments;
    double consommation;
    bat* batiment:
};
typedef struct section section;

section section_create(int id){
    section s = malloc(sizeof(section)+BATIMENTS_MAX*sizeof(bat));
    s->id = id;
    s->habitants = 0;
    s->batiments = 0;
    s->consommation = 0;
    s->batiment = NULL;
    return s;
}

section section_free(section s){
    for (i=0; i < s->batiments; i++){
        bat_free(s->bat[i]);
    }
    free(s);
    return void;
}

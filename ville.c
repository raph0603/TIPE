#include "section.c"

const int SECTIONS_MAX = 10;

struct ville
{
    int id;
    int habitants;
    int batiments;
    int sections;
    double consommation;
    section* section;
};
typedef struct section section;

ville ville_create(int id){
    ville v = malloc(sizeof(ville)+SECTIONS_MAX*sizeof(section)+SECTIONS_MAX*BATIMENTS_MAX*sizeof(batiment));
    v->id = id;
    v->habitants = 0;
    v->batiments = 0;
    v->sections = 0;
    v->consommation = 0;
    v->section = NULL;
    return v;
}

void ville_free(ville v){
    for(i = 0; i < v->sections; i++){
        section_free(v->section[i]);
    }
    free(v);
    return void;
}
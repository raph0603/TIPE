#include "ville.c"
#include "section.c"
#include "batiment.c"


bat batiment_set(bat b, int habitants, double consommation){
    b->habitants = habitants;
    b->consommation = consommation;
    return b
}

section section_refresh(section s){
    s->habitants = 0;
    s->consommation = 0.0;
    for (i = 0; i < s->batiments, i++){
        s->habitants += s->batiment[i]->habitants;
        s->consommation += s->batiment[i]->consommation;
    }
    return s;
}


#include "univers.c"
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

bool section_add_bat(section* s, bat b){
    if (s->batiments == BATIMENTs_MAX) {
        return false;
    }
    else {
        s->batiment[s->batiments] = b;
        s->batiments += 1;
        return true;
    }
}

bool ville_add_section(ville* v, section s){
      if (s->sections == SECTIONS_MAX) {
        return false;
    }
    else {
        s->section[s->section] = b;
        s->sections += 1;
        return true;
    }
}


bool ville_add_batiments(ville* v, bat b){
    if !(section_add_bat(v->section[sections-1], b)){
        section s = section_create(v->sections);
        v->sections++;
        
    }
}


struct batiment
{
	int id;
	int habitants;
	double consommation;
};
typedef struct batiment bat;

bat bat_create(int id){
	bat b = malloc(sizeof(bat));
	b->id = id;
	b->habitants = 0;
	b->consommation = 0;
	return b; 
}

void bat_free(bat b){
	free(b);
	return void;
}


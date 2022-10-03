

struct batiment
{
	int id;
	int habitants;
	double puissance;
};
typedef struct batiment bat;

bat bat_create(int id, double puissance, int habitants){
	bat b = malloc(sizeof(bat));
	b->id = id;
	b->habitants = habitants;
	b->puissance = puissance;
	return b; 
}

void bat_free(bat b){
	free(b);
	return void;
}


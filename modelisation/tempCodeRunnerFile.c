int main(int argc, char const *argv[])
{
	srand(time(NULL));
	printf("\n");
	section *s = section_new(0);
	for (int i = 0; i < 120; i++)
	{
		section_add_batiment(s, batiment_new(i, 0)) ? printf("Error adding batiment %d to section %d, max batiments reached\n", i, s->id) : printf("Batiment %d added to section %d \n", i, s->id);
	}
	section_set_consommation_random(s);
	section_print_batiments(s);
	section_print(s);
	section_update(s);
	section_print(s);
}
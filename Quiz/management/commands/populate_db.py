import csv
import requests
from django.core.management.base import BaseCommand
from Quiz.models import Plant, Picture


class Command(BaseCommand):
    help = """
    This command will populate the database of plant and picture objects 
    from the data present in the staticfiles\Plant_database.csv file
    by fetching the data present in the Trefle API.
    The app only collect the pictures of plant leaf and flower.
    """

    def _create_plants(self):
        Plant.objects.all().delete()
        Picture.objects.all().delete()

        TREFLE_API_KEY = 'your key here'

        with open('staticfiles\Plant_database.csv') as csvFile:
            reader = csv.reader(csvFile)

            for i, row in enumerate(reader):
                
                if i == 0:
                    pass
                
                else:
                    row = "".join(row)
                    row = row.replace(";", " ")
                    row = row.split()

                    slug = f'{row[0].lower()}-{row[1].lower()}'

                    plant_Trefle_API = requests.get(f'https://trefle.io/api/v1/species/{slug}?token={TREFLE_API_KEY}').json()
                    
                    if plant_Trefle_API.get('error'):
                        print(slug, 'pas dans la bdd de trèfle')
                        Plant.objects.create(
                            genus_name = row[0].lower(),
                            specie_name= row[1].lower(),
                            orchard = row[3],
                            maize = row[4],
                            rice = row[5],
                            rubber = row[6],	
                            teak = row[7],	
                            bambou = row[8],	
                            fallow = row[9],	
                            community_forest = row[10],	
                            secondary_forest = row[11],
                        )

                    else:
                        created_plant = Plant.objects.create(
                            family_name = plant_Trefle_API.get('data').get('family').lower(),
                            genus_name = row[0].lower(),
                            specie_name= row[1].lower(),
                            orchard = row[3],
                            maize = row[4],
                            rice = row[5],
                            rubber = row[6],	
                            teak = row[7],	
                            bambou = row[8],	
                            fallow = row[9],	
                            community_forest = row[10],	
                            secondary_forest = row[11],
                        )

                        print('created_plant', created_plant)

                        if plant_Trefle_API.get('data').get('images').get('flower'):
                            for flower_picture in plant_Trefle_API.get('data').get('images').get('flower'):
                                print('new flower picture', flower_picture)

                                Picture.objects.create(
                                    url = flower_picture.get('image_url'),
                                    copyright = flower_picture.get('copyright'),
                                    plant = created_plant,
                                )

                        if plant_Trefle_API.get('data').get('images').get('leaf'):
                            for leaf_picture in plant_Trefle_API.get('data').get('images').get('leaf'):
                                print('new leaf picture', leaf_picture)

                                Picture.objects.create(
                                    url = leaf_picture.get('image_url'),
                                    copyright = leaf_picture.get('copyright'),
                                    plant = created_plant,
                                )        

    def handle(self, *args, **options):
        self._create_plants()





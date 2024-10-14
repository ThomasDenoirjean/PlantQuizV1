from Quiz.models import Plant, Picture
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """
    Display the different items or data missing in the database:
    - Family names: the plant is in the database but has no family name*
    - Pictures instances: there are no pictures associated to a plant instance**
    - Missing .png: the image of some Pictures instances have not been downloaded

    *This is because the plant was not on the Trefle database. You have to add it manually.
    **This is because either the plant had no pictures linked to it in the Trefle database 
    or the plant was not on the Trefle database and was manually created. You have to create
    it manually.
    """

    def _missing_items(self):
            plants_family_unknown = Plant.objects.filter(family_name__exact='')
            print("Plante dont la famille n'est pas renseignée", plants_family_unknown.count())

            pictures = Picture.objects.all()
            plant_ID_with_pictures_url =  []
            for picture in pictures:
                if picture.plant.id not in plant_ID_with_pictures_url:
                     plant_ID_with_pictures_url.append(picture.plant.id)
            plants_without_pictures = Plant.objects.exclude(id__in=plant_ID_with_pictures_url)
            message = "n'ont pas d'url d'image renseignée. Voici les premières plantes qu'il faut mettre à jour : "
            print(len(plants_without_pictures), message, plants_without_pictures)

            pictures_without_image_downloaded = Picture.objects.filter(picture__exact='')
            print(len(pictures_without_image_downloaded), " images n'ont pas encore été téléchargée sur un total de ", Picture.objects.all().count())
            
            
    def handle(self, *args, **options):
        self._missing_items()


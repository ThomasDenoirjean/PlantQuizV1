import os
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from PIL import Image
from io import BytesIO
from Quiz.models import Picture
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = """
    Download the flower or leaf picture from the url property of each picture instance.
    Saves it as a .png file.
    """

    def _download_images(self):
        pictures = Picture.objects.all()

        for picture in pictures:
            if picture.url and not picture.picture :
                print("L'image dont l'id est ", picture.id, " a une URL renseignée mais la photo n'est pas incluse dans la BDD")
                try:
                    img_temp = NamedTemporaryFile(delete=True, suffix=".png")

                    response = urlopen(picture.url)
                    total_size = int(response.info().get('Content-Length').strip())
                    print("Taille de l'image : ", total_size)
                    bytes_so_far = 0
                    chunk_size = 1024

                    img_bytes = BytesIO()
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        img_bytes.write(chunk)
                        bytes_so_far += len(chunk)
                        percentage = (bytes_so_far / total_size) * 100
                        print(f"Download progress: {percentage:.2f}%")

                    img_bytes.seek(0)
                    img = Image.open(img_bytes)
                    img = img.convert("RGBA")
                    img.save(img_temp, format="PNG")
                    img_temp.flush()

                    picture.picture.save(os.path.basename(picture.url).rsplit('.', 1)[0] + '.png', File(img_temp))
                    picture.save()
                    print("La photo de l'image dont l'id est ", picture.id, " a été enregistrée")
                except Exception as e:
                    print(f"ERREUR : la photo de l'image dont l'id est {picture.id} n'a pas été enregistrée. Error: {e}")
            else:
                print("La photo de l'image dont l'id est ", picture.id, " a déjà été téléchargée")

    def handle(self, *args, **options):
        self._download_images()
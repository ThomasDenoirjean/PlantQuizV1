from django.db import models

# Create your models here.
class Plant(models.Model):
    family_name = models.CharField(max_length=100, blank=True)
    genus_name = models.CharField(max_length=100)
    specie_name = models.CharField(max_length=100)
    orchard = models.IntegerField()
    maize = models.IntegerField()
    rice = models.IntegerField()	
    rubber = models.IntegerField()
    teak = models.IntegerField()	
    bambou = models.IntegerField()	
    fallow = models.IntegerField()	
    community_forest = models.IntegerField()	
    secondary_forest = models.IntegerField()
    number_of_guess = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.genus_name} {self.specie_name} - {self.family_name}"


class Picture(models.Model):
    url = models.CharField(max_length=100)
    copyright = models.CharField(max_length=100)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='pictures')
    picture = models.ImageField(upload_to='plant_pictures/', blank=True)

    def __str__(self):
        return f"Photo de {self.plant.genus_name} {self.plant.specie_name}"

from rest_framework.serializers import ModelSerializer
from Quiz.models import Plant, Picture


class PictureSerializer(ModelSerializer):
 
    class Meta:
        model = Picture
        fields = ['id', 'url', 'plant', 'picture']


class PlantSerializer(ModelSerializer):
    pictures = PictureSerializer(many=True)
 
    class Meta:
        model = Plant
        fields = ['id', 'family_name', 'genus_name', 'specie_name', 'number_of_guess', 'pictures']
        
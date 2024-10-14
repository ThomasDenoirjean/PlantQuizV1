import random
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Quiz.models import Plant, Picture
from Quiz.serializers import PlantSerializer, PictureSerializer


# Create your views here.
def quiz(request):
    return render(request, 'Quiz/quiz.html')


#######################
# section lié à l'API #
#######################
class PlantToGuessAPI(APIView):
    def get(self, request):
        habitats = json.loads(request.GET.get('habitats'))

        plants = Plant.objects.all()

        if habitats:
            for habitat in habitats:
                plants = plants.filter(**{habitat: 1})

        selected_plant = None
        while selected_plant == None:
            tested_plant = random.choice(plants)
            if Plant.objects.get(id=tested_plant.id).pictures.all().exists():
                selected_plant = tested_plant   
        serialized = PlantSerializer(selected_plant)
        return Response(serialized.data)
    

class TenPlantsToGuess(APIView):
    def get(self, request):
        habitats = json.loads(request.GET.get('habitats'))
        plants = Plant.objects.all()

        if habitats:
            for habitat in habitats:
                plants = plants.filter(**{habitat: 1})

        possible_ids = list(plants.values_list('id', flat=True))
        possible_ids = random.choices(possible_ids, k=10)
        serialized = PlantSerializer(plants.filter(pk__in=possible_ids), many=True)
        return Response(serialized.data)


class GetMisleadingPlants(APIView):
    def get(self, request):
        plant_id = int(request.GET.get('id'))
        NUMBER_OF_MISLEADING_HINTS = int(request.GET.get('NUMBER_OF_MISLEADING_HINTS'))
        plants = Plant.objects.exclude(id=plant_id)
        misleading_plants = []
        for i in range(NUMBER_OF_MISLEADING_HINTS):
            selected_plant = random.choice(plants)
            plants = plants.exclude(id=selected_plant.id)
            misleading_plants.append(selected_plant)
        serialized = PlantSerializer(misleading_plants, many=True)
        return Response(serialized.data)    


class GetMisleadingPictures(APIView):
    def get(self, request):
        plant_id = int(request.GET.get('id'))
        NUMBER_OF_MISLEADING_HINTS = int(request.GET.get('NUMBER_OF_MISLEADING_HINTS'))
        pictures = Picture.objects.exclude(plant__id=plant_id)
        misleading_pictures = []
        for i in range(NUMBER_OF_MISLEADING_HINTS):
            selected_picture = random.choice(pictures)
            misleading_pictures.append(selected_picture)
            pictures = pictures.exclude(id=selected_picture.id)  
        serialized = PictureSerializer(misleading_pictures, many=True)
        return Response(serialized.data)  

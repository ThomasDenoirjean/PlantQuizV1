from Quiz.models import Plant
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """
    Reset the guess count of each plant object. 
    This property is usefull to track which plants are harder to identify.
    """

    def _reset_count(self):
        plants = Plant.objects.all()

        for plant in plants:
            if plant.number_of_guess != 0:
                print(plant, ', number of guess: ', plant.number_of_guess)
                plant.number_of_guess = 0
            
    def handle(self, *args, **options):
        self._reset_count()

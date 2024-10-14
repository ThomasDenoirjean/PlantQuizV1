from django.contrib import admin
from Quiz.models import Plant, Picture


class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'family_name', 'genus_name', 'specie_name')


class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'plant', 'url', 'picture')


# Register your models here.
admin.site.register(Plant, PlantAdmin)
admin.site.register(Picture, PictureAdmin)

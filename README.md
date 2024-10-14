# 🌷 PlantQuiz

This repo is the first version of a web app that is designed to test your botanical knowledge thanks to quiz with various mode and difficulty level.

# 1- Basics
## Which plant information ?
In my example, I have defined a set of habitats in which the plant I want to train on could be find.
The pictures that the app will fetch from the Trefle API will be only leaves and flowers pictures.

## Quiz mode
There are three quiz modes:
  - infinite: endless mode, will fetch a new plant each time you correctly identified one
  - ten plants: will select 10 plants from the database ; will end the game when you identified the 10th plant
  - timer: you have 60 seconds to identify as many plants as you can

## Quiz difficulty
Each difficulty can be run with each mode. There are 5 difficulties level:
  - easy: the hints are the plant pictures and you have to select the correct plant name among four propositions
  - medium: the hints are the plant pictures and you have to type the family, genus and specie names of the plant
  - inverse: the hint is the plant name and you have to select the correct plant picture among four propositions
  - freestyle: select a random difficulty for each plant
  - sudden death: same as freestyle for the quiz configuration, but at the first error the game ends

## Habitats filter
You can select one or multiple habitats, and only plants that can be found in these habitats will be proposed in the quiz.


# 2- Set up the app
## Data structure
Create a .csv with the first two column being 'Species name' (genus + specie name) and 'family', plus as many habitats as you want (you will have to modify the populate_db.py command accordingly). You don't have to complete the 'family' row, as we will get the family name directly from the Trefle API.


## Collect plant information
From the .csv file listing all the species you want to train on, run commands to:
  - populate_db: extract Plant information and pictures from the Trefle API
  - download_images: download plant pictures from their url*
  - check_missing_items_db: check which plant where on the .csv file but not on the Trefle database**
  - reset_guess_count: the app tracks the number of correct guesses of each plant, considered as a metric for evaluating the degree of accuracy in identifying different plants

*Some plants may not have pictures linked in the Trefle database. Through Django admin interface, you can create the picture objects yourself. Don't forget to add the url link so the picture could be downloaded thanks to the command.
**In this case, you will have to add these species and their pictures directly through Django admin interface.

Don't forget to create a superuser to use the Django admin interface.


## What's next ?
A second version of the web app is in development. It will rely entirely on the Trefle database, to get access to around 400 000 species worldwide. While quiz modes and difficulties are not intended to change, the habitats filter will be replaced by a family and a distribution filters.
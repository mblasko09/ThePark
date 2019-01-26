from django.db import models
from enum import Enum

class Species(Enum):
    dog = 1
    cat = 2
    rabbit = 3
    octopus = 4
    fish = 5
    turtle = 6
    hamster = 7
    chinchilla = 8
    lizard = 9
    snake = 10

class Animal(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    species = models.Species()
    bio = models.TextField()
    pictures = models.ArrayField(models.ImageField())

class Account(models.Model):
    my_pet = Animal()
    matches = models.ArrayField(Animal())

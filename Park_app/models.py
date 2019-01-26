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
    species = Species
    bio = models.TextField()
    pictures = models.ImageField()

class Account(models.Model):
    my_pet = Animal()
    preference = Species
    #matches = models.ArrayField(Animal())

class User(models.Model):
    my_account = Account()
    username = models.TextField()
    password = models.TextField()

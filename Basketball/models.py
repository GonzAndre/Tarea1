from __future__ import unicode_literals

from django.db import models

class Team(models.Model): #herencia de models
    name = models.CharField(max_length=200) #maximo del string
    description = models.TextField()
    photo = models.ImageField()
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    birthdate = models.DateField()
    age = models.IntegerField(default = 0)
    rut = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    weight = models.IntegerField(default = 0)
    photo = models.ImageField()
    position = models.CharField(
            max_length=2,
            choices=(
                    ('BA', 'Base'),
                    ('ES', 'Escolta'),
                    ('AL', 'Alero'),
                    ('AP', 'AlaPivot'),
                    ('PI', 'Pivot'),
                    ),
            default='BA'
            )

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    age = models.IntegerField(default = 0)
    rut = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)

class Partido(models.Model):
    name = models.CharField(max_length=200)

from django.db import models

# Create your models here.

from django.db import models


class Car(models.Model):

    brand = models.CharField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name="name",
        max_length=250,
        blank=True
    )
    make = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    year = models.IntegerField(blank=True)


class Car2(models.Model):

    brand = models.CharField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name="name",
        max_length=250,
        blank=True
    )
    make = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    year = models.IntegerField(blank=True)


class Candy(models.Model):

    name = models.CharField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name="name",
        max_length=250,
        blank=True
    )
    flavor = models.CharField(max_length=50)
    size = models.CharField(max_length=30)
    year_created = models.IntegerField(blank=True)

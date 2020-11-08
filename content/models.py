from django.db import models
from django.contrib.auth import get_user_model


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50)


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50)

class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField("year published", auto_now_add=True)
    rating = models.PositiveSmallIntegerField
    description = models.TextField(blank=True, null=True)
    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, blank=True, null=True, related_name="titles")
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True, null=True, related_name="titles")


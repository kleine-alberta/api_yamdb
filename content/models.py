from django.db import models


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50, blank=True, null=True)


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50, blank=True, null=True)

class Titles(models.Model):
    name = models.CharField(max_length=200, blank=True)
    year = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genres, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True, null=True, related_name="category")

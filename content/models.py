import datetime
from django.db import models
from django.core.validators import MaxValueValidator


class Genres(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name="genres")
    slug = models.SlugField(unique=True,
                            max_length=50,
                            blank=True,
                            null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Categories(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name="categories")
    slug = models.SlugField(unique=True,
                            max_length=50,
                            blank=True,
                            null=True)

    def __str__(self):
        return self.name

        class Meta:
            verbose_name = 'Category'
            verbose_name_plural = 'Categories'


class Titles(models.Model):
    def current_year():
        return datetime.date.today().year

    name = models.CharField(max_length=200,
                            blank=True,
                            verbose_name="titles")
    year = models.IntegerField(validators=[MaxValueValidator(current_year())],
                               null=True,
                               db_index=True)
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genres, blank=True)
    category = models.ForeignKey(Categories,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 related_name='titles')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

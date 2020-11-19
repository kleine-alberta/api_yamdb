# Generated by Django 3.0.5 on 2020-11-19 13:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titles',
            name='rating',
        ),
        migrations.AlterField(
            model_name='titles',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='content.Categories'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2020)]),
        ),
    ]
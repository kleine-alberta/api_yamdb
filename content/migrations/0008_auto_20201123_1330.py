# Generated by Django 3.0.5 on 2020-11-23 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20201119_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]

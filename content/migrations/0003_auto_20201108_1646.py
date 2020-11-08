# Generated by Django 3.0.5 on 2020-11-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20201108_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titles',
            name='rating',
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(unique='name'),
        ),
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='genres',
            name='slug',
            field=models.SlugField(unique='name'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.DateField(auto_now_add=True, verbose_name='year published'),
        ),
    ]

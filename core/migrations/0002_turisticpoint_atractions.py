# Generated by Django 3.1.5 on 2021-01-28 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atractions', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turisticpoint',
            name='atractions',
            field=models.ManyToManyField(to='atractions.Atraction'),
        ),
    ]

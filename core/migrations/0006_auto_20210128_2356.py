# Generated by Django 3.1.5 on 2021-01-28 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('core', '0005_turisticpoint_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turisticpoint',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
        ),
    ]

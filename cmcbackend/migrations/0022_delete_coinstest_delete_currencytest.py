# Generated by Django 4.2.3 on 2023-07-20 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmcbackend', '0021_currencytest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coinstest',
        ),
        migrations.DeleteModel(
            name='Currencytest',
        ),
    ]

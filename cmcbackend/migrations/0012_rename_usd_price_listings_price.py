# Generated by Django 4.2.3 on 2023-07-13 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmcbackend', '0011_listings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='usd_price',
            new_name='price',
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-18 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmcbackend', '0018_alter_currency_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
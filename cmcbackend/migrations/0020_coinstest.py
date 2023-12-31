# Generated by Django 4.2.3 on 2023-07-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmcbackend', '0019_currency_last_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coinstest',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('last_updated', models.DateTimeField()),
                ('date_added', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=20, max_digits=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]

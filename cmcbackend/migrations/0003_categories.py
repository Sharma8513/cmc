# Generated by Django 4.2.3 on 2023-07-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmcbackend', '0002_rename_crytos_cryptos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('num_tokens', models.IntegerField()),
                ('avg_price_change', models.FloatField()),
                ('market_cap', models.DecimalField(decimal_places=6, max_digits=20)),
                ('market_cap_change', models.FloatField()),
                ('volume', models.DecimalField(decimal_places=6, max_digits=20)),
                ('volume_change', models.FloatField()),
                ('last_updated', models.DateTimeField()),
                ('timestamp', models.DateTimeField()),
                ('error_code', models.IntegerField()),
                ('error_message', models.TextField()),
                ('elapsed', models.IntegerField()),
                ('credit_count', models.IntegerField()),
            ],
        ),
    ]

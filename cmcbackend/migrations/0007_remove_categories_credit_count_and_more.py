# Generated by Django 4.2.3 on 2023-07-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmcbackend', '0006_delete_cryptocurrency_alter_categories_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='credit_count',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='elapsed',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='error_code',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='error_message',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='categories',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]

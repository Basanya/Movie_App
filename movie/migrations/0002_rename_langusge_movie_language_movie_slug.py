# Generated by Django 4.1.7 on 2023-02-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='langusge',
            new_name='language',
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]

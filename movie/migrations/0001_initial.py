# Generated by Django 4.1.7 on 2023-02-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descripton', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='movies')),
                ('category', models.CharField(choices=[('A', 'ACTION'), ('B', 'DRAMA'), ('C', 'COMEDY'), ('D', 'ROMANCE')], max_length=1)),
                ('langusge', models.CharField(choices=[('EN', 'ENGLISH'), ('YR', 'YORUBA')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'RECENTLY ADDED'), ('MA', 'MOST ADDED'), ('TR', 'TOP RATED')], max_length=2)),
                ('year_of_production', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
    ]
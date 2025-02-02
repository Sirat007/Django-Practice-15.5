# Generated by Django 5.1.4 on 2024-12-16 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='albumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.TextField()),
                ('release_date', models.DateField()),
                ('ratings', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musicianmodel')),
            ],
        ),
    ]

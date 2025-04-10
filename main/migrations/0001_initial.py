# Generated by Django 5.2 on 2025-04-03 22:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='clubs')),
                ('president', models.CharField(blank=True, max_length=255, null=True)),
                ('coach', models.CharField(blank=True, max_length=255, null=True)),
                ('found_date', models.DateField(blank=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField()),
                ('position', models.CharField(max_length=255)),
                ('number', models.PositiveSmallIntegerField()),
                ('price', models.FloatField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.club')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('price_tft', models.FloatField()),
                ('date', models.DateField()),
                ('club_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_from', to='main.club')),
                ('club_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_to', to='main.club')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.season')),
            ],
        ),
    ]

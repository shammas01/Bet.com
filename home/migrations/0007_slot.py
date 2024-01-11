# Generated by Django 5.0.1 on 2024-01-11 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_betmodel_max_enroll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.PositiveIntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.betmodel')),
            ],
        ),
    ]

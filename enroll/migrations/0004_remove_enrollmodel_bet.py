# Generated by Django 5.0.1 on 2024-01-11 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_betslotmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollmodel',
            name='bet',
        ),
    ]

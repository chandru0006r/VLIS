# Generated by Django 4.1.5 on 2023-10-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_landinformations_land_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landinformations',
            name='land_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True),
        ),
    ]

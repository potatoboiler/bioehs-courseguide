# Generated by Django 2.1.5 on 2021-01-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industrial', '0017_auto_20200112_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.PositiveSmallIntegerField(default=2021),
        ),
    ]

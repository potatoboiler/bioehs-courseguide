# Generated by Django 2.1.5 on 2022-01-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industrial', '0018_auto_20210107_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.PositiveSmallIntegerField(default=2022),
        ),
    ]
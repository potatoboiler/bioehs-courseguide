# Generated by Django 2.1.4 on 2019-01-14 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industrial', '0014_auto_20190113_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='year',
            field=models.ManyToManyField(related_name='sponsors', to='industrial.Year'),
        ),
    ]

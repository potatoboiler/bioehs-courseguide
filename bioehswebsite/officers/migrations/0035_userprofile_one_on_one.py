# Generated by Django 2.1.5 on 2019-09-21 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0034_auto_20190920_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='one_on_one',
            field=models.BooleanField(blank=True, default=False, verbose_name='One on one Meeting'),
        ),
    ]
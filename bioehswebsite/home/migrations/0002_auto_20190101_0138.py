# Generated by Django 2.0 on 2019-01-01 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BioEHSLinks',
            new_name='LinkDatabase',
        ),
    ]
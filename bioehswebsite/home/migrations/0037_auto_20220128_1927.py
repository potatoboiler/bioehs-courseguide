# Generated by Django 2.1.5 on 2022-01-29 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20220128_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semesterspecificinfo',
            old_name='bioehsc_HS_flyer',
            new_name='bioehsc_hs_flyer',
        ),
    ]

# Generated by Django 2.1.5 on 2020-03-04 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20200303_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semesterspecificinfo',
            name='video_and_project_abstract_form',
        ),
    ]

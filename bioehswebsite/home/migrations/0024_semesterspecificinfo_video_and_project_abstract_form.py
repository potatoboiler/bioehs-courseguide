# Generated by Django 2.1.5 on 2020-03-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_semesterspecificinfo_bioehsc_ugrad_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='semesterspecificinfo',
            name='video_and_project_abstract_form',
            field=models.URLField(default='bit.ly/2020BioEHSCVideo', help_text='TO BE UPDATED EACH SPRING', verbose_name='Video and Project Abstract Form'),
        ),
    ]

# Generated by Django 2.1.5 on 2020-03-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_semesterspecificinfo_video_and_project_abstract_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semesterspecificinfo',
            name='video_and_project_abstract_form',
            field=models.URLField(default='https://docs.google.com/forms/d/e/1FAIpQLSdAM56DoBrKSbvDtuuuB3tQz7VMWscd0iP-Ut-hBHtzU8RdJg/viewform?pli=1', help_text='TO BE UPDATED EACH SPRING', verbose_name='Video and Project Abstract Form'),
        ),
    ]

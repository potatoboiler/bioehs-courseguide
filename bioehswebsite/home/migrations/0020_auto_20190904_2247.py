# Generated by Django 2.1.5 on 2019-09-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_semesterspecificinfo_bioe_decal_flyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semesterspecificinfo',
            name='bioe_decal_flyer',
            field=models.FileField(default='decal.pdf', help_text='TO BE UPDATED EACH FALL', upload_to='', verbose_name='Decal Flyer'),
        ),
    ]

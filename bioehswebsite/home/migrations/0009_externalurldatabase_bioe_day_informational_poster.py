# Generated by Django 2.0 on 2019-01-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_externalurldatabase_bioe_day_rsvp_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalurldatabase',
            name='bioe_day_informational_poster',
            field=models.ImageField(default='images/committees/outreach/bioe_day_flyer.jpg', upload_to='', verbose_name='BioE Day Informational Poster'),
        ),
    ]

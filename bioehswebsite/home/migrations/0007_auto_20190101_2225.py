# Generated by Django 2.0 on 2019-01-01 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190101_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalurldatabase',
            name='bioehsc_online_application',
            field=models.URLField(default='https://fs26.formsite.com/BioEHSC/form3/index.html?1514880069958', help_text='TO BE UPDATED EACH SPRING', verbose_name='BioEHSC Application'),
        ),
    ]
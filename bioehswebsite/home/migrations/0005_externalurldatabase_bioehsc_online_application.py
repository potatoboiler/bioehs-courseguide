# Generated by Django 2.0 on 2019-01-01 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190101_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalurldatabase',
            name='bioehsc_online_application',
            field=models.URLField(default='https://fs26.formsite.com/BioEHSC/form3/index.html?1514880069958', verbose_name='BioEHSC Application'),
        ),
    ]

# Generated by Django 2.1.5 on 2022-04-07 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0047_userprofile_alumnus_last_contacted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='alumnus_last_contacted',
            field=models.TextField(blank=True, help_text='Last contacted date, need to manually', verbose_name='Last Contacted Date'),
        ),
    ]

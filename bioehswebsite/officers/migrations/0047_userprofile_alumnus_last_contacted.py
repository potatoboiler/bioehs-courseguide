# Generated by Django 2.1.5 on 2022-04-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0046_auto_20220115_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='alumnus_last_contacted',
            field=models.TextField(blank=True, help_text='Last contacted date, need to manually update', verbose_name='Last Contacted Date'),
        ),
    ]

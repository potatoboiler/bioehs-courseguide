# Generated by Django 2.1.5 on 2022-11-30 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0053_userprofile_buddy_hangouts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='buddy_hangouts',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='family_competition',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='resume_workshop',
        ),
    ]
# Generated by Django 2.1.5 on 2020-02-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0037_auto_20200212_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='family_dinner',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='one_on_one',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='family_competition',
            field=models.BooleanField(blank=True, default=False, verbose_name='Family Competition'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='family_hangout',
            field=models.BooleanField(blank=True, default=False, verbose_name='Family Hangout'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='officer_challenges',
            field=models.BooleanField(blank=True, default=False, verbose_name='Officer Challenges'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='waiver_submission',
            field=models.BooleanField(blank=True, default=False, verbose_name='Waiver Submission'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin_workshop',
            field=models.BooleanField(blank=True, default=False, verbose_name='LinkedIn Workshop'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resume_submission',
            field=models.BooleanField(blank=True, default=False, verbose_name='Revised Résumé Submission'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_event_2',
            field=models.BooleanField(blank=True, default=False, verbose_name='Social Event 2'),
        ),

    ]
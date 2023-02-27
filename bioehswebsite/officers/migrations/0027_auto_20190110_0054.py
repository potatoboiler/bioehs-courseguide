# Generated by Django 2.1.4 on 2019-01-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0026_auto_20190105_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='academic_event',
            field=models.BooleanField(blank=True, default=False, verbose_name='Academic Event'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='banquet',
            field=models.BooleanField(blank=True, default=False, verbose_name='End of the Year Banquet'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='candidate_challenge',
            field=models.BooleanField(blank=True, default=False, verbose_name='Candidate Challenge Night'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dues_1',
            field=models.BooleanField(blank=True, default=False, verbose_name='Membership Dues Part 1'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dues_2',
            field=models.BooleanField(blank=True, default=False, verbose_name='Membership Dues Part 2'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='family_dinner',
            field=models.BooleanField(blank=True, default=False, verbose_name='Family Dinner'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gm_1',
            field=models.BooleanField(blank=True, default=False, verbose_name='General Meeting 1'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gm_2',
            field=models.BooleanField(blank=True, default=False, verbose_name='General Meeting 2'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gm_3',
            field=models.BooleanField(blank=True, default=False, verbose_name='General Meeting 3'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='outreach_event',
            field=models.BooleanField(blank=True, default=False, verbose_name='Outreach Event'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photoshoot',
            field=models.BooleanField(blank=True, default=False, verbose_name='Photoshoot'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='prodev_event',
            field=models.BooleanField(blank=True, default=False, verbose_name='Professional Development Event'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resume_linkedin',
            field=models.BooleanField(blank=True, default=False, verbose_name='Résumé and LinkedIn Workshop'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='retreat',
            field=models.BooleanField(blank=True, default=False, verbose_name='Candidate Retreat'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_event_1',
            field=models.BooleanField(blank=True, default=False, verbose_name='Social Event 1'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_event_2',
            field=models.BooleanField(blank=True, default=False, verbose_name='Social Event 2 with your large family'),
        ),
    ]

# Generated by Django 2.0 on 2018-12-31 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0018_userprofile_dues_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dues_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='officers.CandidateRequirement'),
        ),
    ]

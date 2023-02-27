# Generated by Django 2.0 on 2018-12-31 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0016_auto_20181229_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('date', models.DateField(blank=True, verbose_name='Date Completed')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
            ],
        ),
    ]

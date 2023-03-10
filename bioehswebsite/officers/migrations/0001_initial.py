# Generated by Django 2.1.4 on 2018-12-20 21:12

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            managers=[
                ('officers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('SP', 'Spring'), ('FA', 'Fall')], max_length=5)),
                ('year', models.PositiveSmallIntegerField()),
            ],
            managers=[
                ('semesters', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='officer',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officers', to='officers.Semester'),
        ),
    ]

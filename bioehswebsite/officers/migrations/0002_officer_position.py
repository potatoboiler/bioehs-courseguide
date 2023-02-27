# Generated by Django 2.1.4 on 2018-12-20 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='position',
            field=models.CharField(choices=[('Executive Officers', (('PRES', 'President'), ('EVP', 'External Vice President'), ('IVP', 'Internal Vice President'), ('TREAS', 'Treasurer'), ('SEC', 'Secretary'), ('BIOEHSC', 'BioEHSC External Relations Chair'))), ('Non-Executive Officers', (('PRODEV', 'Professional Development Chair'), ('PUBL', 'Publicity Chair'), ('ACA', 'Academic Chair'), ('HIST', 'Historian'), ('SOC', 'Social Chair'), ('WEBMAS', 'Webmaster'), ('PROJ', 'Projects Chair'), ('BIOEHSCSENIOR', 'BioEHSC Senior Chair'), ('OUTR', 'Outreach Chair'))), ('Assistant Officers', (('ASSISACA', 'Academic Assistant Officer'), ('ASSISOUTR', 'Outreach Assistant Officer'), ('ASSISPRODEV', 'Professional Development Assistant Officer'), ('ASSISPROJ', 'Projects Assistant Officer'))), ('Advisors', (('SRADV', 'Senior Advisor'), ('FACADV', 'Faculty Advisor')))], default=None, max_length=50),
            preserve_default=False,
        ),
    ]

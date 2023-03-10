# Generated by Django 2.1.5 on 2020-02-13 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0035_userprofile_one_on_one'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(choices=[('Executive Officers', (('PRES', 'President'), ('EVP', 'External Vice President'), ('IVP', 'Internal Vice President'), ('TREAS', 'Treasurer'), ('SEC', 'Secretary'), ('BIOEHSCSENIOR', 'BioEHSC™ Senior Chair'), ('BIOEHSCEXT', 'BioEHSC™ External Relations Chair'))), ('Non-Executive Officers', (('PRODEV', 'Professional Development Chair'), ('PUBL', 'Publicity Chair'), ('ACA', 'Academic Chair'), ('HIST', 'Historian'), ('SOC', 'Social Chair'), ('WEBMAS', 'Webmaster'), ('PROJ', 'Projects Chair'), ('BIOEHSCJUNIOR', 'BioEHSC™ Junior Chair'), ('COMMSERVE', 'Community Service Chair'), ('OUTR', 'Outreach Chair'))), ('Assistant Officers', (('ASSISACA', 'Academic Assistant Officer'), ('ASSISOUTR', 'Outreach Assistant Officer'), ('ASSISPRODEV', 'Professional Development Assistant Officer'), ('ASSISPROJ', 'Projects Assistant Officer'), ('ASSISIVP', 'Internal Vice President Assistant Officer'), ('ASSISTRE', 'Treasurer Assitant Officer'))), ('Advisors', (('SRADV', 'Senior Advisor'), ('FACADV', 'Faculty Advisor')))], max_length=50),
        ),
    ]

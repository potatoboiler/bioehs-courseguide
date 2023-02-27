# Generated by Django 2.1.5 on 2022-01-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0045_auto_20210430_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(choices=[('Executive Officers', (('PRES', 'President'), ('EVP', 'External Vice President'), ('IVP', 'Internal Vice President'), ('TREAS', 'Treasurer'), ('SEC', 'Secretary'), ('BIOEHSCSENIOR', 'BioEHSC™ Senior Chair'), ('BIOEHSCEXT', 'BioEHSC™ External Relations Chair'))), ('Non-Executive Officers', (('PRODEV', 'Professional Development Chair'), ('PUBL', 'Publicity Chair'), ('ACA', 'Academic Chair'), ('HIST', 'Historian'), ('SOC', 'Social Chair'), ('WEBMAS', 'Webmaster'), ('PROJ', 'Projects Chair'), ('BIOEHSCJUNIOR', 'BioEHSC™ Junior Chair'), ('COMMSERVE', 'Community Service Chair'), ('BDB', 'BDB DeCal Facilitator'), ('OUTR', 'Outreach Chair'))), ('Assistant Officers', (('ASSISACA', 'Academic Assistant Officer'), ('ASSISOUTR', 'Outreach Assistant Officer'), ('ASSISPRODEV', 'Professional Development Assistant Officer'), ('ASSISPROJ', 'Projects Assistant Officer'), ('ASSISIVP', 'Internal Vice President Assistant Officer'), ('ASSISEVP', 'External Vice President Assistant Officer'), ('ASSISBDB', 'BDB DeCal Assistant Facilitator'), ('ASSISTREAS', 'Treasurer Assitant Officer'))), ('Advisors', (('SRADV', 'Senior Advisor'), ('FACADV', 'Faculty Advisor')))], max_length=50),
        ),
    ]

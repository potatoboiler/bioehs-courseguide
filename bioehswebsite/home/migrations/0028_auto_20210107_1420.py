# Generated by Django 2.1.5 on 2021-01-07 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20210107_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semesterspecificinfo',
            name='bioehsc_fee_waiver',
            field=models.URLField(default='http://bit.ly/2021FeeWaiver', help_text='TO BE UPDATED EACH SPRING', verbose_name='BioEHSC Fee Waiver Form'),
        ),
        migrations.AlterField(
            model_name='semesterspecificinfo',
            name='bioehsc_liability_form',
            field=models.URLField(default='https://drive.google.com/file/d/18gLjQ8GgXNe-TPxc1P67NH7GU9CP3eqX/view?usp=sharing', help_text='TO BE UPDATED EACH SPRING', verbose_name='BioEHSC Liability Waiver'),
        ),
        migrations.AlterField(
            model_name='semesterspecificinfo',
            name='bioehsc_online_application',
            field=models.URLField(default='https://docs.google.com/forms/d/e/1FAIpQLSc_ktVT1OwYoN3DqLa4jDid5UJGL-LeTOIUFVQ6Oy5WIlHAOQ/viewform?usp=sf_link', help_text='TO BE UPDATED EACH SPRING', verbose_name='BioEHSC Application'),
        ),
        migrations.AlterField(
            model_name='semesterspecificinfo',
            name='bioehsc_petition_form',
            field=models.URLField(default='http://bit.ly/2021PetitionForm', help_text='TO BE UPDATED EACH SPRING', verbose_name='BioEHSC Petition Form'),
        ),
        migrations.AlterField(
            model_name='semesterspecificinfo',
            name='bioehsc_photo_release_form',
            field=models.URLField(default='https://drive.google.com/file/d/10jd6qY09zx0s0KXWmiSS0XhKCPTEX9Om/view?usp=sharing', help_text='TO BE UPDATED EACH SPRING', verbose_name='BioEHSC Photo Release Form'),
        ),
        migrations.AlterField(
            model_name='semesterspecificinfo',
            name='bioehsc_school_auth_form',
            field=models.URLField(default='https://drive.google.com/file/d/1eGQdCYfGLPtUm8FNHlnMlfcnwkXPWWmj/view?usp=sharing', help_text='TO BE UPDATED EACH SPRING', verbose_name='BioEHSC School Authorization Form'),
        ),
        migrations.AlterField(
            model_name='semesterspecificinfo',
            name='bioehsc_student_registration_form',
            field=models.URLField(default='http://bit.ly/2021BioEHSCEventbrite', help_text='TO BE UPDATED EACH SPRING', verbose_name='BioEHSC Student Registration Form'),
        ),
    ]

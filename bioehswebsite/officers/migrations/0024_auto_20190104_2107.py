# Generated by Django 2.0 on 2019-01-04 21:07

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0023_userprofile_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default='assets/images/officers/headshots/default.jpg', upload_to='assets/images/officers/headshots/'),
        ),
    ]

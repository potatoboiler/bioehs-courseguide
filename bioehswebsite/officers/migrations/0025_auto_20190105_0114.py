# Generated by Django 2.0 on 2019-01-05 01:14

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0024_auto_20190104_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default='headshots/default.jpg', upload_to='headshots/'),
        ),
    ]

# Generated by Django 2.0 on 2018-12-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0008_auto_20181221_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='image',
            field=models.ImageField(default='static/headshots/default.jpg', upload_to='static/headshots'),
        ),
    ]
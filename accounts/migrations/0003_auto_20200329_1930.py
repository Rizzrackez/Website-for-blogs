# Generated by Django 3.0.4 on 2020-03-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190707_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='images',
            field=models.ImageField(blank=True, default='default_image.png', upload_to='profile_image'),
        ),
    ]

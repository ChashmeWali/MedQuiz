# Generated by Django 4.2.6 on 2023-11-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_profile_profile_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_images',
            field=models.ImageField(blank=True, default='usericon.png', null=True, upload_to='profile_images/', verbose_name='Profile Picture'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-04 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_email_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_images',
            new_name='profile_images',
        ),
    ]

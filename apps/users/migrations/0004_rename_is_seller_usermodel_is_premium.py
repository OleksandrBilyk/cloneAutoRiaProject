# Generated by Django 5.0.6 on 2024-07-07 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_usermodel_is_bayer_usermodel_is_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='is_seller',
            new_name='is_premium',
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_is_seller_usermodel_is_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(default=1, upload_to='avatar'),
            preserve_default=False,
        ),
    ]

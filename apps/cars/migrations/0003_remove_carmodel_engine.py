# Generated by Django 5.0.6 on 2024-06-30 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_carmodel_options_carmodel_engine_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='engine',
        ),
    ]

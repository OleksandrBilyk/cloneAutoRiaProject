# Generated by Django 5.0.6 on 2024-07-06 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carmodel_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='body_type',
            field=models.CharField(choices=[('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Crossover', 'Crossover'), ('Universal', 'Universal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z\\s]{2,49}$', ['first letter uppercase', 'min 3', 'max 50'])]),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)]),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2024)]),
        ),
    ]

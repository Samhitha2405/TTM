# Generated by Django 5.0.1 on 2024-01-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0004_remove_register_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phonenumber',
            field=models.PositiveBigIntegerField(),
        ),
    ]

# Generated by Django 4.1.4 on 2023-08-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='trending',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcartmodel',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]

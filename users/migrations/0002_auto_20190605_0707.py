# Generated by Django 2.2.1 on 2019-06-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.IntegerField(default=0),
        ),
    ]
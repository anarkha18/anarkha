# Generated by Django 3.1.6 on 2021-09-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
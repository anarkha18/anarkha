# Generated by Django 3.1.6 on 2021-07-07 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20210707_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='uname',
        ),
    ]

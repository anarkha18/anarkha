# Generated by Django 3.1.6 on 2021-07-03 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210702_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sno',
            new_name='id',
        ),
    ]

# Generated by Django 3.1.6 on 2021-07-09 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_remove_reg_uname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fbuser',
        ),
        migrations.DeleteModel(
            name='Mesg',
        ),
        migrations.DeleteModel(
            name='reg',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserLogin',
        ),
        migrations.DeleteModel(
            name='UserReg',
        ),
    ]

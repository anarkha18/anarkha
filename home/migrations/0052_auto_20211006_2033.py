# Generated by Django 3.1.6 on 2021-10-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.CharField(max_length=200),
        ),
    ]

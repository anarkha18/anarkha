# Generated by Django 3.1.6 on 2021-09-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_auto_20210902_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

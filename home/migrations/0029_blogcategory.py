# Generated by Django 3.1.6 on 2021-08-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientProfile', '0007_alter_clientprofile_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='summary',
            field=models.TextField(default=True),
        ),
    ]

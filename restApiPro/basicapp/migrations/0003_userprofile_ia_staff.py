# Generated by Django 2.2.15 on 2020-08-05 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_remove_userprofile_ia_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ia_staff',
            field=models.BooleanField(default=False),
        ),
    ]

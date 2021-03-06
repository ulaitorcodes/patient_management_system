# Generated by Django 3.0.5 on 2021-09-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='vendor',
            new_name='is_admin',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]

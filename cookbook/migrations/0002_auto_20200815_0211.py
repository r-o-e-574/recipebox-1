# Generated by Django 3.1 on 2020-08-15 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='username',
            new_name='user',
        ),
    ]
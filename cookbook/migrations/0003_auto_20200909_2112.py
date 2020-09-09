# Generated by Django 3.1 on 2020-09-09 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_auto_20200909_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorite', to='cookbook.Recipe'),
        ),
    ]
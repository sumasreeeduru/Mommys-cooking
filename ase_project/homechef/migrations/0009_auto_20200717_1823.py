# Generated by Django 3.0.8 on 2020-07-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homechef', '0008_auto_20200717_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditem',
            old_name='slug',
            new_name='slug1',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='slug2',
            field=models.SlugField(default=0),
        ),
    ]

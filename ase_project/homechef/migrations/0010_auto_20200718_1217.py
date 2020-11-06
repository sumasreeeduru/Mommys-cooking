# Generated by Django 3.0.8 on 2020-07-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homechef', '0009_auto_20200717_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='slug1',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='slug2',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='slug',
            field=models.SlugField(default='test-product'),
            preserve_default=False,
        ),
    ]

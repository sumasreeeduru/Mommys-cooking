# Generated by Django 3.0.4 on 2020-03-26 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homechef', '0003_vendor_food_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='ingredients',
            field=models.ManyToManyField(to='homechef.Ingredients'),
        ),
    ]

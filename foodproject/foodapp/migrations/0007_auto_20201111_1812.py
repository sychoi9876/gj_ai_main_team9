# Generated by Django 3.1.3 on 2020-11-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_auto_20201111_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_history',
            name='food_1',
            field=models.CharField(default=-1, max_length=200),
        ),
    ]

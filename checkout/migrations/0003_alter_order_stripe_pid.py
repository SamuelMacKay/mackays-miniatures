# Generated by Django 3.2.25 on 2024-11-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20241114_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]

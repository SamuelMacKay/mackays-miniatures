# Generated by Django 3.2.25 on 2024-10-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='pre_order',
            field=models.BooleanField(default=False),
        ),
    ]

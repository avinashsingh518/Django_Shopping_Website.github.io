# Generated by Django 3.2.7 on 2021-11-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]

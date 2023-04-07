# Generated by Django 4.2 on 2023-04-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(default=0),
        ),
    ]

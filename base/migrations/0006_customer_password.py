# Generated by Django 4.0.4 on 2022-07-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-07 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='saledetail',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 4.2.13 on 2024-07-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webkiosk", "0002_remove_customer_address_remove_customer_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="date_joined",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 3.1.1 on 2020-10-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active_status',
            field=models.IntegerField(default=1),
        ),
    ]
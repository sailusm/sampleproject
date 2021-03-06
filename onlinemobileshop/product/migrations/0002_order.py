# Generated by Django 3.1.1 on 2020-10-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personname', models.CharField(max_length=123)),
                ('address', models.CharField(max_length=223)),
                ('pin', models.CharField(max_length=123)),
                ('phone', models.CharField(max_length=123)),
                ('email', models.EmailField(max_length=123)),
                ('productid', models.IntegerField()),
            ],
        ),
    ]

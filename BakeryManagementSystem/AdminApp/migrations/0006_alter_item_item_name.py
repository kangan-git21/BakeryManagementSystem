# Generated by Django 4.1 on 2022-08-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0005_alter_item_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

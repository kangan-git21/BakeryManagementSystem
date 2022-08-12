# Generated by Django 4.1 on 2022-08-12 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0002_alter_ingredient_name_alter_item_item_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.item')),
            ],
        ),
    ]
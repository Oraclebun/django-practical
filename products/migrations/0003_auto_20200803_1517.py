# Generated by Django 2.2.14 on 2020-08-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200803_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

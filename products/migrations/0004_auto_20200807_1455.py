# Generated by Django 2.2.14 on 2020-08-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
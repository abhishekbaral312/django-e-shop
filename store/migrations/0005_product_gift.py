# Generated by Django 3.1.3 on 2020-11-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201124_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gift',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.0.6 on 2021-12-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20211223_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2022-07-25 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20220725_1121'),
        ('orders', '0003_auto_20220725_1121'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='suits',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suits_products', to='shop.sub_category'),
        ),
        migrations.AlterIndexTogether(
            name='suits',
            index_together={('id', 'slug')},
        ),
    ]
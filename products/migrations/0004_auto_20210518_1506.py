# Generated by Django 3.2.1 on 2021-05-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210514_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customers_rating',
            field=models.IntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Nothing special'), (4, 'Good'), (5, 'Very good')], default=5),
        ),
        migrations.AddField(
            model_name='product',
            name='publicly_listed',
            field=models.BooleanField(default=False),
        ),
    ]
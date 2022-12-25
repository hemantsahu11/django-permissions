# Generated by Django 4.1.1 on 2022-09-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FOOD', 'food'), ('FLOWER', 'flower'), ('LIQUID', 'liquid'), ('VEHICLE', 'vehicle'), ('ELECTRONIC', 'electronic'), ('OTHERS', 'other')], default='OTHERS', max_length=20),
        ),
    ]

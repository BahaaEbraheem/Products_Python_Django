# Generated by Django 5.1.6 on 2025-04-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=models.TextField(default='Default Product Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='photos/no_image.png', upload_to='photos/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Default Product Name', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

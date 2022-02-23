# Generated by Django 4.0.2 on 2022-02-22 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=200, unique=True)),
                ('pro_slug', models.CharField(max_length=200, unique=True)),
                ('pro_description', models.TextField(blank=True, max_length=500)),
                ('pro_price', models.IntegerField()),
                ('pro_images', models.ImageField(upload_to='photos/products')),
                ('pro_stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0006_page_precio_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
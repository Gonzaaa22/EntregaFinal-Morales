# Generated by Django 5.1.4 on 2024-12-23 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0002_rename_page_pagina_rename_content_pagina_contenido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='imagen',
            field=models.ImageField(upload_to='paginas/'),
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-20 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0002_alter_desenvolvedor_data_modificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desenvolvedor',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
    ]

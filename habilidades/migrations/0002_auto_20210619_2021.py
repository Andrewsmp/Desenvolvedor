# Generated by Django 3.2.4 on 2021-06-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework',
            name='data_modificacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de modificação'),
        ),
        migrations.AlterField(
            model_name='linguagem',
            name='data_modificacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de modificação'),
        ),
    ]

# Generated by Django 3.2.8 on 2022-04-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_Eps', '0003_auto_20220415_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='celular',
            field=models.BigIntegerField(verbose_name='Celular'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assinatura',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]

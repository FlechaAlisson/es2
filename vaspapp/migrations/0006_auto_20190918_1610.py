# Generated by Django 2.2.4 on 2019-09-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaspapp', '0005_auto_20190918_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='presenca',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
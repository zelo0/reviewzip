# Generated by Django 3.1.6 on 2021-02-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewzip', '0005_auto_20210214_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewinfo',
            name='file_path',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewzip', '0002_auto_20210131_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='negative_keyword',
            field=models.ManyToManyField(blank=True, null=True, related_name='negative_keyword', to='reviewzip.Keyword'),
        ),
        migrations.AlterField(
            model_name='review',
            name='negative_sentence',
            field=models.ManyToManyField(blank=True, null=True, related_name='negative_sentence', to='reviewzip.Sentence'),
        ),
        migrations.AlterField(
            model_name='review',
            name='positive_keyword',
            field=models.ManyToManyField(blank=True, null=True, related_name='positive_keyword', to='reviewzip.Keyword'),
        ),
        migrations.AlterField(
            model_name='review',
            name='positive_sentence',
            field=models.ManyToManyField(blank=True, null=True, related_name='positive_sentence', to='reviewzip.Sentence'),
        ),
    ]

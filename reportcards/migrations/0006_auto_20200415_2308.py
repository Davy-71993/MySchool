# Generated by Django 2.2.6 on 2020-04-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportcards', '0005_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='value1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='value2',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

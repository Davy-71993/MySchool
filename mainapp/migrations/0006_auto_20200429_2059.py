# Generated by Django 3.0.5 on 2020-04-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200429_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
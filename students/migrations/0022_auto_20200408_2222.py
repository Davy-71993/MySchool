# Generated by Django 2.2.6 on 2020-04-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0021_auto_20200408_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(default=(), to='students.Subject'),
        ),
    ]

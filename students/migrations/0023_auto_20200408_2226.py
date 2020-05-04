# Generated by Django 2.2.6 on 2020-04-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0022_auto_20200408_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='house',
            field=models.CharField(blank=True, choices=[('Australia', 'Australia'), ('Brazil', 'Brazil'), ('Canada', 'Canada'), ('France', 'France'), ('Japan', 'Japan'), ('Nigeria', 'Nigeria')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(default=(), to='students.Subject'),
        ),
    ]

# Generated by Django 2.2.6 on 2020-04-06 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
        migrations.DeleteModel(
            name='Paper',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
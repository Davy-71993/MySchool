# Generated by Django 2.2.6 on 2020-04-03 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_student'),
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

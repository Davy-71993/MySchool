# Generated by Django 3.0.5 on 2020-04-17 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0030_remove_student_subjects'),
        ('reportcards', '0010_auto_20200416_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Subject'),
        ),
    ]

# Generated by Django 2.2.6 on 2020-04-15 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0030_remove_student_subjects'),
        ('reportcards', '0008_delete_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportcards.MarkList')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]

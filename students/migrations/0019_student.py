# Generated by Django 2.2.6 on 2020-04-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0018_paper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sir_name', models.CharField(max_length=50)),
                ('given_name', models.CharField(max_length=50)),
                ('other_names', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=8)),
                ('passport_photo', models.ImageField(blank=True, null=True, upload_to='passports')),
                ('klass', models.CharField(choices=[('S.1', 'S.1'), ('S.2', 'S.2'), ('S.3', 'S.3'), ('S.4', 'S.4'), ('S.5', 'S.5'), ('S.6', 'S.6')], max_length=5)),
                ('stream', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('S', 'S')], max_length=10)),
                ('house', models.CharField(choices=[('Australia', 'Australia'), ('Brazil', 'Brazil'), ('Canada', 'Canada'), ('France', 'France'), ('Japan', 'Japan'), ('Nigeria', 'Nigeria')], default='Australia', max_length=10)),
                ('subjects', models.ManyToManyField(default=(), to='students.Subject')),
            ],
        ),
    ]

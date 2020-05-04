# Generated by Django 2.2.6 on 2020-04-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0009_auto_20200404_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbr', models.CharField(max_length=6)),
                ('alevel', models.BooleanField()),
                ('olevel', models.BooleanField()),
                ('olevel_code', models.CharField(max_length=10)),
                ('alevel_code', models.CharField(max_length=10)),
                ('is_compulsary', models.BooleanField(default=False)),
            ],
        ),
    ]

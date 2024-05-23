# Generated by Django 5.0.3 on 2024-05-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=150)),
                ('parents_name', models.CharField(max_length=150)),
                ('drop_off', models.CharField(max_length=150)),
                ('pickedby', models.CharField(max_length=150)),
                ('periodofstay', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=150)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateTimeField()),
                ('gender', models.CharField(max_length=150)),
                ('next_of_kin', models.CharField(max_length=100)),
                ('NIN', models.CharField(max_length=150)),
                ('recommender_name', models.CharField(max_length=150)),
                ('level_of_education', models.CharField(max_length=150)),
                ('sitter_number', models.CharField(max_length=150)),
                ('contacts', models.CharField(max_length=150)),
            ],
        ),
    ]

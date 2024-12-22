# Generated by Django 5.1.3 on 2024-12-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Middle_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Phone_Number', models.CharField(max_length=15)),
                ('College_Name', models.CharField(max_length=100)),
                ('Home_Address', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=10)),
                ('Area_Of_Intrest', models.CharField(max_length=100)),
            ],
        ),
    ]

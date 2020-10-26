# Generated by Django 3.1.2 on 2020-10-26 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('percent_completed', models.DecimalField(decimal_places=2, max_digits=4)),
                ('category', models.CharField(choices=[('Novel', 'Novel'), ('Fashion', 'Fashion'), ('Cuisine', 'Cuisine'), ('Religion', 'Religion'), ('Other', 'Other')], max_length=25)),
                ('date', models.DateField(default=datetime.datetime(2020, 10, 26, 20, 47, 31, 68733))),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
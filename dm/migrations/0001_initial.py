# Generated by Django 4.1.6 on 2023-02-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.TextField(default='-', max_length=100)),
                ('rate', models.TextField(default='-', max_length=100)),
                ('price', models.TextField(default='-', max_length=100)),
                ('number', models.TextField(default=0, max_length=100)),
            ],
        ),
    ]

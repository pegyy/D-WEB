# Generated by Django 4.1.6 on 2023-02-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='-', max_length=100)),
                ('upass', models.TextField(default='-', max_length=100)),
                ('username', models.TextField(default='-', max_length=100)),
                ('phone', models.TextField(default='-', max_length=100)),
                ('address', models.TextField(default='-', max_length=100)),
                ('number', models.TextField(default=0, max_length=100)),
            ],
        ),
    ]
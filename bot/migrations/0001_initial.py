# Generated by Django 3.2.11 on 2022-01-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('emoji', models.CharField(max_length=100)),
            ],
        ),
    ]

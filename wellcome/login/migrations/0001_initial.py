# Generated by Django 3.2.11 on 2022-01-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name="Им'я")),
                ('last_name', models.CharField(max_length=30, verbose_name='Призвіще')),
            ],
        ),
    ]

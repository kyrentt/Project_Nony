# Generated by Django 4.2.4 on 2023-09-25 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('pas', models.CharField(max_length=10)),
            ],
        ),
    ]

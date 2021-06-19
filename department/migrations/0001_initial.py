# Generated by Django 3.2.4 on 2021-06-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dep_bio', models.TextField(blank=True, max_length=10000, unique=True)),
            ],
        ),
    ]
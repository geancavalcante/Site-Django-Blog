# Generated by Django 5.0.4 on 2024-04-25 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=10)),
                ('versiculo', models.CharField(max_length=100)),
                ('texto', models.TextField(max_length=600)),
            ],
        ),
    ]
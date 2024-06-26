# Generated by Django 5.0.4 on 2024-04-25 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proverbiosapp', '0002_alter_postagens_texto_alter_postagens_versiculo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postagens',
            name='texto',
        ),
        migrations.AddField(
            model_name='postagens',
            name='aplicacao',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='postagens',
            name='contexto',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='postagens',
            name='tema',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='postagens',
            name='versiculo',
            field=models.CharField(max_length=60, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('white', 'WHITE'), ('black', 'BLACK')], default='black', max_length=6),
        ),
    ]

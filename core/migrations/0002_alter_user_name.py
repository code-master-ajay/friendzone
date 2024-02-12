# Generated by Django 5.0.1 on 2024-02-11 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(help_text='If no name is given, your public display will default to your username.', max_length=256),
        ),
    ]
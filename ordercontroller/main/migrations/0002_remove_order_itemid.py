# Generated by Django 4.1.4 on 2022-12-09 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ItemId',
        ),
    ]
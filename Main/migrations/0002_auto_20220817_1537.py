# Generated by Django 3.2.7 on 2022-08-17 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='challenges',
            name='flag',
            field=models.CharField(default='DPSS{EMPTY}', max_length=255),
        ),
    ]

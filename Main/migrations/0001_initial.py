# Generated by Django 3.2.7 on 2022-08-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('difficulty', models.CharField(max_length=255)),
                ('points', models.IntegerField()),
                ('description', models.TextField(default='', max_length=1000)),
                ('hint', models.CharField(default='', max_length=255)),
                ('flag', models.CharField(default='DPSS{EMPTY}', max_length=255)),
                ('link', models.CharField(default='dashboard', max_length=255)),
                ('solve_status', models.BooleanField(default=False)),
            ],
        ),
    ]

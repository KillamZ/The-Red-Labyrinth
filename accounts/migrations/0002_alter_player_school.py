# Generated by Django 3.2.7 on 2022-08-20 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='school',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.school'),
        ),
    ]

# Generated by Django 2.0.4 on 2018-05-04 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20180504_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilephone',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Category'),
        ),
    ]
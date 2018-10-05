# Generated by Django 2.0.4 on 2018-04-29 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20180429_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='category',
            field=models.ForeignKey(default='Apartment', on_delete=django.db.models.deletion.CASCADE, to='service.Category'),
        ),
        migrations.AlterField(
            model_name='computing',
            name='category',
            field=models.ForeignKey(default='Computing', on_delete=django.db.models.deletion.CASCADE, to='service.Category'),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='category',
            field=models.ForeignKey(default='Ecommerce', on_delete=django.db.models.deletion.CASCADE, to='service.Category'),
        ),
        migrations.AlterField(
            model_name='education',
            name='category',
            field=models.ForeignKey(default='Education', on_delete=django.db.models.deletion.CASCADE, to='service.Category'),
        ),
        migrations.AlterField(
            model_name='others',
            name='category',
            field=models.ForeignKey(default='Others', on_delete=django.db.models.deletion.CASCADE, to='service.Category'),
        ),
        migrations.AlterField(
            model_name='television',
            name='category',
            field=models.ForeignKey(default='Television', on_delete=django.db.models.deletion.CASCADE, to='service.Category'),
        ),
    ]
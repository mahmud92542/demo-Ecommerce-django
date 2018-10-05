# Generated by Django 2.0.4 on 2018-05-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20180430_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('designation', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='team_image')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='category_photo',
            field=models.ImageField(blank=True, upload_to='category_image'),
        ),
    ]

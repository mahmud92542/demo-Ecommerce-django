# Generated by Django 2.0.4 on 2018-04-29 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0005_auto_20180430_0010'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_image')),
                ('profile_name', models.CharField(max_length=50)),
                ('title', models.CharField(choices=[('Mr.', 'Mr'), ('Miss', 'Miss'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs'), ('Ir.', 'Ir'), ('Dr.', 'Dr'), ('Drs', 'Drs'), ('Professor', 'Professor')], max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birth_day', models.DateField()),
                ('phone', models.IntegerField()),
                ('qualification', models.TextField(blank=True, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.District')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Division')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
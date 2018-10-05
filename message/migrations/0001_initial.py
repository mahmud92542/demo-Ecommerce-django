# Generated by Django 2.0.4 on 2018-05-02 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userinfo', '0002_remove_profile_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

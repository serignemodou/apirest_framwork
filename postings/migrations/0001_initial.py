# Generated by Django 2.1.3 on 2018-12-02 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(max_length=15)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

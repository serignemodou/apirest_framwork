# Generated by Django 2.1.3 on 2018-12-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='content',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

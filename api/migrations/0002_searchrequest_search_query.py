# Generated by Django 2.2.1 on 2019-11-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchrequest',
            name='search_query',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 4.0 on 2022-01-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_useranswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lastRecommendation',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

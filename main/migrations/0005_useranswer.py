# Generated by Django 4.0 on 2022-01-09 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0004_question_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.answer')),
                ('q', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
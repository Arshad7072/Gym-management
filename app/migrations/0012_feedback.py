# Generated by Django 5.0.6 on 2024-08-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_trainer_join_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=12)),
                ('feedback', models.CharField(max_length=150)),
            ],
        ),
    ]

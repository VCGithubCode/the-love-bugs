# Generated by Django 4.2.7 on 2024-02-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_one', models.CharField(blank=True, max_length=30, null=True)),
                ('name_two', models.CharField(blank=True, max_length=30, null=True)),
                ('location_one', models.CharField(blank=True, max_length=100)),
                ('location_two', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, choices=[('option1', 'Situationship'), ('option2', 'Officially together'), ('option3', 'Engaged'), ('option4', 'Married')], max_length=20, null=True)),
            ],
        ),
    ]

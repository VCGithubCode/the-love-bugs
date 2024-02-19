from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profile_datetime_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('Situationship', 'Situationship'), ('Officially together', 'Officially together'), ('Engaged', 'Engaged'), ('Married', 'Married')], max_length=20, null=True),
        ),
    ]

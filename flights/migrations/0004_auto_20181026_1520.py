# Generated by Django 2.1.2 on 2018-10-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passengers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passengers',
            name='flight',
        ),
        migrations.AddField(
            model_name='passengers',
            name='flight',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight'),
        ),
    ]

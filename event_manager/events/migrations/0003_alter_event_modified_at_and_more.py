# Generated by Django 5.1.2 on 2024-11-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventattendee',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanager', '0004_participantregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantregistration',
            name='contactNumber',
            field=models.CharField(max_length=12),
        ),
    ]

# Generated by Django 3.1.7 on 2023-08-10 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circle',
            options={'get_latest_by': 'created', 'ordering': ['-rides_taken', '-rides_offered']},
        ),
    ]

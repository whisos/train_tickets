# Generated by Django 5.0.2 on 2024-02-22 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train_tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-02 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('сonstructionСompany', '0002_project_alter_personnel_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='price',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='weight',
        ),
    ]

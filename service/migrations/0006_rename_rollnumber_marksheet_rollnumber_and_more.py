# Generated by Django 4.0.3 on 2022-05-18 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_user_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marksheet',
            old_name='rollnumber',
            new_name='rollNumber',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subjectDiscription',
            new_name='subjectDescription',
        ),
    ]

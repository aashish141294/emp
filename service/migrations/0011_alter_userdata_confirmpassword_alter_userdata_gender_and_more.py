# Generated by Django 4.1.7 on 2023-04-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='ConfirmPassword',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='Gender',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='Password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
# Generated by Django 4.1 on 2022-09-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pwd',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='userid',
            field=models.CharField(default='', max_length=32),
        ),
    ]

# Generated by Django 4.1 on 2022-10-29 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_userinfo_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='userid',
            field=models.CharField(default='', max_length=32, primary_key=True, serialize=False),
        ),
    ]

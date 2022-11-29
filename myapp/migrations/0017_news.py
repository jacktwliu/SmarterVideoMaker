# Generated by Django 4.1 on 2022-11-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsdate', models.DateField()),
                ('newsname', models.CharField(default='', max_length=20)),
                ('newssubject', models.CharField(default='', max_length=100)),
                ('newsperson', models.CharField(default='', max_length=10)),
            ],
        ),
    ]

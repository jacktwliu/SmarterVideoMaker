# Generated by Django 4.1 on 2022-11-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_userinfo_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedbacktype', models.CharField(default='', max_length=10)),
                ('detail', models.CharField(default='', max_length=100)),
                ('feedbackemail', models.CharField(default='', max_length=32)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_friend_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlement',
            name='must_pay',
            field=models.IntegerField(default=0),
        ),
    ]

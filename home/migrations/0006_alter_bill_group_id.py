# Generated by Django 4.0.3 on 2022-03-28 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_bill_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='group_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.group'),
        ),
    ]

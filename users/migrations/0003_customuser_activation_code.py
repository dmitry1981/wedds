# Generated by Django 2.2.6 on 2019-11-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191114_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='activation_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

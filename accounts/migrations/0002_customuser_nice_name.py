# Generated by Django 3.1.4 on 2020-12-09 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='nice_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

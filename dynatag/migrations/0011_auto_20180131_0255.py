# Generated by Django 2.0 on 2018-01-31 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynatag', '0010_auto_20180131_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]

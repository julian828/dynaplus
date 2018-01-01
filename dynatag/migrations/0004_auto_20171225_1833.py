# Generated by Django 2.0 on 2017-12-25 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dynatag', '0003_auto_20171224_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=256, null=True)),
                ('address_street', models.CharField(max_length=256, null=True)),
                ('address_city', models.CharField(max_length=256, null=True)),
                ('address_province', models.CharField(max_length=256, null=True)),
                ('address_country', models.CharField(max_length=256, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='penddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='pstartdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='targetdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dynatag.Profile'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dynatag.Profile'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

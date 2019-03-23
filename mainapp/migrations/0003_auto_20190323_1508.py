# Generated by Django 2.1.7 on 2019-03-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190323_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='check_in_2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='check_out_2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='days_count_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='rate_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='room_no_2',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
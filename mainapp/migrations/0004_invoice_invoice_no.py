# Generated by Django 2.1.5 on 2019-03-19 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190319_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

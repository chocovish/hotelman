# Generated by Django 2.1.7 on 2019-04-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190331_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]

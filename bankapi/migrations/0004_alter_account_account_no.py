# Generated by Django 5.0.6 on 2024-07-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapi', '0003_account_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_no',
            field=models.CharField(default='0000', max_length=20),
        ),
    ]

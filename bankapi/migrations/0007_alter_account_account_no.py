# Generated by Django 5.0.6 on 2024-07-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapi', '0006_account_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_no',
            field=models.CharField(editable=False, max_length=250, unique=True),
        ),
    ]
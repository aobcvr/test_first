# Generated by Django 2.2.20 on 2021-04-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('clients', '0002_alter_client_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
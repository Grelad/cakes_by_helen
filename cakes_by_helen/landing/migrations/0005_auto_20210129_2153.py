# Generated by Django 3.1.5 on 2021-01-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20210129_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(blank=True, choices=[('classic_cake', 'Classic Cake'), ('custom_cake', 'Custom Cake'), ('pastries', 'Pastries'), ('gingerbread', 'Gingerbread')], max_length=12, null=True),
        ),
    ]

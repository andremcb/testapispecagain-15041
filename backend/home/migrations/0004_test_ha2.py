# Generated by Django 2.2.12 on 2020-06-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='ha2',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True),
        ),
    ]

# Generated by Django 3.0.6 on 2020-10-23 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0002_auto_20201019_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionproduct',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]

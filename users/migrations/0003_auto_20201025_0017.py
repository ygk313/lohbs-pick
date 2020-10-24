# Generated by Django 3.0.6 on 2020-10-25 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201012_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address1',
            field=models.CharField(default='주소1', max_length=300, verbose_name='주소1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='address2',
            field=models.CharField(default='주소2', max_length=300, verbose_name='주소2 참고항목'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(default='00000', max_length=5, verbose_name='우편번호'),
            preserve_default=False,
        ),
    ]

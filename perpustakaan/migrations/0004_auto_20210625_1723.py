# Generated by Django 3.2.4 on 2021-06-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_auto_20210624_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
        migrations.AddField(
            model_name='buku',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

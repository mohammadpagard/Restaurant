# Generated by Django 3.2 on 2022-05-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(default=1, upload_to='images/staff'),
            preserve_default=False,
        ),
    ]

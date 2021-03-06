# Generated by Django 3.2 on 2022-05-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('rate', models.IntegerField()),
                ('price', models.IntegerField()),
                ('time', models.IntegerField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='images/foods/')),
            ],
        ),
    ]

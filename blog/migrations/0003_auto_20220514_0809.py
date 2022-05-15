# Generated by Django 3.2 on 2022-05-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
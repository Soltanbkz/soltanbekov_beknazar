# Generated by Django 5.0.1 on 2024-01-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_price_new_price_alter_price_old_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('about_text', models.CharField(max_length=200, verbose_name='about text')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('my_photo', models.FileField(upload_to='photos/')),
                ('hello', models.CharField(max_length=200, verbose_name='hello text')),
            ],
        ),
    ]

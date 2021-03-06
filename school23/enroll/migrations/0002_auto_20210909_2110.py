# Generated by Django 3.2.6 on 2021-09-10 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=' ', max_length=70),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=' ', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='re_password',
            field=models.CharField(max_length=10),
        ),
    ]

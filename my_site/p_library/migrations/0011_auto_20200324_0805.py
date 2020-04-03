# Generated by Django 2.2.6 on 2020-03-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0010_auto_20200324_0741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='debt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='friends',
            field=models.ManyToManyField(to='p_library.Friend'),
        ),
    ]
# Generated by Django 3.1.4 on 2021-05-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_otherlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]
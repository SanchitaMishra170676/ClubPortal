# Generated by Django 3.1.5 on 2021-05-14 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210514_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videolecture',
            old_name='embeded_code',
            new_name='embeded_link',
        ),
    ]

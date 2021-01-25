# Generated by Django 2.1.5 on 2020-08-26 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='paragraph',
            new_name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-11-09 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment',)},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]
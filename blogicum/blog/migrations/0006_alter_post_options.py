# Generated by Django 3.2.16 on 2024-12-21 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20241222_0002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date', 'title'], 'verbose_name': 'публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
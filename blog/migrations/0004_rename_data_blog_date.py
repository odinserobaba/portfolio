# Generated by Django 4.1.7 on 2023-03-22 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_description_alter_blog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='data',
            new_name='date',
        ),
    ]

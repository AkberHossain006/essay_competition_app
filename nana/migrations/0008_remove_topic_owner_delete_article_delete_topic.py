# Generated by Django 4.2.14 on 2024-11-12 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nana', '0007_alter_essaytopic_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]

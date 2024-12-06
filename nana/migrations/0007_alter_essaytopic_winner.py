# Generated by Django 4.2.14 on 2024-10-17 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nana', '0006_alter_essaytopic_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essaytopic',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
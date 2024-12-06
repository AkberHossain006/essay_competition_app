# Generated by Django 4.2.14 on 2024-08-13 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nana', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author_name', models.CharField(default='sample', max_length=200)),
                ('age', models.IntegerField(default=18)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nana.topic')),
            ],
            options={
                'verbose_name_plural': 'Article',
            },
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]

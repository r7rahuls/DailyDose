# Generated by Django 4.1.7 on 2023-04-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField(max_length=800)),
                ('category', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
            ],
        ),
    ]

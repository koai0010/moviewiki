# Generated by Django 4.2.16 on 2024-10-24 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviewiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='background_path',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api5', '0002_imageslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickLinks',
            fields=[
                ('QuickLinks_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FilePathField()),
                ('text', models.TextField()),
                ('added_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

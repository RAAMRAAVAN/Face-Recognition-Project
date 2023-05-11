# Generated by Django 4.1.7 on 2023-02-24 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_trainimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('person_name', models.CharField(max_length=50)),
                ('added_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TrainImages',
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_auto_20210703_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reply', models.CharField(max_length=5000)),
                ('comment_id', models.IntegerField()),
            ],
        ),
    ]

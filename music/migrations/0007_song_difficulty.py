# Generated by Django 3.1.7 on 2021-03-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20210328_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='difficulty',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 3.2.12 on 2022-05-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=250, null=True),
        ),
    ]

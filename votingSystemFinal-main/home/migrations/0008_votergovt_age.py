# Generated by Django 4.0.4 on 2022-04-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_name_feedback_name2'),
    ]

    operations = [
        migrations.AddField(
            model_name='votergovt',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
# Generated by Django 4.0.4 on 2022-04-16 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_votergovt_voterregisteredamroha_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UIDamroha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pannumber', models.CharField(max_length=10)),
                ('uniqueid', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UIDpalghar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pannumber', models.CharField(max_length=10)),
                ('uniqueid', models.CharField(max_length=10)),
            ],
        ),
    ]

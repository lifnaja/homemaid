# Generated by Django 3.0.8 on 2020-07-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('description', models.TextField()),
                ('certificate', models.TextField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]

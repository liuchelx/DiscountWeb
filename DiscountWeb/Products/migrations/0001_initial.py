# Generated by Django 2.2.7 on 2019-12-07 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_ID', models.IntegerField(default=0)),
                ('ProductName', models.CharField(max_length=200)),
                ('PubTime', models.DateTimeField(verbose_name='Product Released')),
                ('OriPrice', models.FloatField(default=0)),
                ('DisPrice', models.FloatField(default=0)),
                ('link', models.URLField(max_length=500)),
                ('Tag', models.CharField(max_length=200)),
                ('click', models.IntegerField(default=0)),
                ('EndTime', models.DateTimeField(verbose_name='Discount End')),
            ],
        ),
    ]
# Generated by Django 3.1.1 on 2020-11-13 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('detail', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/')),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('width', models.IntegerField(max_length=10)),
                ('height', models.IntegerField(max_length=10)),
                ('src', models.CharField(max_length=100)),
                ('album', models.TextField(max_length=100)),
                ('is_grid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
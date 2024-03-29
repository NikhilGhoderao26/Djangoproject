# Generated by Django 2.1.7 on 2019-11-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('idpackages', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=45)),
            ],
            options={
                'db_table': 'packages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='djangoapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('djangoapp_name', models.CharField(max_length=50)),
                ('djangoapp_mailid', models.CharField(max_length=20)),
                ('created_at', models.DateField()),
            ],
        ),
    ]

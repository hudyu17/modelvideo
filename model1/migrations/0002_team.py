# Generated by Django 2.1.7 on 2019-04-16 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('payroll', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1 on 2022-08-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='This field is required', max_length=40)),
                ('description', models.TextField(db_column='aciklama')),
                ('number', models.IntegerField(unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('priority', models.CharField(choices=[('1', 'first'), ('2', 'second'), ('3', 'third'), ('4', 'fourth')], max_length=20)),
                ('status', models.CharField(choices=[('C', 'Completed'), ('P', 'Pending'), ('I', 'In-Progress')], max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Todoss',
                'ordering': ['number'],
            },
        ),
    ]

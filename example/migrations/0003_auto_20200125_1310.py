# Generated by Django 3.0.2 on 2020-01-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_programmer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='programmer',
            name='languages',
            field=models.ManyToManyField(to='example.Language'),
        ),
    ]

# Generated by Django 3.0.1 on 2020-06-29 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=64)),
                ('date', models.DateField(auto_now=True, db_index=True)),
                ('time', models.TimeField(auto_now=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('document', models.FileField(blank=True, upload_to='files')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.ChatRoom')),
            ],
        ),
    ]

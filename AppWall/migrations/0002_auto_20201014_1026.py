# Generated by Django 3.1.1 on 2020-10-14 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppWall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='message_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remarks', to='AppWall.messages'),
        ),
    ]

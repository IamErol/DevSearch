# Generated by Django 4.1.3 on 2023-01-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_eamil_message_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='devsearch/static/images/profiles/user-default.png', null=True, upload_to='devsearch/static/images/profiles'),
        ),
    ]
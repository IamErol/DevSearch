# Generated by Django 4.1.3 on 2023-01-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='DevSearch/devsearch/static/images/devsearch/static/images/profiles/user-default.png', null=True, upload_to='DevSearch/devsearch/static/images/devsearch/static/images/profiles/'),
        ),
    ]
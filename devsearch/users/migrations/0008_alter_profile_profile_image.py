# Generated by Django 4.1.3 on 2023-01-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='/DevSearch/devsearch/static/images/profiles/user-default.png', null=True, upload_to='devsearch/staticfiles/images/profiles'),
        ),
    ]

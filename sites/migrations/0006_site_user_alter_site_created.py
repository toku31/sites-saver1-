# Generated by Django 4.0.4 on 2022-07-07 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username'),
        ('sites', '0005_alter_site_category_alter_site_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='site',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='投稿日'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-16 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location'),
        ('sites', '0007_alter_site_options_category_created_tag_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(blank=True, choices=[('up', 'いいね'), ('down', '良くない')], max_length=200, verbose_name='感想（選択）'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'site')},
        ),
    ]

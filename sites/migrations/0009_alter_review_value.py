# Generated by Django 4.0.4 on 2022-07-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0008_review_owner_alter_review_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(blank=True, choices=[('up', 'いいね'), ('down', 'いまいち')], max_length=200, verbose_name='感想（選択）'),
        ),
    ]

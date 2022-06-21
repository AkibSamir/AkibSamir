# Generated by Django 3.2 on 2022-06-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_blogpost_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='comment',
        ),
        migrations.AlterField(
            model_name='about',
            name='sub_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='title1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='title2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
    ]
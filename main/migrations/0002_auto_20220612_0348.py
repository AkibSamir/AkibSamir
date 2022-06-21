# Generated by Django 3.2.4 on 2022-06-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('social_twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('social_facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('social_instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('social_github', models.CharField(blank=True, max_length=200, null=True)),
                ('social_linkedIn', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hero')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Facts',
        ),
    ]

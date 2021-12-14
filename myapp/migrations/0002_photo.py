# Generated by Django 3.2.8 on 2021-12-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_Main_Img', models.ImageField(blank=True, null=True, upload_to='photo/')),
            ],
        ),
    ]

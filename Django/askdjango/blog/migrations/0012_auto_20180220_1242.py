# Generated by Django 2.0.1 on 2018-02-20 03:42

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180220_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]
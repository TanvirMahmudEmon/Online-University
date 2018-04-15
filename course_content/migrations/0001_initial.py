# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('pdf_title', models.CharField(max_length=250, verbose_name='PDF Title 1')),
                ('pdf', models.TextField(verbose_name='Embed Code 1')),
                ('video_title', models.CharField(max_length=250, verbose_name='Video Title 1')),
                ('video', models.TextField(verbose_name='Embed Code 1')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0002_auto_20150630_1208'),
        ('trans', '0048_auto_20151120_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='whiteboardmessage',
            name='language',
            field=models.ForeignKey(to='lang.Language', null=True),
        ),
        migrations.AddField(
            model_name='whiteboardmessage',
            name='project',
            field=models.ForeignKey(to='trans.Project', null=True),
        ),
        migrations.AddField(
            model_name='whiteboardmessage',
            name='subproject',
            field=models.ForeignKey(to='trans.SubProject', null=True),
        ),
    ]

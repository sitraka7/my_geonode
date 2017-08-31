# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partenaires',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_organisation', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('lien_site', models.CharField(max_length=300)),
                ('logo', models.CharField(max_length=800)),
            ],
        ),
    ]

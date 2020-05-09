# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-24 13:18
from __future__ import unicode_literals

from django.db import migrations
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0030_rename__githubuser__to__user'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='three_d_secure',
            field=djstripe.fields.StripeTextField(help_text=b'State of 3D secure requirement', null=True),
        ),
    ]

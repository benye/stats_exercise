# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeadThings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LiveThings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('p_id', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LivePeople',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='things.Person')),
                ('age', models.IntegerField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
            bases=('things.person',),
        ),
        migrations.CreateModel(
            name='DeadPeople',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='things.Person')),
                ('age_at_death', models.IntegerField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
            bases=('things.person',),
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('t_id', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_things.person_set+', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='livethings',
            name='person',
            field=models.ForeignKey(to='things.LivePeople', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='livethings',
            name='thing',
            field=models.ForeignKey(to='things.Thing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deadthings',
            name='person',
            field=models.ForeignKey(to='things.DeadPeople', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deadthings',
            name='thing',
            field=models.ForeignKey(to='things.Thing'),
            preserve_default=True,
        ),
    ]

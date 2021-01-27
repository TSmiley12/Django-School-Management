# Generated by Django 2.2.13 on 2021-01-25 22:54

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_auto_20210124_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('widget_type', models.CharField(choices=[('text', 'Text Content'), ('list', 'List Items')], default='text', max_length=10)),
                ('widget_title', models.CharField(max_length=50)),
                ('widget_number', models.PositiveSmallIntegerField(unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WidgetListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('widget_type', models.CharField(choices=[('text', 'Text Content'), ('list', 'List Items')], default='text', max_length=10)),
                ('widget_title', models.CharField(max_length=50)),
                ('widget_number', models.PositiveSmallIntegerField(unique=True)),
                ('text', models.CharField(max_length=150)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('widget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.ListWidget')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
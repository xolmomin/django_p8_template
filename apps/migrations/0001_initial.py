# Generated by Django 4.2.1 on 2023-05-06 04:20

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import shared.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('discount', models.SmallIntegerField(default=0)),
                ('detail', ckeditor.fields.RichTextField()),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.category')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, shared.models.BaseDateModel),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=shared.models.upload_name)),
                ('type', models.CharField(choices=[('images', 'Rasmlar'), ('documents', 'Dokumentlar'), ('videos', 'Videolar')], max_length=15)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images',
                                              to='apps.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=255)),
                ('star', models.SmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.product')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, shared.models.BaseDateModel),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent',
                 mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                            related_name='children', to='apps.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-05 04:45

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('item_type', models.CharField(db_index=True, max_length=50)),
                ('author', models.CharField(max_length=100, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(max_length=500, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('text', models.TextField(null=True)),
                ('score', models.BigIntegerField(default=0, null=True)),
                ('parent_id', models.IntegerField(null=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'All Items',
                'verbose_name_plural': 'All Items',
                'ordering': ['-time'],
            },
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]

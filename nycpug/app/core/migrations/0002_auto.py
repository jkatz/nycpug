# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    depends_on = (
        ('app.sponsor', '0001_initial'),
    )

    def forwards(self, orm):
        
        # Adding M2M table for field sponsor_categories on 'Conference'
        db.create_table('core_conference_sponsor_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('conference', models.ForeignKey(orm['core.conference'], null=False)),
            ('sponsorcategory', models.ForeignKey(orm['sponsor.sponsorcategory'], null=False))
        ))
        db.create_unique('core_conference_sponsor_categories', ['conference_id', 'sponsorcategory_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field sponsor_categories on 'Conference'
        db.delete_table('core_conference_sponsor_categories')


    models = {
        'core.conference': {
            'Meta': {'object_name': 'Conference'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sponsor_categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sponsor.SponsorCategory']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'sponsor.sponsorcategory': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'SponsorCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']

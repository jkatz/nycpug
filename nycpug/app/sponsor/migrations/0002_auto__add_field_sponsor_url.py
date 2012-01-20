# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Sponsor.url'
        db.add_column('sponsor_sponsor', 'url', self.gf('django.db.models.fields.URLField')(default='', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Sponsor.url'
        db.delete_column('sponsor_sponsor', 'url')


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
        'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsors'", 'to': "orm['sponsor.SponsorCategory']"}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsors'", 'to': "orm['core.Conference']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'sponsor.sponsorcategory': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'SponsorCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['sponsor']

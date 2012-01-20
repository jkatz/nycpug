# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    depends_on = (
        ('app.core', '0001_initial'),
    )

    def forwards(self, orm):
        
        # Adding model 'Sponsor'
        db.create_table('sponsor_sponsor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sponsors', to=orm['core.Conference'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sponsors', to=orm['sponsor.SponsorCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('sponsor', ['Sponsor'])

        # Adding model 'SponsorCategory'
        db.create_table('sponsor_sponsorcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('sponsor', ['SponsorCategory'])


    def backwards(self, orm):
        
        # Deleting model 'Sponsor'
        db.delete_table('sponsor_sponsor')

        # Deleting model 'SponsorCategory'
        db.delete_table('sponsor_sponsorcategory')


    models = {
        'core.conference': {
            'Meta': {'object_name': 'Conference'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsors'", 'to': "orm['sponsor.SponsorCategory']"}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsors'", 'to': "orm['core.Conference']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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

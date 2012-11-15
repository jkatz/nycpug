# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Proposal.conference'
        db.add_column('core_proposal', 'conference', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proposals', null=True, to=orm['core.Conference']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Proposal.conference'
        db.delete_column('core_proposal', 'conference_id')


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
        'core.proposal': {
            'Meta': {'object_name': 'Proposal'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proposals'", 'null': 'True', 'to': "orm['core.Conference']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'proposal_length': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proposal_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proposals'", 'null': 'True', 'to': "orm['core.Speaker']"})
        },
        'core.room': {
            'Meta': {'object_name': 'Room'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rooms'", 'to': "orm['core.Venue']"})
        },
        'core.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'entire_space': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proposal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Proposal']", 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'schedules'", 'null': 'True', 'to': "orm['core.Room']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'core.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'core.venue': {
            'Meta': {'object_name': 'Venue'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'conference': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Conference']", 'unique': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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

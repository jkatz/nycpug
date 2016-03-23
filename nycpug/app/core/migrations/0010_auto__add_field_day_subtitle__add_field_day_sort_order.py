# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Day.subtitle'
        db.add_column(u'core_day', 'subtitle',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Day.sort_order'
        db.add_column(u'core_day', 'sort_order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Day.subtitle'
        db.delete_column(u'core_day', 'subtitle')

        # Deleting field 'Day.sort_order'
        db.delete_column(u'core_day', 'sort_order')


    models = {
        u'account.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.article': {
            'Meta': {'object_name': 'Article'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles'", 'to': u"orm['core.Conference']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.User']"})
        },
        u'core.block': {
            'Meta': {'ordering': "['day__event_date', 'start_time']", 'object_name': 'Block'},
            'day': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blocks'", 'to': u"orm['core.Day']"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'core.conference': {
            'Meta': {'object_name': 'Conference'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_call_for_papers_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_schedule_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'sponsor_categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'conferences'", 'blank': 'True', 'to': u"orm['core.SponsorCategory']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'core.day': {
            'Meta': {'ordering': "['event_date']", 'object_name': 'Day'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'days'", 'to': u"orm['core.Conference']"}),
            'event_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'days'", 'to': u"orm['core.Venue']"})
        },
        u'core.event': {
            'Meta': {'object_name': 'Event'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['core.Block']"}),
            'event_bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event_speaker': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_full_block': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'proposal': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Proposal']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['core.Room']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Track']", 'null': 'True', 'blank': 'True'})
        },
        u'core.opinion': {
            'Meta': {'unique_together': "(('user', 'proposal'),)", 'object_name': 'Opinion'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_recommended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'proposal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opinions'", 'to': u"orm['core.Proposal']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opinions'", 'to': u"orm['account.User']"})
        },
        u'core.proposal': {
            'Meta': {'object_name': 'Proposal'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proposals'", 'to': u"orm['core.Conference']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'Regular'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proposals'", 'to': u"orm['account.User']"})
        },
        u'core.room': {
            'Meta': {'object_name': 'Room'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rooms'", 'to': u"orm['core.Venue']"})
        },
        u'core.sponsor': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Sponsor'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsors'", 'to': u"orm['core.SponsorCategory']"}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsors'", 'to': u"orm['core.Conference']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'core.sponsorcategory': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'SponsorCategory'},
            'css_class': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.track': {
            'Meta': {'ordering': "['name']", 'object_name': 'Track'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': u"orm['core.Conference']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.venue': {
            'Meta': {'object_name': 'Venue'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'venues'", 'to': u"orm['core.Conference']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['core']
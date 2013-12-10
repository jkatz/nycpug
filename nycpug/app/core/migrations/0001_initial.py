# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'core_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles', to=orm['core.Conference'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'core', ['Article'])

        # Adding model 'Block'
        db.create_table(u'core_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blocks', to=orm['core.Day'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['Block'])

        # Adding model 'Conference'
        db.create_table(u'core_conference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'core', ['Conference'])

        # Adding M2M table for field sponsor_categories on 'Conference'
        m2m_table_name = db.shorten_name(u'core_conference_sponsor_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('conference', models.ForeignKey(orm[u'core.conference'], null=False)),
            ('sponsorcategory', models.ForeignKey(orm[u'core.sponsorcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['conference_id', 'sponsorcategory_id'])

        # Adding model 'Day'
        db.create_table(u'core_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(related_name='days', to=orm['core.Conference'])),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(related_name='days', to=orm['core.Venue'])),
            ('event_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'core', ['Day'])

        # Adding model 'Event'
        db.create_table(u'core_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['core.Block'])),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['core.Room'])),
            ('proposal', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Proposal'], unique=True, null=True, blank=True)),
            ('event_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('event_speaker', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('event_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Event'])

        # Adding model 'Proposal'
        db.create_table(u'core_proposal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proposals', to=orm['core.Conference'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proposals', to=orm['account.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('format', self.gf('django.db.models.fields.CharField')(default='50', max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Proposal'])

        # Adding model 'Room'
        db.create_table(u'core_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rooms', to=orm['core.Venue'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Room'])

        # Adding model 'Sponsor'
        db.create_table(u'core_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sponsors', to=orm['core.Conference'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sponsors', to=orm['core.SponsorCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'core', ['Sponsor'])

        # Adding model 'SponsorCategory'
        db.create_table(u'core_sponsorcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'core', ['SponsorCategory'])

        # Adding model 'Venue'
        db.create_table(u'core_venue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(related_name='venues', to=orm['core.Conference'])),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Venue'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'core_article')

        # Deleting model 'Block'
        db.delete_table(u'core_block')

        # Deleting model 'Conference'
        db.delete_table(u'core_conference')

        # Removing M2M table for field sponsor_categories on 'Conference'
        db.delete_table(db.shorten_name(u'core_conference_sponsor_categories'))

        # Deleting model 'Day'
        db.delete_table(u'core_day')

        # Deleting model 'Event'
        db.delete_table(u'core_event')

        # Deleting model 'Proposal'
        db.delete_table(u'core_proposal')

        # Deleting model 'Room'
        db.delete_table(u'core_room')

        # Deleting model 'Sponsor'
        db.delete_table(u'core_sponsor')

        # Deleting model 'SponsorCategory'
        db.delete_table(u'core_sponsorcategory')

        # Deleting model 'Venue'
        db.delete_table(u'core_venue')


    models = {
        u'account.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
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
            'Meta': {'object_name': 'Block'},
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
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'sponsor_categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'conferences'", 'blank': 'True', 'to': u"orm['core.SponsorCategory']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'core.day': {
            'Meta': {'object_name': 'Day'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'days'", 'to': u"orm['core.Conference']"}),
            'event_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'days'", 'to': u"orm['core.Venue']"})
        },
        u'core.event': {
            'Meta': {'object_name': 'Event'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['core.Block']"}),
            'event_description': ('django.db.models.fields.TextField', [], {}),
            'event_speaker': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proposal': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Proposal']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['core.Room']"})
        },
        u'core.proposal': {
            'Meta': {'object_name': 'Proposal'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proposals'", 'to': u"orm['core.Conference']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'50'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proposals'", 'to': u"orm['account.User']"})
        },
        u'core.room': {
            'Meta': {'object_name': 'Room'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
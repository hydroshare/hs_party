# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AddressType'
        db.create_table(u'hs_party_addresstype', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=24, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('hs_party', ['AddressType'])

        # Adding model 'PhoneType'
        db.create_table(u'hs_party_phonetype', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=24, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('hs_party', ['PhoneType'])

        # Adding model 'EmailType'
        db.create_table(u'hs_party_emailtype', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=24, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('hs_party', ['EmailType'])

        # Adding model 'City'
        db.create_table(u'hs_party_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geonamesUrl', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('hs_party', ['City'])

        # Adding model 'Region'
        db.create_table(u'hs_party_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geonamesUrl', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('hs_party', ['Region'])

        # Adding model 'Country'
        db.create_table(u'hs_party_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geonamesUrl', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('hs_party', ['Country'])

        # Adding model 'ExternalIdentifierType'
        db.create_table(u'hs_party_externalidentifiertype', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=24, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('hs_party', ['ExternalIdentifierType'])

        # Adding model 'Person'
        db.create_table(u'hs_party_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('uniqueCode', self.gf('django.db.models.fields.CharField')(default='cd63582c-affd-4394-9bae-3b6eef69ee96', max_length=64)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length='255', blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('lastUpdate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('givenName', self.gf('django.db.models.fields.CharField')(max_length='125')),
            ('familyName', self.gf('django.db.models.fields.CharField')(max_length='125')),
            ('jobTitle', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
            ('primaryOrganizationName', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
            ('primaryAddress', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
            ('primaryTelephone', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('primaryOrganizationRecord', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['hs_party.Organization'])),
        ))
        db.send_create_signal('hs_party', ['Person'])

        # Adding model 'PersonEmail'
        db.create_table(u'hs_party_personemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('phone_type', self.gf('django.db.models.fields.related.ForeignKey')(default='other', to=orm['hs_party.EmailType'], blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='email_addresses', null=True, to=orm['hs_party.Person'])),
        ))
        db.send_create_signal('hs_party', ['PersonEmail'])

        # Adding model 'PersonLocation'
        db.create_table(u'hs_party_personlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('address_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.AddressType'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mail_addresses', null=True, to=orm['hs_party.Person'])),
        ))
        db.send_create_signal('hs_party', ['PersonLocation'])

        # Adding model 'PersonPhone'
        db.create_table(u'hs_party_personphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('phone_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.PhoneType'], blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='phone_numbers', null=True, to=orm['hs_party.Person'])),
        ))
        db.send_create_signal('hs_party', ['PersonPhone'])

        # Adding model 'UserType'
        db.create_table(u'hs_party_usertype', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=24, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('hs_party', ['UserType'])

        # Adding model 'OtherNames'
        db.create_table(u'hs_party_othernames', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persons', self.gf('django.db.models.fields.related.ForeignKey')(related_name='otherNames', to=orm['hs_party.Person'])),
            ('otherName', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('annotation', self.gf('django.db.models.fields.CharField')(default='citation', max_length='10')),
        ))
        db.send_create_signal('hs_party', ['OtherNames'])

        # Adding model 'OrganizationType'
        db.create_table(u'hs_party_organizationtype', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=24, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('hs_party', ['OrganizationType'])

        # Adding model 'Organization'
        db.create_table(u'hs_party_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'specialities_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            (u'keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('uniqueCode', self.gf('django.db.models.fields.CharField')(default='1177a306-511b-407a-b68e-16314272ac69', max_length=64)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length='255', blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('lastUpdate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('logoUrl', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('parentOrganization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.Organization'], null=True, blank=True)),
            ('organizationType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.OrganizationType'])),
            ('businessAddress', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
            ('businessTelephone', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
        ))
        db.send_create_signal('hs_party', ['Organization'])

        # Adding model 'OrganizationEmail'
        db.create_table(u'hs_party_organizationemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('phone_type', self.gf('django.db.models.fields.related.ForeignKey')(default='other', to=orm['hs_party.EmailType'], blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='email_addresses', null=True, to=orm['hs_party.Organization'])),
        ))
        db.send_create_signal('hs_party', ['OrganizationEmail'])

        # Adding model 'OrganizationLocation'
        db.create_table(u'hs_party_organizationlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('address_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.AddressType'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mail_addresses', null=True, to=orm['hs_party.Organization'])),
        ))
        db.send_create_signal('hs_party', ['OrganizationLocation'])

        # Adding model 'OrganizationPhone'
        db.create_table(u'hs_party_organizationphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('phone_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.PhoneType'], blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='phone_numbers', null=True, to=orm['hs_party.Organization'])),
        ))
        db.send_create_signal('hs_party', ['OrganizationPhone'])

        # Adding model 'OrganizationNames'
        db.create_table(u'hs_party_organizationnames', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('phone_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.PhoneType'], blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='alternate_names', null=True, to=orm['hs_party.Organization'])),
        ))
        db.send_create_signal('hs_party', ['OrganizationNames'])

        # Adding model 'ExternalOrgIdentifiers'
        db.create_table(u'hs_party_externalorgidentifiers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='externalIdentifiers', to=orm['hs_party.Organization'])),
            ('identifierName', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.ExternalIdentifierType'], max_length='10')),
            ('otherName', self.gf('django.db.models.fields.CharField')(max_length='255', blank=True)),
            ('identifierCode', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('hs_party', ['ExternalOrgIdentifiers'])

        # Adding model 'GroupModel'
        db.create_table(u'hs_party_groupmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uniqueCode', self.gf('django.db.models.fields.CharField')(default='04a37fa4-4954-405f-b7b1-bd009fa3e413', max_length=64)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length='255', blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('lastUpdate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('hs_party', ['GroupModel'])

        # Adding model 'OrganizationAssociation'
        db.create_table(u'hs_party_organizationassociation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('uniqueCode', self.gf('django.db.models.fields.CharField')(default='13fcd8a2-6089-4cd5-ba98-99416d59db96', max_length=64)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.Organization'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_party.Person'])),
            ('beginDate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('endDate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('jobTitle', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
            ('presentOrganization', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('hs_party', ['OrganizationAssociation'])

        # Adding model 'ChoiceType'
        db.create_table(u'hs_party_choicetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choiceType', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('hs_party', ['ChoiceType'])


    def backwards(self, orm):
        # Deleting model 'AddressType'
        db.delete_table(u'hs_party_addresstype')

        # Deleting model 'PhoneType'
        db.delete_table(u'hs_party_phonetype')

        # Deleting model 'EmailType'
        db.delete_table(u'hs_party_emailtype')

        # Deleting model 'City'
        db.delete_table(u'hs_party_city')

        # Deleting model 'Region'
        db.delete_table(u'hs_party_region')

        # Deleting model 'Country'
        db.delete_table(u'hs_party_country')

        # Deleting model 'ExternalIdentifierType'
        db.delete_table(u'hs_party_externalidentifiertype')

        # Deleting model 'Person'
        db.delete_table(u'hs_party_person')

        # Deleting model 'PersonEmail'
        db.delete_table(u'hs_party_personemail')

        # Deleting model 'PersonLocation'
        db.delete_table(u'hs_party_personlocation')

        # Deleting model 'PersonPhone'
        db.delete_table(u'hs_party_personphone')

        # Deleting model 'UserType'
        db.delete_table(u'hs_party_usertype')

        # Deleting model 'OtherNames'
        db.delete_table(u'hs_party_othernames')

        # Deleting model 'OrganizationType'
        db.delete_table(u'hs_party_organizationtype')

        # Deleting model 'Organization'
        db.delete_table(u'hs_party_organization')

        # Deleting model 'OrganizationEmail'
        db.delete_table(u'hs_party_organizationemail')

        # Deleting model 'OrganizationLocation'
        db.delete_table(u'hs_party_organizationlocation')

        # Deleting model 'OrganizationPhone'
        db.delete_table(u'hs_party_organizationphone')

        # Deleting model 'OrganizationNames'
        db.delete_table(u'hs_party_organizationnames')

        # Deleting model 'ExternalOrgIdentifiers'
        db.delete_table(u'hs_party_externalorgidentifiers')

        # Deleting model 'GroupModel'
        db.delete_table(u'hs_party_groupmodel')

        # Deleting model 'OrganizationAssociation'
        db.delete_table(u'hs_party_organizationassociation')

        # Deleting model 'ChoiceType'
        db.delete_table(u'hs_party_choicetype')


    models = {
        'hs_party.addresstype': {
            'Meta': {'object_name': 'AddressType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '24', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'hs_party.choicetype': {
            'Meta': {'object_name': 'ChoiceType'},
            'choiceType': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'hs_party.city': {
            'Meta': {'object_name': 'City'},
            'geonamesUrl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hs_party.country': {
            'Meta': {'object_name': 'Country'},
            'geonamesUrl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hs_party.emailtype': {
            'Meta': {'object_name': 'EmailType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '24', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'hs_party.externalidentifiertype': {
            'Meta': {'object_name': 'ExternalIdentifierType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '24', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'hs_party.externalorgidentifiers': {
            'Meta': {'object_name': 'ExternalOrgIdentifiers'},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifierCode': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'identifierName': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.ExternalIdentifierType']", 'max_length': "'10'"}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'externalIdentifiers'", 'to': "orm['hs_party.Organization']"}),
            'otherName': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        'hs_party.groupmodel': {
            'Meta': {'object_name': 'GroupModel'},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastUpdate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'uniqueCode': ('django.db.models.fields.CharField', [], {'default': "'2a6bca0b-ce2c-4211-a3df-4a3de97a2196'", 'max_length': '64'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        'hs_party.organization': {
            'Meta': {'object_name': 'Organization'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'businessAddress': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            'businessTelephone': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'lastUpdate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'logoUrl': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organizationType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.OrganizationType']"}),
            'parentOrganization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.Organization']", 'null': 'True', 'blank': 'True'}),
            'persons': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'organizations'", 'to': "orm['hs_party.Person']", 'through': "orm['hs_party.OrganizationAssociation']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            u'specialities_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'uniqueCode': ('django.db.models.fields.CharField', [], {'default': "'6b157862-a519-4d4c-ae4a-95f70c86bea0'", 'max_length': '64'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        'hs_party.organizationassociation': {
            'Meta': {'object_name': 'OrganizationAssociation'},
            'beginDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'endDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobTitle': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.Organization']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.Person']"}),
            'presentOrganization': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'uniqueCode': ('django.db.models.fields.CharField', [], {'default': "'28911f5f-115a-4dd5-87d9-8aa1ba0e0723'", 'max_length': '64'})
        },
        'hs_party.organizationemail': {
            'Meta': {'object_name': 'OrganizationEmail'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'email_addresses'", 'null': 'True', 'to': "orm['hs_party.Organization']"}),
            'phone_type': ('django.db.models.fields.related.ForeignKey', [], {'default': "'other'", 'to': "orm['hs_party.EmailType']", 'blank': 'True'})
        },
        'hs_party.organizationlocation': {
            'Meta': {'object_name': 'OrganizationLocation'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'address_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.AddressType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mail_addresses'", 'null': 'True', 'to': "orm['hs_party.Organization']"})
        },
        'hs_party.organizationnames': {
            'Meta': {'object_name': 'OrganizationNames'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'alternate_names'", 'null': 'True', 'to': "orm['hs_party.Organization']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'phone_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.PhoneType']", 'blank': 'True'})
        },
        'hs_party.organizationphone': {
            'Meta': {'object_name': 'OrganizationPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'phone_numbers'", 'null': 'True', 'to': "orm['hs_party.Organization']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'phone_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.PhoneType']", 'blank': 'True'})
        },
        'hs_party.organizationtype': {
            'Meta': {'object_name': 'OrganizationType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '24', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'hs_party.othernames': {
            'Meta': {'object_name': 'OtherNames'},
            'annotation': ('django.db.models.fields.CharField', [], {'default': "'citation'", 'max_length': "'10'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otherName': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'persons': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherNames'", 'to': "orm['hs_party.Person']"})
        },
        'hs_party.person': {
            'Meta': {'object_name': 'Person'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'familyName': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'givenName': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'jobTitle': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'lastUpdate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'primaryAddress': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            'primaryOrganizationName': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            'primaryOrganizationRecord': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['hs_party.Organization']"}),
            'primaryTelephone': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'uniqueCode': ('django.db.models.fields.CharField', [], {'default': "'b3c32336-fa3f-4424-87f2-380a882378b2'", 'max_length': '64'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        'hs_party.personemail': {
            'Meta': {'object_name': 'PersonEmail'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'email_addresses'", 'null': 'True', 'to': "orm['hs_party.Person']"}),
            'phone_type': ('django.db.models.fields.related.ForeignKey', [], {'default': "'other'", 'to': "orm['hs_party.EmailType']", 'blank': 'True'})
        },
        'hs_party.personlocation': {
            'Meta': {'object_name': 'PersonLocation'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'address_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.AddressType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mail_addresses'", 'null': 'True', 'to': "orm['hs_party.Person']"})
        },
        'hs_party.personphone': {
            'Meta': {'object_name': 'PersonPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'phone_numbers'", 'null': 'True', 'to': "orm['hs_party.Person']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'phone_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hs_party.PhoneType']", 'blank': 'True'})
        },
        'hs_party.phonetype': {
            'Meta': {'object_name': 'PhoneType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '24', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'hs_party.region': {
            'Meta': {'object_name': 'Region'},
            'geonamesUrl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hs_party.usertype': {
            'Meta': {'object_name': 'UserType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '24', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hs_party']
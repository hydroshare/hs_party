from tastypie.api import Api
from tastypie import fields
from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, SessionAuthentication, MultiAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie.constants import ALL

from ..models.party import Party
from ..models.person import Person
from ..models.organization import Organization

__author__ = 'valentin'

v1_api = Api(api_name='v1')

class PersonResource(ModelResource):
    class Meta:
        always_return_data = True
        queryset = Person.objects.all()
        resource_name = 'person'
        excludes = ['createdDate', 'updatedDate', 'is_staff', 'is_superuser']
        filtering = {
            'name': ALL,
        }
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication(), SessionAuthentication())
        # make it so only superusers and people with express permission can modify / create user objects
        authorization = DjangoAuthorization()

v1_api.register(PersonResource())

class OrganizationResource(ModelResource):
    class Meta:
        always_return_data = True
        queryset = Organization.objects.all()
        resource_name = 'organization'
        excludes = ['createdDate', 'updatedDate', 'is_staff', 'is_superuser']
        filtering = {
            'name': ALL,
        }
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication(), SessionAuthentication())
        # make it so only superusers and people with express permission can modify / create user objects
        authorization = DjangoAuthorization()

v1_api.register(OrganizationResource())


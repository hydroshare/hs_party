from tastypie.api import Api,NamespacedApi
from tastypie import fields
from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, SessionAuthentication, MultiAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from django.conf.urls import url

from .models.party import Party
from .models.person import Person
from .models.organization import Organization,OrganizationCodeList

from .serializers.person import PersonFoafSerializer
from .serializers.organization import OrganizationFFoafSerializer

__author__ = 'valentin'

#party_v1_api = NamespacedApi(api_name='v1',urlconf_namespace='party')
party_v1_api = Api(api_name='v1')

class PersonResource(ModelResource):
    class Meta:
        always_return_data = True
        queryset = Person.objects.all()
        resource_name = 'person'
        serializer=PersonFoafSerializer()
        #excludes = ['createdDate', 'lastUpdate']
        #filtering = {
        #    'name': ALL,
        #}
        #authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication(), SessionAuthentication())
        # make it so only superusers and people with express permission can modify / create user objects
        #authorization = DjangoAuthorization()


    pass

party_v1_api.register(PersonResource())

class OrganizationResource(ModelResource):
    class Meta:
        always_return_data = True
        queryset = Organization.objects.all()
        resource_name = 'organization'
        serializer=OrganizationFFoafSerializer()
        excludes = ['createdDate', 'lastUpdate']
        filtering = {
            'name': ALL,
        }
        #authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication(), SessionAuthentication())
        # make it so only superusers and people with express permission can modify / create user objects
        #authorization = DjangoAuthorization()

    pass

party_v1_api.register(OrganizationResource())

class OrganizationalCodeListResource(ModelResource):
    class Meta:
        always_return_data = True
        queryset = OrganizationCodeList.objects.all()
        resource_name = 'organization_types'
        filtering = {
            'name': ALL,
        }
        #authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication(), SessionAuthentication())
        # make it so only superusers and people with express permission can modify / create group objects
        #authorization = DjangoAuthorization()

    # def prepend_urls(self):
    #     return [
    #         url(r"^(?P<resource_name>%s)/(?P<pk>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
    #     ]

party_v1_api.register(OrganizationalCodeListResource())
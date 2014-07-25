from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import ExternalOrgIdentifiers, OtherNames,ExternalIdentifierType, Organization,OrganizationType

__author__ = 'valentin'


class testExternalOrgIdentifiers(TestCase):
    fixtures =['initial_data.json']

    def setUp(self):
        self.idName = ExternalIdentifierType.objects.get(code='other')
        idName2 = ExternalIdentifierType.objects.get(code='twitter')
        self.orgType = OrganizationType.objects.get(code="other")
        self.orgname = 'org1'
        self.identifierCode = "testExternalOrg"
        self.org = Organization.objects.create(name=self.orgname, organizationType = self.orgType)
        ExternalOrgIdentifiers.objects.create(identifierCode = self.identifierCode,
              identifierName = self.idName, organization = self.org)

        ExternalOrgIdentifiers.objects.create(identifierCode = "testExternalOrg2",
       identifierName = idName2, organization = self.org
        )


    def test_ExternalOrgIdentifiers(self):
        """just a quick test to learn testing"""
        extorg1 = ExternalOrgIdentifiers.objects.get(identifierCode=self.identifierCode)
        self.assertEqual(extorg1.organization.name, self.org.name)
        self.assertEqual(extorg1.identifierCode, self.identifierCode)
        self.assertIsNotNone(extorg1.createdDate)







from __future__ import absolute_import
from django.test import TestCase
from django.utils.unittest import skipUnless
from django.core.urlresolvers import reverse,resolve,reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User,Group
#from django_webtest import WebTest
from ..models import Organization, Person,OrgAssociations, ExternalOrgIdentifiers,ScholarGroup,OrganizationType
from datetime import date
from django.test.utils import override_settings

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from mezzanine.conf import settings

__author__ = 'valentin'

@skipUnless("hs_scholar_profile" in settings.INSTALLED_APPS,"hs_scholar_profile must be installed" )
class UserOrgViewTests(TestCase):
    fixtures =['initial_data.json', 'group_data.json']
    # should be able to do this, but
    # issue: need to override base page or you see this error
    #  NoReverseMatch: Reverse for 'blog_post_feed'
    #urls = 'hs_scholar_profile.urls'

    def setUp(self):
        otherChoice = OrganizationType.objects.get(code='other')
        self.aPerson = Person.objects.create(givenName="last", familyName="first", name="last first")
        self.org2 = Organization.objects.create(name="org2",organizationType=otherChoice)
        self.u1 = User.objects.create(username='user1',email='me@example.com')
        self.u1p = self.u1.get_profile()
        self.u1p.uniqueCode="ab"
        self.u1p.givenName="first"
        self.u1p.familyName="last"
        self.u1p.name="First Last"
        self.u1p.jobTitle="job"


        self.u1p.save()
        #scholar = Scholar.objects.create(uniqueCode="ab",givenName="first", familyName="last", name="First Last",
        #                                 userType=UserDemographics.USER_TYPES_CHOICES[1],jobTitle="job")
        agroup = Group.objects.create(name="ResearchGroup")
        self.rGroup = ScholarGroup.objects.create(name="ResearchGroup",group=agroup,createdBy=self.u1p)
        #ScholarGroupAssociations.objects.create(scholar=u1p,scholargroup=rGroup, beginDate=date(2013,01,10))
        self.rGroup.group.user_set.add(self.u1)

    @override_settings(TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner')
    def test_list_views(self):
        plist = reverse("person_list")
        response = self.client.get(plist)
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("organization_list"))
        self.assertEqual(response.status_code, 200)
        #response = self.client.get(reverse("ScholarGroupList"))
        #self.assertEqual(response.status_code, 200)

    def test_detail_views(self):
        response = self.client.get(reverse("person_detail", args=[ self.aPerson.id] ) )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("organization_detail", args=[  self.org2.id] ) )
        self.assertEqual(response.status_code, 200)
        #response = self.client.get(reverse("ScholarGroupDetail", args=[  self.rGroup.id] ) )
        #self.assertEqual(response.status_code, 200)

# tried:  resolve....)
    # people, /people, /people/
    # party/people, /party/people
    # hs_user_org:people
    # def test_urls(self):
    #     response = self.client.get(resolve('hs_user_org:people'))
    #     self.assertEqual(response.status_code, 200)

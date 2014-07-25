from django.test import TestCase
from django.contrib.auth import get_user_model
#from django_webtest import WebTest
from ..models.organization import Organization
from ..models.person import Person, OtherNames,UserType
from django.core.exceptions import ObjectDoesNotExist,ValidationError



__author__ = 'valentin'


class PersonTest(TestCase):
    fixtures =['initial_data.json']

    def setUp(self):
        otherChoice = UserType.objects.get(code='other')
        Person.objects.create(givenName="first", familyName="last", name="First Last")
        aPerson = Person.objects.create(givenName="last", familyName="first", name="last first")
        bPerson = Person.objects.create(givenName="1", familyName="2")
        OtherNames.objects.create(persons=aPerson, otherName="abcd", annotation="other")
        OtherNames.objects.create(persons=aPerson, otherName="def", annotation="other")

    def test_Person(self):
        person1 = Person.objects.get(familyName="last")

        self.assertEqual(person1.otherNames.count(), 0)

        person2 = Person.objects.get(familyName="first")
        self.assertEqual(person2.otherNames.count(),2)
        self.assertEquals(person2.otherNames.get(otherName='def').annotation, 'other')
        self.assertIsNotNone(person2.uniqueCode)
        print("uuid:" + person2.uniqueCode)


    def test_otherNames(self):
        person1 = Person.objects.get(familyName="last")
        person2 = Person.objects.get(familyName="first")
        self.assertEqual(person1.otherNames.count(), 0)
        self.assertEqual(person2.otherNames.count(), 2)

    def test_name(self):
        person1 = Person.objects.get(familyName='2')
        self.assertEqual(person1.name, '1 2')

    def test_dupecheck(self):
        person1 = Person(familyName='2', givenName='1')
        person2 = Person(familyName='2', givenName='1', name='dummy name')
        person2.save() # no error
        with self.assertRaises(ValidationError):
           #person1.validate_unique()
           person1.save() # should be an error




pass
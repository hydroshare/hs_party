from django.test import TestCase
from django.contrib.auth import get_user_model
#from django_webtest import WebTest
from ..models.organization import Organization
from ..models.person import Person, OtherName,UserCodeList,PersonEmail,PersonPhone,PersonLocation
from ..models.party_types import NameAliasCodeList
from django.core.exceptions import ObjectDoesNotExist,ValidationError



__author__ = 'valentin'
FIRST1='first'
FIRST2='me'

LAST1='last'
LAST2='You'

NAME1="{0} {1}".format(FIRST1, LAST1)
NAME2="{0} {1}".format( FIRST2, LAST2)

ALTNAME1='Alt 1'
ALTNAME2='Alt2'

def otherNameAliasType():
   return NameAliasCodeList.objects.get(name='other')

def PersonCore():
    return Person(givenName=FIRST1, familyName=LAST1, name=NAME1)


def PersonBasic():
    aPerson = Person(givenName=FIRST2, familyName=LAST2, name=NAME2)
    aPerson.save()
    OtherName.objects.create(persons=aPerson, otherName=ALTNAME2, annotation=otherNameAliasType())
    OtherName.objects.create(persons=aPerson, otherName=ALTNAME1, annotation=otherNameAliasType())
    PersonEmail.objects.create(person=aPerson,email='me@example.com' )
    PersonPhone.objects.create(person=aPerson,phone_number="1234567890" )
    PersonLocation.objects.create(person=aPerson,address="somestreet address" )
    return aPerson

def PersonOne():
    aPerson = PersonCore().save()
    return aPerson

def PersonTwo():
    aPerson = PersonBasic()

    return aPerson

def PersonUnsavedDupe():
    aPerson = Person(givenName=FIRST2, familyName=LAST2, name=NAME2)

    return aPerson

# courtesy method for other classes
def AddPeople():
    return {PersonOne(),
    PersonTwo()}



class PersonTest(TestCase):
    fixtures =['initial_data.json']

    def setUp(self):

        self.person1=PersonOne()

        self.person2= PersonTwo()



    def test_Person(self):
        person1 = Person.objects.get(familyName=LAST1)

        self.assertEqual(person1.otherNames.count(), 0)

        person2 = Person.objects.get(familyName=LAST2)
        self.assertEqual(person2.otherNames.count(),2)
        self.assertEquals(person2.otherNames.get(otherName=ALTNAME1).annotation.name, 'other')
        self.assertIsNotNone(person2.uniqueCode)
        print("uuid:" + person2.uniqueCode)


    def test_otherNames(self):
        person1 = Person.objects.get(familyName=LAST1)
        person2 = Person.objects.get(familyName=LAST2)
        self.assertEqual(person1.otherNames.count(), 0)
        self.assertEqual(person2.otherNames.count(), 2)

    def test_name(self):
        person1 = Person.objects.get(familyName=LAST1)
        self.assertEqual(person1.name, NAME1)

    def test_dupecheck(self):
        person1 = Person(familyName=LAST1, givenName=FIRST1,name="Different Display Name")
        person2 = PersonUnsavedDupe()
        person1.save() # no error, diff display naame
        with self.assertRaises(ValidationError):
           #person1.validate_unique()
           person2.save() # should be an error




pass
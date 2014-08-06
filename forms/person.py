__author__ = 'valentin'
#from mezzanine.forms.models import Form
from django.forms import ModelForm, Textarea
from django import forms
from django.forms.models import inlineformset_factory

from ..models.organization import Organization
from ..models.person import Person,PersonLocation,PersonExternalIdentifier,\
    PersonPhone,PersonEmail,OtherName
from ..models.organization_association import OrganizationAssociation

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


# intial form
class PersonEditorForm(ModelForm):


    class Meta:
        model = Person
        fields = ( 'name','givenName','familyName','primaryOrganizationRecord',
                   'jobTitle','notes','url',
        #           'primaryAddress',"primaryTelephone"
        )
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 6}),
        }
        labels = {
            'notes': _('Short Bio'),
            'name': _('Full Name of Person (must be unique)'),
            'primaryOrganizationRecord': _('Select Primary Organization'),
        }
        help_texts = {
            'notes': _('Short Biography discussing you work and interests.'),
            'name': _('Full Name of Person that will be displayed on the site. Must be unique.'),
        }

    pass

LocationFormSet = inlineformset_factory(
    Person,
    PersonLocation,
    extra=2,)
EmailFormSet = inlineformset_factory(
    Person,
    PersonEmail,
    extra=2,)
PhoneFormSet = inlineformset_factory(
    Person,
    PersonPhone,
    extra=2,)
NameFormSet = inlineformset_factory(
    Person,
    OtherName,
    extra=2,)
IdentifierFormSet = inlineformset_factory(
    Person,
    PersonExternalIdentifier,
    extra=2,)

OrgAssociationsFormSet = inlineformset_factory(
    Person,
    OrganizationAssociation,
    extra=2)
#
# class PersonForm(ModelForm):
#     class Meta:
#         model = Person
#         fields ={"givenName","familyName","name",}
#
#     pass
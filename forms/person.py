__author__ = 'valentin'
#from mezzanine.forms.models import Form
from django.forms import ModelForm, Textarea
from django import forms
from django.forms.models import inlineformset_factory

from ..models.organization import Organization
from ..models.person import Person
from ..models.organization_association import OrganizationAssociation

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


# intial form
class PersonEditorForm(ModelForm):
    OrgAssociationsFormSet = inlineformset_factory(
        Person,
        OrganizationAssociation,
        extra=2)
    
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


#
# class PersonForm(ModelForm):
#     class Meta:
#         model = Person
#         fields ={"givenName","familyName","name",}
#
#     pass
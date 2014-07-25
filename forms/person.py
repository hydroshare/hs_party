__author__ = 'valentin'
#from mezzanine.forms.models import Form
from django.forms import ModelForm, Textarea
from django import forms
from django.forms.models import inlineformset_factory

from ..models import Scholar,Organization,OrgAssociations,Person,PersonLocation
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


# intial form
class PersonEditorForm(ModelForm):
    OrgAssociationsFormSet = inlineformset_factory(
        Person,
        OrgAssociations,
        )
    class Meta:
        model = Person
        fields = ( 'givenName','familyName','name','jobTitle','notes')
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 6}),
        }
        labels = {
            'notes': _('Short Bio'),
        }
        help_texts = {
            'notes': _('Short Biography discussing you work and interests.'),
        }

    pass


#
# class PersonForm(ModelForm):
#     class Meta:
#         model = Person
#         fields ={"givenName","familyName","name",}
#
#     pass
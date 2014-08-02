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
class OrganizationEditorForm(ModelForm):

    class Meta:
        model = Organization
        fields = ["name","organizationType","specialities","logoUrl",
           #   "businessAddress","businessTelephone",
              "logoUrl","notes","parentOrganization"]
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 6}),
        }
        labels = {
            'notes': _('Short Organization Description'),
        }
        help_texts = {
            'notes': _('Short Organization Description.'),
        }

    pass
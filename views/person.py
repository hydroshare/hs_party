__author__ = 'valentin'

from django.views.generic import ListView,DetailView,TemplateView,UpdateView,CreateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from ..models.person import Person
from ..models.organization import Organization
from ..models.organization_association import OrganizationAssociation
from django.forms.models import inlineformset_factory


from ..forms.person import PersonEditorForm

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
#from ..forms import ScholarForm,ScholarProfileForm,OrgAssociationsForm




class PersonList(ListView):
    model = Person
    #template_name = "pages/person/person_list.html"
    queryset = Person.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

#@login_required
class PersonCreate(CreateView):
    model = Person
    template_name = "pages/person/person_create.html"
    fields = ["name",'givenName','familyName',
             'primaryOrganizationRecord',
            # 'primaryAddress',
              'notes']

#@login_required
class PersonEdit(UpdateView):
    model = Person
    #template_name = "pages/person/person_edit.html"
    form_class = PersonEditorForm

    OrgAssociationsFormSet = inlineformset_factory(
        Person,
        OrganizationAssociation
        )
    pass

class PersonDetail(DetailView):
    model = Person
    queryset = Person.objects.all()
    #template_name = "pages/person/person.html"

    def get_context_data(self, **kwargs):
        context = super(PersonDetail, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

    def get_object(self,**kwargs):
        # Call the superclass
        object = super(PersonDetail, self).get_object(**kwargs)
        # Record the last accessed date
        #object.last_accessed = timezone.now()
        #object.save()
        # Return the object
        return object


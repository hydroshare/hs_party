__author__ = 'valentin'

from django.views.generic import ListView,DetailView,TemplateView,UpdateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf

from ..models import Person,Organization,ScholarGroup,PersonModel,Scholar,OrgAssociations
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
#from ..forms import ScholarForm,ScholarProfileForm,OrgAssociationsForm
from .. import forms



class PersonList(ListView):
    model = PersonModel
    template_name = "pages/person/person_list.html"
    queryset = Person.objects.all()
    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context


class PersonDetail(DetailView):
    model = Person
    queryset = Person.objects.all()
    template_name = "pages/person/person.html"

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

class PersonEdit(UpdateView):
    model = Person
    template_name = "pages/person/person_edit.html"
    pass
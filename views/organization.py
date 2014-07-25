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

class OrganizationList(ListView):
    model = Organization
    template_name = "pages/orgs/organization_list.html"

    def get_context_data(self, **kwargs):
        context = super(OrganizationList, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

class OrganizationEdit(UpdateView):
    model = Organization
    template_name = "pages/orgs/organization_edit.html"

class OrganizationDetail(DetailView):
    model = Organization
    queryset = Organization.objects.all()
    template_name = "pages/orgs/organization.html"

    def get_context_data(self, **kwargs):
        context = super(OrganizationDetail, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

    def get_object(self,**kwargs):
        # Call the superclass
        object = super(OrganizationDetail, self).get_object(**kwargs)
        # Record the last accessed date
        #object.last_accessed = timezone.now()
        #object.save()
        # Return the object
        return object
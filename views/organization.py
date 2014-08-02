from django.views.generic import ListView,DetailView,TemplateView,UpdateView,CreateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from ..models.person import Person
from ..models.organization import Organization

from ..forms.organization import OrganizationEditorForm

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



class OrganizationList(ListView):
    model = Organization
    template_name = "pages/orgs/organization_list.html"

    def get_context_data(self, **kwargs):
        context = super(OrganizationList, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

#@login_required
class OrganizationEdit(UpdateView):
    model = Organization
    template_name = "pages/orgs/organization_edit.html"
    form_class = OrganizationEditorForm

#@login_required
class OrganizationCreate(CreateView):
    model = Organization
    template_name = "pages/orgs/organization_create.html"
    fields = ["name","organizationType","specialities","logoUrl",
    #          "businessAddress","businessTelephone",
              "logoUrl","notes","parentOrganization"]

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
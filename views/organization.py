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

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        location_form = OrganizationEditorForm.LocationFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  location_form=location_form,
                                  )
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        location_form = OrganizationEditorForm.LocationFormSet(self.request.POST)
        if (form.is_valid() and location_form.is_valid()):
            return self.form_valid(form, location_form)
        else:
            return self.form_invalid(form, location_form)

    def form_valid(self, form, location_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        location_form.instance = self.object
        location_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, location_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  location_form=location_form))

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
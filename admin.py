from copy import deepcopy
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import DisplayableAdmin, TabularDynamicInlineAdmin, OwnableAdmin,StackedDynamicInlineAdmin
from django.contrib import admin
from django.contrib.admin import ModelAdmin,StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from .models import *

class PersonInline(admin.TabularInline):
    model = Person


#####
# Org
# #####
#person_extra_fieldsets = ((None, {"fields": ("dob",)}),)

class OrgInline (admin.StackedInline):
    model = Organization
    list_display = ('name',"organizationType")


class PersonAssociationInline(StackedDynamicInlineAdmin):
    model = Organization.persons.through
    extra = 0
#    inlines = (OrgInline)

class OrganizationTypeInline(admin.TabularInline):
    model = OrganizationType
    list_display = ('code',"name")

#class OrganizationAdmin( ModelAdmin):
class OrganizationAdmin(DisplayableAdmin):
    model = Organization
    search_fields = ['name',]
    readonly_fields = ["uniqueCode",]
    #inlines = (OrganizationTypeInline,PersonAssociationInline)
    #inlines = (PersonAssociationInline,)
    list_display = ("id","name","organizationType")
    list_display_links = ("id",)
    list_editable = ()
    ordering = ("name",)
    fieldsets = (
       (None, {
           "fields": ("uniqueCode","name","organizationType","parentOrganization","url"),
               }),
        ("Advanced", {
           "fields": ("specialities","notes",),
               }),
   )

    #fieldsets = deepcopy(PageAdmin.fieldsets) #+ person_extra_fieldsets
    pass



class UserTypeInline(admin.TabularInline):
    model = UserType
    list_display = ('code',"name")

class PersonAdmin(DisplayableAdmin):
    model = Person
    search_fields = [ "name" , ]
    inlines = (PersonAssociationInline,)# OrgInline)
    list_display = ("id","name","primaryOrganizationRecord",)
    list_display_links = ("id",)
    list_editable = ()
    readonly_fields = ["uniqueCode",]
    ordering = ("name",)
    fieldsets = (
        (None, {
            "fields": ("uniqueCode","givenName","familyName","name","jobTitle","primaryOrganizationRecord",),
                }),
        ("Contact", {
           "fields": ("primaryAddress","primaryTelephone"),
               }),
        ("Personal", {
           "fields": ("url","notes",),
               }),
    )
    #filter_horizontal = ('organizations',)
    pass

admin.site.register(Organization, OrganizationAdmin)

admin.site.register(Person, PersonAdmin)


admin.site.register(OrganizationAssociation)

admin.site.register(UserType)
admin.site.register(OrganizationType)
admin.site.register(PhoneType)
admin.site.register(AddressType)
admin.site.register(EmailType)
admin.site.register(ExternalIdentifierType)



class GroupInlineAdmin(admin.TabularInline):
    model = Group



class PersonInline(admin.TabularInline):
    model = Person
    list_display = ('name',"familyName","givenName",)






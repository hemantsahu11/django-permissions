from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Product
from guardian.admin import GuardedModelAdmin
# Register your models here.


# admin.site.register(Product)
# admin.site.unregister(User)   # by unregistering the user and group will  not be available on the admin site
# admin.site.unregister(Group)

# class ReadOnlyAdminMixin:              we can set permission by using this class also then we will pass this class to ProductAdmin and permissions will be overridden
#     def has_view_permission(self, request, obj=None):
#         return False
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name']    # we dont want to staff member to update the name
#
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#
#         if not is_superuser:
#             form.base_fields['name'].disabled = True
#         return form
#
#     #from here also we can modify permissions by overriding previously available methods
#     def has_add_permission(self, request):     # by this user will not be able to add the products
#         return False                 # to allow user to change return True
#
#     def has_change_permission(self, request, obj=None):  # by this user will not be able to change the content of product
#         if request.user.has_perm('inventory.change_product'):
#             return True
#         else:
#             return False
#
#     def has_view_permission(self, request, obj=None):
#         return True




"""    Object level permissions begins from here   """


@admin.register(Product)
class ProductAdmin(GuardedModelAdmin):
    list_display = ('name', )

    def has_module_permission(self, request):
        if super().has_module_permission(request):  # if user has access to view any of the object then we will show product table at users console
            return True                             # by returning true Product will be displayed on users end

    def get_queryset(self, request):
        return super().get_queryset(request)

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


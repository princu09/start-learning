# Custom User Create
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Import Models
from .models import UserManage , Chapter , Comment

class CustomData(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = UserManage
    list_display = ['id', 'email', 'username', 'first_name', 'last_name']

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'fieldName', 'mobile', 'dob' , 'userImg',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('fieldName', 'mobile', 'dob', 'userImg',)}),)


admin.site.register(UserManage, CustomData)
admin.site.register(Chapter)
admin.site.register(Comment)
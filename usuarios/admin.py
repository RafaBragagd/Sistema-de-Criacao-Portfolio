from pyexpat import model
from django.contrib import admin
from django.contrib.auth import admin as authAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

# Register your models here.
@admin.register(User)
class UserAdmin(authAdmin.UserAdmin):
    form        = UserChangeForm
    add_form    = UserCreationForm
    model       = User
    fieldsets   = authAdmin.UserAdmin.fieldsets + (
        ("Campo personalizados", {"fields": ("abstract","numberFone", "Address",)}),
    )
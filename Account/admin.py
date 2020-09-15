from django.contrib import admin
from django.contrib.auth.models import Group
from allauth.account.models import EmailAddress
from Account.models import Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(Account)
class AccountAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'is_author', 'is_superuser')
    list_filter = ('is_author',)
    fieldsets = (
        ('Account Profile', {'fields': ('email', 'username', 'is_author', 'is_superuser','password')}),
        ('Account Status', {'fields': ('is_active',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_author', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('is_author',)            
    filter_horizontal = ()

admin.site.unregister(Group)
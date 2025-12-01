from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import UserProfile

# Inline profile inside the User admin page
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

# Extend the default UserAdmin to include the profile inline and show email
class CustomUserAdmin(DjangoUserAdmin):
    inlines = (UserProfileInline,)
    # columns shown on the user list page in admin
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_superuser')
    list_select_related = ('userprofile',)

    def phone(self, obj):
        # safe access to related profile
        return getattr(obj.userprofile, 'phone', '')
    phone.short_description = 'Phone'

    # If you want the phone to appear in the list_display, uncomment:
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active', 'is_superuser')

# Unregister the default User admin and register our extended one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Also register UserProfile separately (optional)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'phone', 'user__email')

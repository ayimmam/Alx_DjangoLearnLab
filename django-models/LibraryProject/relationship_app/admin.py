from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Author, Library, Librarian, UserProfile

class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for the CustomUser model.
    """
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),)

# Register models with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
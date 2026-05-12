from django.contrib import admin
from .models import Visit, Contact, Project
from martor.admin import MartorModelAdmin # Ensure correct import path

@admin.register(Project)
class ProjectAdmin(MartorModelAdmin):
    # MartorModelAdmin automatically overrides TextField widgets
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'tags')

    class Media:
        css = {
            'all': ('admin_fix.css',)
        }

# Standard registrations
admin.site.register(Contact)
admin.site.register(Visit)
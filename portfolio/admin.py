from django.contrib import admin
from .models import Visit, Contact, Project
from django import forms
from martor.widgets import AdminMartorWidget

class ProjectAdminForm(forms.ModelForm):
    markdown_content = forms.CharField(widget=AdminMartorWidget())

    class Meta:
        model = Project
        fields = '__all__'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'tags')


admin.site.register(Contact)
admin.site.register(Visit)
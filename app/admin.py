from django.contrib import admin

from app.models import Author, JobPost, Location, Skill

class JobAdmin(admin.ModelAdmin):
    # list_display = ('__str__', 'title', 'description', 'date', 'expiry', 'salary','slug')
    # list_filter = ('date', 'expiry', 'salary')
    # search_fields = ('title', 'description')
    # fields = (('title', 'description','salary', 'slug'), 'expiry') # Control fields options and grouping
    # exclude = ('date',)
    fieldsets = (
        ('सामान्य जानकारी', {
            'fields': ('title', 'description')
        }),
# use of inbuild css classes
        ('थप जानकारी', {
            'classes': ('collapse',),
            'fields': (('expiry', 'salary','skills'), 'slug', 'location','author', 'type'),
        }),
    )

# Register your models here. 
admin.site.register(JobPost, JobAdmin)  
admin.site.register(Location)  
admin.site.register(Author)  
admin.site.register(Skill) 

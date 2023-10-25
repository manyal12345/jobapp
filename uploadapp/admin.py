from django.contrib import admin

from uploadapp.models import UploadFile, Uploads

# Register your models herer
admin.site.register(Uploads)
admin.site.register(UploadFile)
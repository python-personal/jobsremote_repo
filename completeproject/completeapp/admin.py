from django.contrib import admin
from completeapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

admin.site.register(Student,StudentAdmin)

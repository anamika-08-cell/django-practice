from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(StudentID)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id","student_name","student_email","student_age","department","student_address")
    list_filter = ('student_name','student_age')
    search_fields = ('student_name','student_email')

@admin.register(Recipe)
class Checkrecipe(admin.ModelAdmin):
    list_display = ('recipe_name','recipe_description','recipe_image')
    list_filter = ('recipe_name',)
    search_fields = ('recipe_name','recipe_description','recipe_image')
 
 
 
class Showdata(admin.TabularInline):
    model = Student
    extra = 1

@admin.register(Department)
class Dept(admin.ModelAdmin):
    inlines = [Showdata]

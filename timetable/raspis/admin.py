from django.contrib import admin

from .models import Group, Discipline, Teacher, Audience, Lesson


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'letter', 'count')
    list_display_links = ('id',)
    search_fields = ('name', 'letter')
    list_editable = ('name', 'letter', 'count')
    list_filter = ('name', 'letter', 'count')

class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_editable = ('name',)
    list_filter = ('name',)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_editable = ('name',)
    list_filter = ('name',)

class AudienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_filter = ('name',)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'name', 'letter', 'para', 'date', 'category', 'office')
    list_display_links = ('id', 'group',)
    search_fields = ('group', 'name',)
    list_editable = ('name', 'letter', 'para', 'date', 'category', 'office')
    list_filter = ('group', 'name', 'letter', 'para', 'date', 'category', 'office')

admin.site.register(Group, GroupAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Audience, AudienceAdmin)
admin.site.register(Lesson, LessonAdmin)
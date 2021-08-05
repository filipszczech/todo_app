from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    model = Task

    list_display = ('id', 'title', 'completed',)

    fieldsets = (('Task', {'fields': ('title', 'completed'),}),)


admin.site.register(Task, TaskAdmin)

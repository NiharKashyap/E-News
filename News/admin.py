from django.contrib import admin

from .models import News, BookMarks
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    fields = ['title','body', 'posted']
    list_display = ['title', 'posted']


class BookMarksAdmin(admin.ModelAdmin):
    fields = ['user', 'news']
    list_display = ['user', 'news']

admin.site.register(News, NewsAdmin)
admin.site.register(BookMarks, BookMarksAdmin)
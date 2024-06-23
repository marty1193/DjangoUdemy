from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('rating',)
    list_filter = ('rating',)
    list_display =('title','rating','aurthor')

admin.site.register(Book, BookAdmin)

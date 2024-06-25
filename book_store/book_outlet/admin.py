from django.contrib import admin
from .models import Book, Aurthor

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ('rating',)
    list_display =('title','rating','aurthor')

class AurthorAdmin(admin.ModelAdmin):

    #list_filter = ('aurthor',)
    list_display =('first_name', 'last_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Aurthor, AurthorAdmin)

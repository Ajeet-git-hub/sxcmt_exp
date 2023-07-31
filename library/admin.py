from django.contrib import admin
from library.models import Book, Student, Book_as_rt

# Register your models here.
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Book_as_rt)

from django.db import models
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length = 100)
    book_author = models.CharField(max_length = 100)
    book_publisher = models.CharField(max_length = 100)
    book_code = models.CharField(max_length = 15, unique = True)
    book_quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.book_title

class Student(models.Model):
    book_having = models.ManyToManyField(Book ,blank = True )
    stu_name = models.CharField(max_length = 40)
    stu_stream = models.CharField(max_length = 10)
    stu_roll = models.CharField(max_length = 15, unique = True)
    max_book = models.PositiveIntegerField(default = 3)
    def __str__(self):
        return self.stu_name
    
class Book_as_rt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(default = timezone.now())
    recovery_date = models.DateField(default = timezone.now()+timezone.timedelta(days=15))
    def __str__(self):
        return self.student.stu_name
    
    
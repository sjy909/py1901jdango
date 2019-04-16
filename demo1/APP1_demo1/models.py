from django.db import models

# Create your models here.


class Book_list(models.Model):
    book_name = models.CharField(max_length=20)
    book_pulish_date = models.DateField()


class Roles_list(models.Model):
    role_name = models.CharField(max_length=30)
    Roles_gerden = models.BooleanField()
    Roles_Book = models.ForeignKey("Book_list", on_delete=models.CASCADE)

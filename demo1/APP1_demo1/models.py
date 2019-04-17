from django.db import models

# Create your models here.


class Book_list(models.Model):
    book_name = models.CharField(max_length=20)
    book_pulish_date = models.DateField(auto_now=True)

    def bookName(self):
        return self.book_name

    def BookPublishDate(self):
        return self.book_pulish_date

    bookName.short_description = "书籍作者"
    BookPublishDate.short_description = "注册时间"


class Roles_list(models.Model):
    role_name = models.CharField(max_length=30)
    Roles_gerden = models.BooleanField()
    Roles_Book = models.ForeignKey("Book_list", on_delete=models.CASCADE)

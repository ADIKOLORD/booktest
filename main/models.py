from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    quantity = models.IntegerField(verbose_name="Количество")

    def __str__(self):
        return self.title


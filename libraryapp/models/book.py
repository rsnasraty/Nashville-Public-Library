from django.db import models

class Library(models.Model):

    Title = models.CharField(max_length=50),
    ISBN_Number = models.CharField(max_length=50),
    Author = models.CharField(max_length=50),
    Year_Published= models.IntegerField()

    class Book:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):

    Title = models.CharField(max_length=50),
    ISBN_Number = models.CharField(max_length=50),
    Author = models.CharField(max_length=50),
    Year_Published= models.IntegerField(),
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

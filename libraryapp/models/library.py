from django.db import models

class Library(models.Model):

    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

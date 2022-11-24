from django.db import models

class Functionalities(models.Model):

    name = models.CharField(

        max_length=100,
        null=False
    )

    description = models.TextField(

        max_length=500
    )
    def __str__(self):
        return f"{self.name}"

    class Meta():
        verbose_name_plural = "Functions"
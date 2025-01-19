from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

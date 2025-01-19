from django.db import models
from enrollments.models import Enrollment
from teachers.models import Teacher


class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True,
                                related_name='subjects')
    end_time = models.DateField(max_length=10)
    grade = models.PositiveIntegerField()
    semeseter = models.PositiveIntegerField()
    is_finished = models.BooleanField(default=False)
    enrollments = models.ManyToManyField(Enrollment, related_name='subjects')

    def __str__(self):
        return self.title

from django.db import models


class Enrollment(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE,
                                related_name='student_enrollments')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE,
                                related_name='subject_enrollments')
    grade = models.FloatField(null=True, blank=True)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enrollment: {self.student} in {self.subject}"

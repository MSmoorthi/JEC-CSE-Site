from django.db import models


from datetime import date


class Student(models.Model):
    roll_no = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128)
    dob: date = models.DateField()
    batch = models.PositiveIntegerField()
    photo = models.FileField(upload_to="students/photos", null=True)
    mail_id = models.CharField(max_length=1024, null=True)

    def __str__(self) -> str:
        return self.roll_no

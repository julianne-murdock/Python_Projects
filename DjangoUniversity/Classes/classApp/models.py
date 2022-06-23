from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=False, null=False)
    course_number = models.IntegerField(default=0, blank=False, null=False)
    instructor_name = models.CharField(max_length=60, default="")
    duration = models.FloatField(default=0, blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title



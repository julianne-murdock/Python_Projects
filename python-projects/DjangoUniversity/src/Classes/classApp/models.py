from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course = models.CharField(max_length=60)
    instructor = models.CharField(max_length=60)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title


Student_1 = djangoClasses.objects.update_or_create(Title="Economics", CourseNumber=201, Instructor="Chubaka Baka",
                                            Duration=1.5)
Student_2 = djangoClasses.objects.update_or_create(Title="ART", CourseNumber=301, Instructor="Indiana Jones",
                                            Duration=2.5)
Student_3 = djangoClasses.objects.update_or_create(Title="Sports", CourseNumber=401, Instructor="Davy Jones Locker",
                                            Duration=1.0)

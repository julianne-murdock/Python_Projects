from django.db import models

TYPE_CHOICES = {
	('appetizers','appetizers'),
	('entrees','entrees'),
	('desserts','desserts'),
	('drinks','drinks'),
}


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course = models.CharField(max_length=60)
    instructor = models.CharField(max_length=60)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title
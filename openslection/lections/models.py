from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Lection(models.Model):
    theme = models.CharField(max_length=256)
    description = models.TextField()
    group = models.CharField(max_length=64)
    subject = models.CharField(max_length=128)
    teacher = models.CharField(max_length=256)
    lecture_hall = models.IntegerField()
    date = models.DateField()
    image = models.ImageField(upload_to='lections_images')
    specialization = models.ForeignKey(to=Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return f'Ашық сабақ: {self.theme} | Мамандық: {self.specialization.name}'

from django.db import models

from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    href = models.URLField()
    time = models.IntegerField()
    product_id = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class ViewingHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time = models.IntegerField()
    status = models.BooleanField(
        default=False)

    def __str__(self):
        return f"{self.user_id} - {self.lesson_id}"

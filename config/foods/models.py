from django.db import models

# Create your models here.
class food_model(models.Model):
    name = models.TextField()
    color = models.TextField()
    class Meta:
        verbose_name_plural = 'food_Models'
    def __str__(self):
        return self.name
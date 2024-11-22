from django.db import models

# Create your models here.
class Author(models.Model):
    Name = models.CharField(max_length=50)
    Bio = models.TextField()
    phone_num = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.Name

from django.db import models
from atractions.models import Atraction
from comments.models import Comment
from reviews.models import Review
from address.models import Address

# Create your models here.

class TuristicPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    atractions = models.ManyToManyField(Atraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
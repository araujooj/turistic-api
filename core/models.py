from django.db import models
from atractions.models import Atraction
from comments.models import Comment
from reviews.models import Review
from address.models import Address


class TuristicPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    atractions = models.ManyToManyField(Atraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to='turistic', null=True, blank=True)
    
    @property
    def complete_description2(self):
        return '%s - %s' % (self.name, self.description)

    def __str__(self):
        return self.name

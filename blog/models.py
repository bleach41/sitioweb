from django.db import models

from django.db.models.fields import CharField, DateField
from django.db.models.fields.files import ImageField
import datetime


class Posts(models.Model):
    title = CharField(max_length=100)
    description = models.TextField()
    image = ImageField(upload_to="blog/images")
    date = DateField(datetime.date.today)

    # def __str__(self) -> str:
    #     return self.title

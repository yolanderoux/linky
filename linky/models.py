from django.db import models
from django.utils.text import slugify

# Create your models here.
class Link(models.Model):
    destination = models.URLField(max_length=200)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.title} | {self.clicks}"
    
    def click(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
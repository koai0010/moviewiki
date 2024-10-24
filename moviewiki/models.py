from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BaseModels(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True

class Genre(BaseModels):
    genre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.genre
    
class Poster(BaseModels):
    poster_path = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.poster_path
    
class Movie(BaseModels):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateField()
    background_path = models.CharField(max_length=300)
    genre = models.ManyToManyField(Genre)
    poster = models.ManyToManyField(Poster)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.title

from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from movies.models import Movies

class Review(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.PROTECT,related_name='reviews')
    star = models.IntegerField(
        validators=[
            MinValueValidator(0,'Avaliação mínima deve ser no máximo 0'),
            MaxValueValidator(5,'Avaliação máxima deve ser no máximo 5')
        ]
    )
    comment = models.TextField()


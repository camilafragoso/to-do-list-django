from re import T
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    #FIELDS OF THE MODEL
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>."
)
  
    dificulty_level_choices = [
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard')
    ]
    dificulty_level = models.CharField(
        max_length=6,
        choices=dificulty_level_choices,
        default='EASY',
        null=True, 
        blank=True
    )
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    #NAME OF THE MODEL
    def __str__(self):
        return self.title

    #ORDERING OF THE MODEL
    class Meta:
        ordering = ['created_at']
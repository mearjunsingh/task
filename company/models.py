from django.db import models
from django.contrib.auth import get_user_model

UserProfile = get_user_model()


class Task(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('inprogress', 'In Progress'),
        ('completed', 'Completed')
    )

    title = models.CharField(max_length=100)
    supervisor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='supervisor')
    intern = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='intern')
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.title
    

class Attandance(models.Model):
    intern = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.intern.username
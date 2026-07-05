from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class CodingChallenge(models.Model):
    Coding_Challenge_Choices = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='challenges/')
    date_added = models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=2, choices=Coding_Challenge_Choices)   

    description = models.TextField(default='No description provided.')

    def __str__(self):
        return self.name



# 1 to many relationship: One coding challenge can have multiple reviews
class CodingReview(models.Model):
    coding = models.ForeignKey(CodingChallenge, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.user.username} for {self.coding.name}'




# Many to many relationship: Users can bookmark multiple coding challenges
class UserBookmark(models.Model):
    user = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)
    coding_challenges = models.ManyToManyField(CodingChallenge, related_name='bookmarked_by')

    def __str__(self):
        return f'{self.user} bookmarked {self.difficulty}'    




# 1 to 1 relationship: Each coding challenge has one solution
class CodingSolution(models.Model):
    coding = models.OneToOneField(CodingChallenge, on_delete=models.CASCADE, related_name='solution')
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Ensures only one user can solve this challenge
    solution_text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Solution for {self.coding.name} by {self.user.username}'

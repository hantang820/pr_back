from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    prompt = models.CharField(max_length=512)
    response = models.TextField()

    def __str__(self):
        return f"{self.prompt}: {self.response}"
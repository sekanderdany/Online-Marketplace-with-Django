from django.contrib.auth.models import User
from django.db import models
from item.models import Item


class Conversation(models.Model):
    """Model representing a conversation."""

    item = models.ForeignKey(
        Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User, related_name='conversations')  # Fixed reference to User
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)  # Fixed ordering to be a tuple


class ConversationMessage(models.Model):
    """Model representing a message in a conversation."""

    conversation = models.ForeignKey(
        Conversation, related_name='messages', on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='created_messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages')

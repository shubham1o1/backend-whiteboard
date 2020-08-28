from django.db import models
import uuid 
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Boards(models.Model):
    idx = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    extras = models.JSONField()
    picture = models.ImageField(upload_to='notes_pic/')
    date_created = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.title

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime

# Create your models here.
class Comment(models.Model):
    title=models.CharField(max_length=40)
    body=RichTextUploadingField()
    created=models.DateTimeField(default=datetime.now)
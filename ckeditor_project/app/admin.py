from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display=['id','title','body','created']
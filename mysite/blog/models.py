from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=50)
    def __str__(self):
        return self.type_name
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, null=True)
    create_time = models.DateField(auto_now_add=True, null=True)
    last_change_time = models.DateField(auto_now=True, null=True)
    def __str__(self):
        return "<标题:%s"%self.title
    class Meta:
        ordering = ['-create_time']

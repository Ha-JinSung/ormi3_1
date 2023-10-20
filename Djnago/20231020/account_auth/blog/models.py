from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True) 
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True) # DB에는 경로만 지정되며 post.file_upload.url 이 경로이다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
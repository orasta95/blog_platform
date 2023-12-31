from django.db import models

class Post(models.Model):

    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=70)    
    description = models.TextField("Description", max_length=1024)
    date_time = models.DateField("Post date", null=True, blank=True)
    photo = models.ImageField("Photo", upload_to="photo", null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["title", "date_time"]

    def __str__(self) -> str:
        return self.title
from django.db import models


class Comment(models.Model):

    description = models.TextField("Add a comment", max_length=1024)
    date_time = models.DateField("Post date", null=True, blank=True)
    photo = models.ImageField("Photo", null=True, blank=True)
    post = models.ForeignKey("blog_platform.post",
                             related_name="comments", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["title", "date_time"]

    def __str__(self) -> str:
        return self.title

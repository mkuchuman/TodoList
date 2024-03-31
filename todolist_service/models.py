from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    tag = models.ManyToManyField(Tag, related_name="tasks", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ["is_done", "-created"]

    def __str__(self):
        return self.content

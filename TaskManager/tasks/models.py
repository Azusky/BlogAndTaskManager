from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    status = models.CharField(max_length=10)
    assign = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

# class Comment(models.Model):
#     text = models.TextField(default="test")
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

#     def save(self, *args, **kwargs):


#         super(Comment, self).save(*args, **kwargs)

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Log(models.Model):
    task = models.ForeignKey('Task', related_name='logs', on_delete=models.CASCADE)
    start_data = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    

    class Meta:
        ordering = ['start_data']

from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    title = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
	#	- user_id


    def __str__(self):
        return self.title;


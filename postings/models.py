from django.db import models
from django.conf import settings

class BlogUser(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    usernames = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=15)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.CharField(max_length=20, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.userid.username)



# Create your models here.
@property
def owner(self):
    return self.userid
from django.db import models
from login.models import User

class Topic(models.Model):
    #tags = models.ForeignKey(Tag, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_text = models.CharField(max_length=250)
    topic_desc=models.CharField(max_length=700,default="")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.topic_text


class Tag(models.Model):
    tag_name= models.CharField(max_length=50)
    tag_desc=models.CharField(max_length=500,default="")
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    def __str__(self):
        return self.tag_name

class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    opinion_text=models.CharField(max_length=500)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    foragainst=models.IntegerField(default=0) #for=1 against=0
    def __str__(self):
        return self.user.user_name

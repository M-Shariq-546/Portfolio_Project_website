from django.db import models
import uuid
from users_info.models import Profile


class Project(models.Model):
    owner = models.ForeignKey(Profile , blank=True , null=True , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg' , null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0 , null=True , blank=True)
    vote_ratio = models.IntegerField(default=0 , null=True, blank=True)
    demo_link = models.CharField(max_length=2000 , null=True , blank=True)
    source_link = models.CharField(max_length=2000 , null=True , blank=True)
    date_of_upload = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True, editable=False)
    #default=uuid.uuid4 ,
    def __str__(self):
        return self.title 
    
    class Meta:
        ordering = ['-vote_total', '-vote_ratio']
    
    
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upvote = reviews.filter(value='up').count() # same as aggregate in MYSQL
        totalVote = reviews.count()
        
        ratio = (upvote / totalVote) * 100
        self.vote_ratio = ratio
        self.vote_total = totalVote
        
        self.save()
        
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = 'default.jpg'
        return url  
    
     
class Review(models.Model):
    VOTE_TYPE = (
        ('up' , 'up vote'),
        ('down', 'down vote'),
    )
    owner = models.ForeignKey(Profile , on_delete=models.CASCADE , null=True)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    body = models.TextField(null=True ,blank=True)
    date_of_upload = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 ,unique=True, primary_key=True , editable=False)
    
    def __str__(self):
        return self.value
            
class Tag(models.Model):
    name = models.CharField(max_length=200)
    date_of_upload = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 ,unique=True, primary_key=True , editable=False)
    
    def __str__(self):
        return self.name
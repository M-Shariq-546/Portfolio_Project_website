from django.contrib.auth.models import User
from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from .models import Profile


    
def createProfile(sender , instance , created , **kwargs):
    print("Profile Created Signal Triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user= user,
            username= user.username,
            email= user.email,
            name= user.first_name ,
        )

#@receiver(post_delete, sender=Profile)
def deleteProfile(sender , instance , **kwargs):
    print("Profile Deleted Signal Triggered")
    user = instance.user
    user.delete()
        
post_save.connect(createProfile , sender=User)
post_delete.connect(deleteProfile , sender=Profile)
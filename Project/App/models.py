from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
import json
# Create your models here.

class User(models.Model):
    mobile_number = models.IntegerField()
    user_name = models.CharField(max_length=20)
    headers = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.mobile_number
    
class Session(models.Model):
    session_key = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField(unpack_ipv4=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.mobile_number


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    headers = json.loads(instance.headers)
    user_agent=headers['HTTP_USER_AGENT']
    ip_address=headers['REMOTE_ADDR']
    try:
        existing_session = Session.objects.get(user=instance, user_agent=user_agent, ip_address=ip_address)
    except Session.DoesNotExist:
        session_key = hash((instance.mobile_number, user_agent, ip_address))
        existing_session = Session.objects.create(user=instance, session_key=session_key, user_agent=user_agent, ip_address=ip_address)
    if not existing_session.active:
        Session.objects.filter(user=instance).update(active=False)
        existing_session.active = True
        existing_session.save()
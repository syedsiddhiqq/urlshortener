from django.db import models

# Create your models here.
from shortener.models import Falcomx

class ClickEventManager(models.Manager):
    def create_event(self,instance):
        if isinstance(Falinstance,instance):
            obj,created = self.get_or_create(falcomxurl = Falinstance)
            obj.count = 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    falcomxurl  = models.OneToOneField(Falcomx)
    count = models.IntegerField(default = 0)
    updated = models.DateTimeField(auto_now = True,)
    timestamp = models.DateTimeField(auto_now_add = True,)

    objects =  ClickEventManager()

    def __str__(self):
        return "{i}".format(i = self.count)

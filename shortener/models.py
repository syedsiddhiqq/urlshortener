from django.db import models
from .utils import codegenerator,createshortcode
from .validators import validate_url,validate_dot_com
from django.core.urlresolvers import reverse
from django.conf import settings

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class FalcomxUrlManager(models.Manager):
    def all(self,*args,**kwargs):
        qsmain = super(FalcomxUrlManager,self).all(*args,**kwargs)
        qs = qsmain.filter(active=True)
        return qs

    def refreshcodes(self,items=None):
        qs = Falcomx.objects.filter(id__gte=1)
        if items is not None and isinstance(items,int):
            qs = qs.order_by("-id")[:items]
        newcodes = 0
        for q in qs:
            q.shortcode = createshortcode(q)
            print(q.shortcode)
            q.save()
            newcodes = newcodes+1
        return "New Codes Made :{i}".format(i=newcodes)




class Falcomx(models.Model):
    url  = models.CharField(max_length = 220,validators=[validate_url,validate_dot_com])
    shortcode = models.CharField(max_length=15,unique = True,blank = True,)
    updated = models.DateTimeField(auto_now = True,)
    timestamp = models.DateTimeField(auto_now_add = True,)
    active = models.BooleanField(default = True,    )
    objects = FalcomxUrlManager()
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = createshortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(Falcomx, self).save(*args, **kwargs)





    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path

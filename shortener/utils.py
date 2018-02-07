import random
import string
from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)



def codegenerator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def createshortcode(instance,size = SHORTCODE_MIN):
    newcode = codegenerator(size = size)
    klass = instance.__class__
    if klass.objects.filter(shortcode = newcode).exists():
        return createshortcode(size = size)
    return newcode
    

import random
import string

def codegenerator(size = 6,chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def createshortcode(instance,size = 6):
    newcode = codegenerator(size = size)
    klass = instance.__class__
    if klass.objects.filter(shortcode = newcode).exists():
        return createshortcode(size = size)
    return newcode

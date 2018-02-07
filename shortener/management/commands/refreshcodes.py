from django.core.management.base import BaseCommand, CommandError
from shortener.models import Falcomx

class Command(BaseCommand):
    help = 'Refreshes all the Falcomx shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items',type=int)

    def handle(self, *args, **options):
        return Falcomx.objects.refreshcodes(items = options['items'])

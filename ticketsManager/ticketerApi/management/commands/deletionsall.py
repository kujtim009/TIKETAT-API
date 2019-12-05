from django.core.management.base import BaseCommand, CommandError
from  ticketerApi.models import Regjionet, Reshtat, Ulset, Cmimet, Shitja
class Command(BaseCommand):
    help = 'delete all'


    def handle(self, *args, **options):
        Cmimet.objects.all().delete()
        Regjionet.objects.all().delete()
        Reshtat.objects.all().delete()
        Ulset.objects.all().delete()
        Shitja.objects.all().delete()

        
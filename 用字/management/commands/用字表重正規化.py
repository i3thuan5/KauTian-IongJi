from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from sys import stderr
from 用字.models import 用字表


class Command(BaseCommand):

    def handle(self, *args, **options):
        for ji in 用字表.objects.all():
            try:
                ji.full_clean()
            except ValidationError as tsho:
                print(ji, tsho, file=stderr)
                continue
            ji.save()

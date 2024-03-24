import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Hw_django.settings')
django.setup()

from quotes.models import Quote, Tag, Author
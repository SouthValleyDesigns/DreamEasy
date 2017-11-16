from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from DreamEasyApp.models import Member

import urllib2
import re


class Command(BaseCommand):
    help = 'Scrapes the soundcloud artist images for dream easy'

    # def __init__(self):
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        member_list = Member.objects.order_by('name')

        for member in member_list:
            try:
                response = urllib2.urlopen(str(member.soundcloud_url))
                soup = BeautifulSoup(response.read(), "lxml")

                for link in soup.find_all('script'):
                    script_info = link.string

                print re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+',
                                 str(script_info.encode('utf-8')))[0].replace('large', 't500x500')

            except:
                raise CommandError('Could not scrape "%s" for soundcould avatar' % member.name)
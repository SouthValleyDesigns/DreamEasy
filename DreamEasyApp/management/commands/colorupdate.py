from colorthief import ColorThief

from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from scss import parser
import sass

import urllib2
import re


class Command(BaseCommand):
    help = 'Scrapes the soundcloud artist images for dream easy'

    # def __init__(self):
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)


    def handle(self, *args, **options):

        # response = urllib2.urlopen(str('static/img/artworks-000261133514-g8rmw0-t500x500.jpg'))
        # soup = BeautifulSoup(response.read(), "lxml")
        #
        # for link in soup.find_all('script'):
        #     script_info = link.string

        #Fix your shitty API soundcloud!!
        # soundcloud_avatar = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+',
        #                  str(script_info.encode('utf-8')))[0].replace('large', 't500x500')

        file_path = 'DreamEasyApp/static/sass/_colors.scss'
        src = open( file_path ).read()

        # Create parser object
        p = parser.Stylesheet( options=dict( compress=True ) )
        print p.loads( src )

        color_thief = ColorThief('DreamEasyApp/static/img/dreameasy.jpg')
        # get the dominant color
        dominant_color = color_thief.get_color(quality=10)
        # build a color palette
        palette = color_thief.get_palette(color_count=6, quality=10)

        print dominant_color, palette[2]

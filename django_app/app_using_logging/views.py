'''views.py'''

# stdlib imports ...
import logging

# third-party imports ...
# from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def hello(request):
    '''hello()'''
    logging.warning('Warn message/')
    logging.info('info_message')
    logging.error('holla')
    return HttpResponse('Logging done')

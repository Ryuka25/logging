# pylint: disable=missing-module-docstring

import logging
log = logging.getLogger(__name__) # __name__ containt the full name of the current module.

def do_somehting():
    '''Function where you do smthng.'''
    log.debug("Doing something!")

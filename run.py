#!/usr/bin/python

from logfile import *

if __name__ == "__main__":
    log = filelog()
    log.bootlog()
    log.lastlog()
    log.secure()
    log.maillog()
    

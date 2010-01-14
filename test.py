#!/usr/bin/python

from pyrowl import Pyrowl
from pprint import pprint
import os

p = None

def main(keys):
    global p
    pkey = None
    
    p = Pyrowl()
    if os.path.isfile("myproviderkey"):
        pkey = open("myproviderkey",'r').readline().strip()
        p.providerkey(pkey)

    p.addkey(keys)
    res = p.push("test app", 'test event', 'test msg', batch_mode=False)
    pprint(res)
    
if __name__ == "__main__":
    if os.path.isfile('myapikey'):
        keys = filter(None,
                      open("myapikey",'r').read().split("\n")
                      )
        
        main(keys)
    else:
        print "need a file named myapikey containing one apikey per line"

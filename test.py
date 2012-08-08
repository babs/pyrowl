#!/usr/bin/python

from pynma import PyNMA
from pprint import pprint
import os

p = None

def main(keys):
    global p
    pkey = None
    
    p = PyNMA()
    if os.path.isfile("mydeveloperkey"):
        dkey = open("mydeveloperkey",'r').readline().strip()
        p.developerkey(dkey)

    p.addkey(keys)
    res = p.push("test app", 'test event', 'test msg <a href="http://www.google.com/">google</a>', 'http://example.com', batch_mode=False, html=True)
    pprint(res)
    
if __name__ == "__main__":
    if os.path.isfile('myapikey'):
        keys = filter(None,
                      open("myapikey",'r').read().split("\n")
                      )
        
        main(keys)
    else:
        print "need a file named myapikey containing one apikey per line"

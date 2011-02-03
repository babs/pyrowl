Pyrowl
======

Pyrowl is a simple python module for the [Prowl][prowl] [API][Prowl API].

[prowl]: http://www.prowlapp.com/
[Prowl API]: http://www.prowlapp.com/api.php

[Prowl][prowl]
---------------
Prowl is the Growl client for the iPhone OS. Notifications from your Mac or Windows computer are sent to your iPhone or iPod touch using push. Prowl has an extensive API, which allows your scripts to integrate beautifully. (source: http://www.prowlapp.com/)

Pyrowl
------

### How it works:
First, import the module:

    import pyrowl

#### Keys management

Create a Pyrowl simple instance:

    p = pyrowl.Pyrowl( "apikey(s)", "providerkey")

Both apikey(s) and providerkey are optionnal. If you'd like to add just one API key, set it as string, if you want more, just provide a list of API key strings.

    p = pyrowl.Pyrowl(['apikey1','apikey2])    # multiple API keys
    p = pyrowl.Pyrowl("apikey1","providerkey") # 1 API key with a providerkey

For more flexible usage, you can add and remove keys:

    p.addkey("apikey1")
    p.addkey(["apikey2","apikey3"])

Or set or change the providerkey

    p.providerkey("providerkey")

#### Notification or Push or Add
    
    p.push(application, event, description, (opt) priority, (opt) batch mode)

##### Application

Application is your message generating application name (limited to 256)

ex: my music player

##### Event

Event is the event name (limited to 1024)

ex: switched to next track

##### Description

The description is the payload of your message (limited to 10000 (10k))
ex:

    Playing next song, Blah Blah Blah
    Artist: blah blah
    Album:  blah blah
    Track: 18/24

##### Priority

Priority goes from -2 (lowest) to 2 (highest). the default priority is 0 (normal)

##### Batch mode

Batch mode is a boolean value to set if you'd like to push the same message to multiple API keys 5 by 5 (as the actual verion of prowl API allows you). Thias can reduce the number of call you make to the API which are limited.

#### Return

The push method returns a dict containing different values depending of the success of you call:

##### The call succeed

you'll have in the dict those keys:

    type: success
    code: the HTTP like code (200 if success)
    remaining: the number of API call you can to until the reset
    resetdate: which is the date of the remaining reset (UTC)

##### The call failed

For wathever reason, you call failed, the dict key "message" will contains the erro message returned by Prowl API. You'll find those keys:

    code: 400, 401, 405, 406 or 500 (depends of the error kind)
    message: API error message

For the code description,  please refer to [Prowl API documentation][Prowl API] for more informations

##### The python module encountered an unhandled problem (mostly during parsing)

The return keys will be:

    code: 600
    type: pyrowlerror
    message: the exception message


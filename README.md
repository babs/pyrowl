Pynma
======

Pynma is a simple python module for the [NotifyMyAndroid][nma] [API][NMA API].

[nma]: http://www.notifymyandroid.com/
[NMA API]: http://www.notifymyandroid.com/api.jsp

Credits to: Damien Degois (github.com/babs)
Refactoring: Adriano Maia (adriano@usk.bz)

[NotifyMyAndroid][nma]
---------------
NotifyMyAndroid is a platform that allows you to delivery push notifications from virtually any application to your Android device. We offer a client application that runs on your Android device and a set of easy to use public APIs that can be integrated into your software. (source: http://www.notifymyandroid.com/)

### How it works:
First, import the module:

    import pynma

#### Keys management

Create a PyNMA simple instance:

    p = pynma.PyNMA( "apikey(s)", "developerkey")

A developerkey is optional. If you'd like to add just one API key, set it as string, if you want more, just provide a list of API key strings.

    p = pynma.PyNMA(['apikey1','apikey2'])   # multiple API keys
    p = pynma.PyNMA("apikey1","providerkey") # 1 API key with a providerkey

For more flexible usage, you can add and remove keys:

    p.addkey("apikey1")
    p.addkey(["apikey2","apikey3"])

Or set or change the providerkey

    p.developerkey("developerkey")

#### Notification or Push or Add
    
    p.push(application, event, description, (opt) url, (opt) contenttype, (opt) priority, (opt) batch mode, (opt) html)

##### Application

Application is your message generating application name (limited to 256)

ex: my music player

##### Event

Event is the event name (limited to 1000)

ex: switched to next track

##### Description

The description is the payload of your message (limited to 10000 (10k))
ex:

    Playing next song, Blah Blah Blah
    Artist: blah blah
    Album:  blah blah
    Track: 18/24

##### Url

The URL which should be attached to the notification.
This will trigger a redirect when on the user's device launched, and is viewable in the notification list.

##### Content type

Define the content type.
According API, the only content type actually considered is text/html.

##### Priority

Priority goes from -2 (lowest) to 2 (highest). the default priority is 0 (normal)

##### Batch mode

Batch mode is a boolean value to set if you'd like to push the same message to multiple API keys 5 by 5 (as the actual verion of prowl API allows you). This can reduce the number of call you make to the API which are limited.

##### HTML

Set html to True is a shortcut for contenttype="text/html".

#### Return

The push method returns a dict containing different values depending of the success of you call:

##### The call succeed

you'll have in the dict those keys:

    type: success
    code: the HTTP like code (200 if success)
    remaining: the number of API call you can to until the reset
    resetdate: number of remaining minutes till the hourly reset of your API call limit

##### The call failed

For wathever reason, you call failed, the dict key "message" will contains the erro message returned by Prowl API. You'll find those keys:

    code: 400, 401, 402 or 500 (depends of the error kind)
    message: API error message

For the code description,  please refer to [NMA API documentation][NMA API] for more informations

##### The python module encountered an unhandled problem (mostly during parsing)

The return keys will be:

    code: 600
    type: pynmaerror
    message: the exception message

Thanks
------

* **Cev** for URL integration and some fixes in docstring
* **ChaoticXSinZ** for UTF-8 integration and other typos

License (MIT)
-------------

    Copyright (c) 2010-2011, Damien Degois.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

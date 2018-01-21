# pyapi
[![Build Status](https://travis-ci.org/npo-poms/pyapi.svg?)](https://travis-ci.org/npo-poms/pyapi)


Python libraries and scripts to talk to the NPO api's. Currently classes are available for the frontend api (Media, Pages, Schedule, and Screens) and for the media backend api (MediaBackend, Pages Backend and Thesaurus).

#How to install

You need a [python3](https://www.python.org/downloads/) installation. Also you need the 'setuptools' module:

```
sudo -H pip3  install setuptools
Collecting setuptools
  Downloading setuptools-36.4.0-py2.py3-none-any.whl (478kB)
    100% |################################| 481kB 2.1MB/s 
Installing collected packages: setuptools
Successfully installed setuptools-36.4.0
```

Then you can install the python libraries and command line scripts with the following command
```
pip3 install git+https://github.com/npo-poms/pyapi.git@5.5.0
```
or if you dare install the latest, which may sometimes be a bit broken:
```
pip3 install git+https://github.com/npo-poms/pyapi.git
```


Check [setup.py](https://github.com/npo-poms/pyapi/blob/master/setup.py) to see which command line clients it will make available. These also serve as examples on how to use the npoapi module.

E.g. you can do:
```bash
michiel@belono:~$ npo_media_get POMS_NTR_388772
No configuration file found. Now creating.
Your NPO api key?:
Your NPO api secret?:
Your NPO api origin?:
{"objectType":"program","mid":"POMS_NTR_388772","type":"BROADCAST","avType":"AUDIO","workflow":"PUBLISHED","sortDate":1376395200000,"creationDate":1376435075424,"lastModified":1376435112166,"urn":"urn:vpro:media:program:28506247","embeddable":true,"episodeOf":[{"midRef":"AUTO_WINFRIEDDRAAITDOOR","urnRef":"urn:vpro:media:group:13405810","type":"SERIES","index":1,"highlighted":false,"added":1376435078278}],"crids":["crid://broadcast.radiobox2/203820"],"broadcasters":[{"id":"NTR","value":"NTR"}],"titles":[{"value":"Winfried Draait Door","owner":"RADIOBOX","type":"MAIN"}],"descriptions":[{"value":"Elke werkdag draait Winfried Baijens door op Radio 6 met de beste soul en jazz, nieuwe releases, Nederlands talent en de mooiste prijzen. Geen dag gaat voorbij zonder een thema dat veelal iets te maken heeft met de actualiteit. Voorwaarde is; het thema moet allitereren. Daar houdt Winfried namelijk van, allitereren.\nVerder hoor je berichten van nationale en internationale sterren, luisteraars, betrokkenen bij het thema en muziekvrienden die Winfrieds voicemail inspreken. DJ Git Hyper is een vaste gast en Winfried maakt ook een muzikale kettingbrief. Vele grote namen uit de Nederlandse muziekwereld werkten al mee aan deze multitracks.","owner":"RADIOBOX","type":"MAIN"}],"genres":[],"countries":[],"languages":[],"duration":7200000,"descendantOf":[{"midRef":"AUTO_WINFRIEDDRAAITDOOR","urnRef":"urn:vpro:media:group:13405810","type":"SERIES"},{"midRef":"POMS_S_VPRO_171668","urnRef":"urn:vpro:media:group:14683553","type":"ARCHIVE"},{"midRef":"POMS_S_VPRO_218686","urnRef":"urn:vpro:media:group:14921825","type":"ARCHIVE"},{"midRef":"POMS_S_VPRO_117474","urnRef":"urn:vpro:media:group:20347947","type":"PLAYLIST"}],"email":["winfrieddraaitdoor@radio6.nl"],"websites":[{"value":"http://www.radio6.nl/winfrieddraaitdoor"}],"predictions":[{"state":"REALIZED","platform":"INTERNETVOD"}],"locations":[{"programUrl":"http://download.omroep.nl/audiologging/r6/2013/08/13/1400_1600_winfried_draait_door.mp3","avAttributes":{"avFileFormat":"MP3"},"duration":7200000,"owner":"RADIOBOX","creationDate":1376435052113,"lastModified":1376435075571,"workflow":"PUBLISHED","urn":"urn:vpro:media:location:28506251"}],"scheduleEvents":[{"start":1376395200000,"duration":7200000,"poProgID":"POMS_NTR_388772","channel":"RAD6","urnRef":"urn:vpro:media:program:28506247","midRef":"POMS_NTR_388772"}],"images":[{"title":"winfried_baijens.jpg","description":"Winfried Draait Door","imageUri":"urn:vpro:image:121034","owner":"RADIOBOX","type":"PICTURE","highlighted":false,"creationDate":1376435059364,"lastModified":1376435075570,"workflow":"PUBLISHED","urn":"urn:vpro:media:image:28506249"}]}
```

Or e.g.
```bash
michiel@baleno:~$ ENV=dev npo_schedule_get | jq             
{
  "total": 850553,
  "offset": 0,
  "max": 10,
  "items": [
    {
      "channel": "NED1",
      "start": 74016000000,
      "guideDay": 73954800000,
      "duration": 2062000,
      "urnRef": "urn:vpro:media:program:19222530",
      "midRef": "immix_116032",
      "media": {
        "objectType": "program",
        "mid": "immix_116032",
        "type": "BROADCAST",
        "avType": "VIDEO",
        "sortDate": 74016000000,
...
```

More information about command line options can be gotten with  '-h'
```bash
michiel@belono:~$ npo_media_get -h
usage: npo_media_get.py [-h] [-s {asc,desc}] [-a {json,xml}]
                        [-e {prod,test,dev}] [-d]
                        mid [{descendants,members,episodes,related,}]

Get an media object from the NPO Frontend API

positional arguments:
  mid                   The mid of the object to get
  {descendants,members,episodes,related,}
                        Sub call for the mediaobject. On default the
                        mediaobject itself is returned, but ou can also opt
                        for one of these choices

optional arguments:
  -h, --help            show this help message and exit
  -s {asc,desc}, --sort {asc,desc}
                        sort (only relevant when using sub)
  -a {json,xml}, --accept {json,xml}
  -e {prod,test,dev}, --env {prod,test,dev}
  -d, --debug

DEBUG=true and ENV=<dev|test|prod> environment variables are recognized.
Credentials are read from a config file. If such a file does not exist it will
offer to create one.

```

# Backend API editing
The 'npo_mediabackend_get' call supports a --process options, this works like so:
```bash
michiel@belono:~$ npo_mediabackend_get -e prod  POMS_S_VPRO_3512033 --process "update.duration='PT5M'"
<?xml version="1.0" ?>
<group avType="MIXED" embeddable="true" mid="POMS_S_VPRO_3512033" ordered="true" type="PLAYLIST" urn="urn:vpro:media:group:72865615" xmlns="urn:vpro:media:update:2009">
  <broadcaster>VPRO</broadcaster>
  <broadcaster>NTR</broadcaster>
  <portal>NETINNL</portal>
  <title type="MAIN">NetInNl</title>
  <duration>PT5M</duration>
  <locations/>
  <scheduleEvents/>
  <images/>
  <poSeriesID>POMS_S_VPRO_3512033</poSeriesID>
</group>
```
This way a poms object can be edited using python. The resulting XML can be posted back.

Objects can be created and manipulated using the classes (generated by [pyxb](http://pyxb.sourceforge.net/) in the npo.xml module.


# Configuration
Credentials and other setting for the different api's can be manually added and maintained in a file  USER_HOME/conf/creds.properties
It looks for example like this
```
# npo api
apikey=<your key>
secret=<your secret>
origin=http://www.vpro.nl

# backend api
user=vpro-mediatools:<your password>
user.prod=vpro-mediatools:<your password or prod>

email=michiel.meeuwissen@gmail.com
```

# Tests
Tests can be run like so:
```bash
python3 -m unittest discover -s tests  -p '*_test.py'
```
or like so if nosetests is installed:
```bash
nosetests
```
# More examples
The libraries and scripts in this repository are all completely generic. In https://github.com/npo-poms/scripts we collect more specific scripts, to perform certain tasks like 'link an image to all members of a group', or 'check the consistency of the pages api'.

 




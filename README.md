# com.rokid.crx.client-m library for Python

A python port of the com.rokid.crx.client-m Java library.

The idea is to allow you to use the CRX-M SDK on any device with bluetooth.

Library supports Python 3.6+ (confirmed using `vermin`), for as far as Bleak supports.


**This repo is NOT an official Rokid Glasses repo. We're not associated with Rokid.**
*This is just a personal project to port CRX-M to python, so it can be used on any platform, instead of only phones with android 10+*


## Info

The Rokid Glasses do have to be re-paired in order for this to connect.

Guide below should help you. If you were to run into issues after you done all the steps according to your display,
then you could make an issue if there isn't one for your display yet.


## Current Status

Currently as of v0.0.1-alpha, only the libcaps.so library is ported.

I already have more code, which connects to the glasses and then already allows me to read events,
but it's not perfect and is just unusable at the moment. I'm still decompiling and developing the rest.
Consider giving me my time to work it out ;) Anyways, as always God bless and peace out!


## Setting up

Install this library using `pip install pyrokid-crx-clientm`


## API/Example

Here is an example code with comments to explain the API functions:

```py
# Imports
from pyrokid_crx_clientm.libcaps import Caps

# Decode bytes to a Caps object
bytes_variable = b'\x00\x00\x00\x99\x05\x05SSSuu$xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\x11MA:C0:AD:DR:ES:SSTxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==\x01\x01'
caps = Caps.from_bytes(bytes_variable)
print(caps)
print('socketUuid:', caps[0].get_string())
print('macAddress:', caps[1].get_string())
print('rokidAccount:', caps[2].get_string())
print('glassesType:', caps[3].get_uint()) # 0-no display, 1-have display

# Encode Caps object to bytes
caps = Caps()
caps.write_uint(0x1004)
caps.write_uint(1)
caps.write_uint(5)
caps.write('TestDevice')
caps.write_ulong(1765983621057)
data = caps.serialize()
print(data)

```


Extra API documentation can be found on the [ReadTheDocs](https://pyrokid-crx-clientm.readthedocs.io/en/latest/) documentation.

# com.rokid.cxr.client-m library for Python

A python port of the com.rokid.cxr.client-m Java library.

The idea is to allow you to use the CXR-M SDK on any device with bluetooth.

Library supports Python 3.7+ (confirmed using `vermin`), for as far as Bleak supports.


**This repo is NOT an official Rokid Glasses repo. We're not associated with Rokid.**
*This is just a personal project to port CXR-M to python, so it can be used on any platform, instead of only phones with android 10+*


## Info

The Rokid Glasses do have to be re-paired in order for this to connect.

Guide below should help you. If you were to run into issues after you done all the steps according to your display,
then you could make an issue if there isn't one for your display yet.


## Current Status

Currently as of v0.0.3a2, only the libcaps.so library is ported.
And some of the java classes have been ported as well.

I already have more code, which connects to the glasses and actually is able to send stuff to the glasses,
but it's not perfect and is just unusable at the moment. I'm still decompiling and developing the rest.
Consider giving me my time to work it out ;) Anyways, as always God bless and peace out!


## Setting up

Install this library using `pip install pyrokid-cxr-clientm`

### Dependencies

When running the install command, python will automatically install the requirements.
But that doesn't stop me being transparent about the dependencies, so here's the list and why its used:

- Bleak: The main Bluetooth library, supports all platforms and is easy to work with, so that's why I'm using it.
- pybluez: Secondary Bluetooth library, used when you're running on python <3.9, for the Rfcomm socket, which is built-in starting from python 3.9+
- tzlocal: A library which allows me to get your machine's timezone name (like `Europe/Amsterdam`) to send with the `setGlassTime()` method
- pycryptodome: A library for doing AES hashing, which is done in the `Md5Utils` class.


## API/Example

Here is an example code with comments to explain the API functions:

```py
# Imports
from pyrokid_cxr_clientm import Caps

# Decode bytes to a Caps object
bytes_variable = b'\x00\x00\x00\x99\x05\x05SSSuu$xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\x11MA:C0:AD:DR:ES:SSTxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==\x01\x01'
caps = Caps.fromBytes(bytes_variable)
print(caps)
print('socketUuid:', caps.at(0).getString())
print('macAddress:', caps.at(1).getString())
print('rokidAccount:', caps.at(2).getString())
print('glassesType:', caps.at(3).getUInt32()) # 0-no display, 1-have display

# Encode Caps object to bytes
caps = Caps()
caps.writeUInt32(0x1004)
caps.writeUInt32(1)
caps.writeUInt32(5)
caps.write('TestDevice')
caps.writeUInt64(1765983621057)
data = caps.serialize()
print(data)
```


Extra API documentation can be found on the [ReadTheDocs](https://pyrokid-cxr-clientm.readthedocs.io/en/latest/) documentation.

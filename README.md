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

Currently as of v0.0.4a2, only the libcaps.so library is ported.
Other than that, also the `utils.LogUtil`, `utils.ValueUtil`, `extend.callbacks`, `extend.infos`, `extend.listeners`, `extend.version` and `extend.sync` have all been ported.
Also `extend.controller.FileController` is finished and working. You just need to have wifi already enabled for you to use it already,
since I'm still working making the bluetooth connection more stable.
The WifiController is coming soon, tho.

I already have more code, which connects to the glasses and actually is able to send stuff to the glasses,
but it's still not fully perfect. I'm still decompiling java and c code and still developing the rest.
Consider giving me my time to work it out. Anyways, as always God bless and peace out!


## Setting up

Install this library using `pip install pyrokid-cxr-clientm`

### Dependencies

When running the install command, python will automatically install the requirements.
But that doesn't stop me being transparent about the dependencies, so here's the list and why its used:

- Bleak: The main Bluetooth library, supports all platforms and is easy to work with, so that's why I'm using it.
- pybluez: Secondary Bluetooth library, used when you're running on python <3.9, for the Rfcomm socket, which is built-in starting from python 3.9+
- tzlocal: A library which allows me to get your machine's timezone name (like `Europe/Amsterdam`) to send with the `setGlassTime()` method
- pycryptodome: A library for doing AES hashing, needed to do `CxrApi.checkGlassesSn()`, which will check if the clientSecret and license file are correct. *(altho this part is also edited to continue regardless of it being correct)*
- requests: A library for performing a POST HTTP request for the `extend.version.check_util.CheckUtil` class. I could've used httplib, but requests is much easier to work with.
- dataclasses_json: A library to make it easier to encode and decode dataclasses to and from JSON strings.


## API/Example

Here is an example code with comments to explain the API functions:

```py
# Imports
from pyrokid_cxr_clientm import Caps
from pyrokid_cxr_clientm.utils import ValueUtil
from pyrokid_cxr_clientm.extend.callbacks import *
from pyrokid_cxr_clientm.extend.infos import *
from pyrokid_cxr_clientm.extend.listeners import *

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

----

To download files from your device, when the glasses are already connected to wifi (since I've not added the bluetooth controller yet), you can use this snippet:
```py
from pyrokid_cxr_clientm.utils import ValueUtil
from pyrokid_cxr_clientm.extend.controllers import FileController
import os, logging

logging.basicConfig(level=logging.INFO)

savePath = 'media/'
os.makedirs(savePath, exist_ok=True) # Make the folder if it doesnt exist yet
types = [ValueUtil.CxrMediaType.PICTURE] # Select the type of media you want to download, you can do [ValueUtil.CxrMediaType.ALL] if you want all media types
address = '192.168.178.114' # Change this to the IP of your glasses. (I cannot really give an easy way to get the ip, except check your network before wifi is on and then after and see which is new)
c1 = FileController.Callback()
FileController.getInstance().startDownload(0, savePath, types, None, address, c1)
# Now just wait, it is still running in the background!

# You could do this to kinda let the thing still wait, but it's not a perfect way to do it.
FileController.getInstance().i.t.join()
```

*P.s. when downloading VIDEO files, you will also see .txt files show up. Those are used by the Hi Rokid app to do the post stabilisation*


## Extra API Documentation

Extra API documentation can be found on the [ReadTheDocs](https://pyrokid-cxr-clientm.readthedocs.io/en/latest/) documentation.

web2jinja
=========

web2py controller decorator that returns Jinja2 compiled template string.

Usage
=====
Place this file under your web2py applications/myapp/modules.

```python
# myapp/controllers/somecontroller.py

from applications.myapp.modules.web2jinja import Web2Jinja

@Web2Jinja(locals())
def index():
    return {
        'foo': 'bar',
    }
```

will render same view file i.e. applications/myapp/views/somecontroller/index.html <br>
by using Jinja2! It will include all the global variables such as request, <br>
response, session, cache and other helpers but only "ON" boolean helper will be missing.

License
=======
The MIT License (MIT)<br>
Copyright (c) 2012 Roy Enjoy a.k.a. kirpit<br>
http://www.opensource.org/licenses/mit-license.php

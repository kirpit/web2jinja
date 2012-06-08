web2jinja
=========

web2py controller decorator that returns Jinja2 compiled template string.
Place this file under your web2py application/modules.

Usage
======
```python
# myapp/controllers/somecontroller.py

from applications.myapp.modules.web2jinja import Web2Jinja

@Web2Jinja(request)
def index():
    return {
        'foo': 'bar',
    }
```

will render same view file i.e. myapp/views/somecontroller/index.html
by using Jinja2!

License
=======
The MIT License (MIT)
Copyright (c) <2012> <Roy Enjoy a.k.a. kirpit>
http://www.opensource.org/licenses/mit-license.php


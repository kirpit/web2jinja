# -*- coding: utf-8 -*-
"""
<web2jinja.py>
https://github.com/kirpit/web2jinja

web2py controller decorator that returns Jinja2 compiled template string.
Place this file under your web2py application/modules.

Example usage:
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

==================================================
The MIT License (MIT)
Copyright (c) <2012> <Roy Enjoy a.k.a. kirpit>
http://www.opensource.org/licenses/mit-license.php
==================================================
"""
from jinja2 import Environment, PackageLoader


class Web2Jinja(object):
    template = None
    func = None

    def __init__(self, request):
        app = 'applications.%s' % request.application
        jinja_env = Environment(loader=PackageLoader(app, 'views'))
        template_name = '%s/%s.%s' % (request.controller,
                                      request.function,
                                      request.extension)
        self.template = jinja_env.get_template(template_name)

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            context = func(*args, **kwargs)
            return self.template.render(**context)
        return wrapper

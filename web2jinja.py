# -*- coding: utf-8 -*-
"""
<web2jinja.py>
https://github.com/kirpit/web2jinja

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
"""
from jinja2 import Environment, PackageLoader


class Web2Jinja(object):
    web2py_locals = None
    template = None

    def __init__(self, web2py_locals):
        # filter web2py globals
        self.web2py_locals = dict([(k, v) for k, v in web2py_locals.iteritems()
                                          if not k.startswith('_') and
                                             getattr(v, '__module__', '').startswith('gluon')])
        # create jinja2 env and template
        request = self.web2py_locals['request']
        app = 'applications.%s' % request.application
        jinja_env = Environment(loader=PackageLoader(app, 'views'))
        template_name = '%s/%s.%s' % (request.controller,
                                      request.function,
                                      request.extension)
        self.template = jinja_env.get_template(template_name)

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # create template context
            context = dict(func(*args, **kwargs).items() + self.web2py_locals.items())
            return self.template.render(**context)
        return wrapper
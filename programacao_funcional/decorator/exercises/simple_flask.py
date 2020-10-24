"""
>>> app = Flask()
>>> set(app.routes)
set()
>>> @app.route('/')
... def root():
...     return 'root'
...
>>> set(app.routes)
{'/'}
>>> root()
'root'
>>> app.execute('/')
'root'
>>> @app.route('/name')
... def name(user):
...     return f'Name: {user}'
...
>>> list(app.routes)
['/', '/name']
>>> name('Python')
'Name: Python'
>>> app.execute('/name', 'Pro')
'Name: Pro'
>>> app.execute('/not_exists')
'404'
"""


class Flask:
    def __init__(self):
        self.routes = dict()

    def route(self, path):
        def decorator(f):
            self.routes[path] = f
            return f

        return decorator

    def execute(self, path, *args, **kwargs):
        f = self.routes.get(path)
        if f is None:
            return "404"
        return f(*args, **kwargs)

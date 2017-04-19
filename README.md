# django-main

A minimal Django app for a single page app entry point.


## Installation

`pip` is the easiest way to get the package:

```python
pip install django-main
```

Add the package to your Django settings file:

```python
INSTALLED_APPS = [
    'main',
    ...
]
```

Add the URLs:

```python
urlpatterns = [
    url('^', include('main.urls')),
    ...
]
```


## Usage

You will now have an index view for `/`. This will load a page with an HTML element
with an ID of `main-mount`, where your app can be mounted.

The currently logged in user is passed to the client side via `jsdata` (please see
the README at http://github.com/furious-luke/django-jsdata).


## Extending

TODO

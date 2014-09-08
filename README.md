fbauth
======

Requirements
============
* Django 1.6+

Installation
============
Just grab the Django app fbauth/apps/fbauth, put it into your apps directory and
add it to your `INSTALLED_APPS`.

Instructions
============
Load the `fbauth` template-tag library into your template, then call
`fbauth_css` inside your `head` tag and call the `fbauth_button` wherever you
want the Facebook button to be rendered.

E.g.

```django
{% load fbauth %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My App</title>
    {% fbauth_css %}
</head>
<body>
    {% fbauth_button %}
</body>
</html>
```

Configure the `FBAUTH_REDIRECT_URL` variable in your `settings` module with the
url that should be receiving the access token from facebook. Sometimes it's more
convinient to put it inside the `__init__` module of your app so that you can
take advantage of Django's `reverse` function.

E.g.

```python
# myapp/__init__.py
from django.core.urlresolvers import reverse
from django.conf import settings

setattr(settings, 'FBAUTH_REDIRECT_URL',
    reverse('demo:redirect') + '?access_token={0}')
```

Remember that your redirection URL should include the format token `{0}` to
indicate where facebook's access token should be written.

You can change the default language (`en-us`) to the locale `es-pe` using the
`LANGUAGE_CODE` setting in your `settings` module.

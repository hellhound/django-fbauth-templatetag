from django.core.urlresolvers import reverse
from django.conf import settings

setattr(settings, 'FBAUTH_REDIRECT_URL',
    reverse('demo:redirect') + '?access_token={0}')

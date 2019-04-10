from django.conf.urls import include, url
from allauth.utils import import_attribute

from .provider import SamlProvider

from django.conf.urls import include, url

from allauth.utils import import_attribute


def default_urlpatterns(provider):
    login_view = import_attribute(
        provider.get_package() + '.views.saml_login')

    urlpatterns = [
        url('^login/$',
            login_view, name=provider.id + "_login"),
    ]

    return [url('^' + provider.get_slug() + '/', include(urlpatterns))]



urlpatterns = default_urlpatterns(SamlProvider)

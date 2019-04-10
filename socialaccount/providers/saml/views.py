from allauth.socialaccount import providers
from allauth.socialaccount.helpers import (
    complete_social_login,
    render_authentication_error,
)
from .provider import SamlProvider


class SamlAdapter():
    provider_id = SamlProvider.id
    def __init__(self, request):
        self.request = request
        pass

    def get_provider(self):
        return providers.registry.by_id(self.provider_id, self.request)

    def complete_login(self, request):
        extra_data = dict(id=request.META.get('eppn', ''),
            first_name=request.META.get('givenName', ''),
            last_name=request.META.get('sn', ''),
            username=request.META.get('eppn', ''),
            email=request.META.get('mail', '').lower())

        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)

class SamlView():
    @classmethod
    def adapter_view(cls, adapter):
        def view(request, *args, **kwargs):
            self = cls()
            self.request = request
            self.adapter = adapter(request)
            return self.dispatch(request, *args, **kwargs)
        return view
    def dispatch(self,request):
        login = self.adapter.complete_login(request)
        return complete_social_login(request, login)

saml_login = SamlView.adapter_view(SamlAdapter)

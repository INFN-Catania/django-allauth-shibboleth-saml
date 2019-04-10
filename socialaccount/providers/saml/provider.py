from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth.provider import OAuthProvider


class SamlAccount(ProviderAccount):
    pass

class SamlProvider(OAuthProvider):
    id = 'saml'
    name = 'saml'
    account_class = SamlAccount

    def get_profile_fields(self):
        default_fields = ['id',
                          'first-name',
                          'last-name',
                          'email-address',
                          'picture-url',
                          'picture-urls::(original)',
                          # picture-urls::(original) is higher res
                          'public-profile-url']
        fields = self.get_settings().get('PROFILE_FIELDS', default_fields)
        return fields

    def extract_uid(self, data):
        return data['id']

    def extract_common_fields(self, data):
        return data

provider_classes = [SamlProvider]

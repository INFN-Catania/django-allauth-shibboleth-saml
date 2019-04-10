# django-allauth-shibboleth-saml

This is a django-allauth provider to integrate Shibboleth authentication into
django based application.

## Configuration

To configure the authentication, the application has to run behind Apache httpd
service and Shibboleth SP has to be configured for the authentication.

Copy the provider inside the django-allauth library into the same path

```
allauth/socialaccount/providers/
```


Configure the Shibboleth authentication for the following location

```
/accounts/saml/login
```

Make sure the IdP will return the following attributes: `eppn`, `sn`,
`givenName` and `mail`.

Add the provider `allauth.socialaccount.providers.saml` to the list of
enabled providers in the configuration variable `INSTALLED_APPS`.


## Optional

The additional class `NoNewUsersAccountAdapter` allows to suspend
the creation of local accounts. If you would enable it just copy the
file `account_adapter.py` in a location accessible by your application
and add the following configuration variable:

```
ACCOUNT_ADAPTER = 'account_adapter.NoNewUsersAccountAdapter'
```

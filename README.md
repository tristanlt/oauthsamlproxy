OAuth SAML Proxy
================

Sometime, the quick way is decorated with flowers, sometime seem like hell. This README can contain devils.

About
-----

OAuth is a good and flexible auth system. A lot of apps can use OAuth.

For SAML, apps should be sub-uri of Service Provider. SAML isn't supported by all apps (recent ones).

SAML federation is awesome, it allow users from differents companies to collaborate whithout additional account.

OAuth SAML Proxy is an OAuth provide which authenticate user with SAML Federation ( with Apache Shibd ).

1. User want to auth
2. App redirect to OAuth Provider
3. OAuth Provider redirect user to /accounts/login
4. Apache catch and redirect user to federation auth (DiscoveryService > IDP Login form...)
5. Apache set headers
6. Django catch header and login user
7. OAuth create token for user and redirect to app

Simple as relativity theory.


Configuration
-------------

Next authentication, Apache set headers. A middleware CustomHeaderMiddleware set the name of the header used to user name.

```
class CustomHeaderMiddleware(PersistentRemoteUserMiddleware):    
        header = "HTTP_MAIL"
```



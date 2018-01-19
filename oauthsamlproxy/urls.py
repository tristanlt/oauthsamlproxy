from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings

import oauth2_provider.views as oauth2_views

from oauthsamlproxy.views import login, me
import oauthsamlproxy


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('osp/login/', oauthsamlproxy.views.login, name="login"),
    url(r'^osp/o-auth/', include("oauth2_provider.urls", namespace="oauth2_provider")),
    url(r'^osp/me/', me, name='me'),
    ]


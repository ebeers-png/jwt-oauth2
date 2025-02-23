#!/usr/bin/env python
# encoding: utf-8
"""
copyright (c) 2016-2018 Earth Advantage. All rights reserved.
..codeauthor::Fable Turas <fable@raintechpdx.com>
"""

from __future__ import absolute_import, unicode_literals

# Imports from Django
import django
from django.urls import include, re_path

# Imports from Third Party Modules
import oauth2_provider.views as oauth2_views

# Local Imports
from oauth2_jwt_provider.views import (
    RestrictedApplicationDelete,
    RestrictedApplicationDetail,
    RestrictedApplicationList,
    RestrictedApplicationRegistration,
    RestrictedApplicationUpdate,
    RestrictedAuthorizedTokenDelete,
    RestrictedAuthorizedTokensList,
)

# OAuth2 provider endpoints
urlpatterns = [
    re_path(
        r'^authorize/$',
        oauth2_views.AuthorizationView.as_view(),
        name="authorize"
    ),
    re_path(
        r'^token/$',
        oauth2_views.TokenView.as_view(),
        name="token"
    ),
    re_path(
        r'^revoke-token/$',
        oauth2_views.RevokeTokenView.as_view(),
        name="revoke-token"
    ),
    re_path(
        r'^applications/$',
        RestrictedApplicationList.as_view(),
        name="list"
    ),
    re_path(
        r'^applications/register/$',
        RestrictedApplicationRegistration.as_view(),
        name="register"
    ),
    re_path(
        r'^applications/(?P<pk>\d+)/$',
        RestrictedApplicationDetail.as_view(),
        name="detail"
    ),
    re_path(
        r'^applications/(?P<pk>\d+)/delete/$',
        RestrictedApplicationDelete.as_view(),
        name="delete"
    ),
    re_path(
        r'^applications/(?P<pk>\d+)/update/$',
        RestrictedApplicationUpdate.as_view(),
        name="update"
    ),
    re_path(
        r'^authorized-tokens/$',
        RestrictedAuthorizedTokensList.as_view(),
        name="authorized-token-list"
    ),
    re_path(
        r'^authorized-tokens/(?P<pk>\d+)/delete/$',
        RestrictedAuthorizedTokenDelete.as_view(),
        name="authorized-token-delete"
    ),
]

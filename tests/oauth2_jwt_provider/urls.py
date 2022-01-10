# Imports from Django
import django
from django.urls import include, re_path

OAUTH_NAMESPACE = 'oauth2_provider'

urlpatterns = [
    re_path(
        r'^oauth/',
        include('oauth2_jwt_provider.urls', namespace=OAUTH_NAMESPACE)
    )
]

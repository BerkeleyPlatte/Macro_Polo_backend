from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from macropoloapi.models import *
from macropoloapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'foods', Foods, base_name='food')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
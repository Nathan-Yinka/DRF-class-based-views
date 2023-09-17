from . import views
from django.urls import path
from rest_framework.authtoken import views as apiviews

urlpatterns = [
    path("api/",views.api_home),
    path('api/auth/', apiviews.obtain_auth_token),
]

"""django_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from django_practice.settings import DEBUG
from django_practice.users.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mileage/', include('django_practice.gas_mileages.urls')),
    path('login/', LoginView.as_view(), name="login"),
    path('api/v1/', include('django_practice.v1.gas_mileages.urls')),
    path('api/v1/auth/', obtain_jwt_token),
    path('api/v1/refresh/', refresh_jwt_token),
    path('api/v1/verify/', verify_jwt_token),
    path('silk/', include('silk.urls', namespace='silk')),
]
schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
    ),
    patterns=[path('/api/v1', include('django_practice.v1.gas_mileages.urls'))],
    generator_class=OpenAPISchemaGenerator,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json')]
urlpatterns += [url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')]

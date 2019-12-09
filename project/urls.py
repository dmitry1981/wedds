from django.urls import path, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # path('api/', include("api.urls", namespace='api')),
    # path('auth/', include('rest_auth.urls')),
    # path('auth/registration/', include('rest_auth.registration.urls')),
    path('auth/', include('users.urls')),
    path('docs/', include_docs_urls(title='API docs')),
    path('admin/', admin.site.urls),
]



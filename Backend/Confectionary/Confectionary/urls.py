from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('Backend.urls')),
]

# path('admin/', admin.site.urls),№

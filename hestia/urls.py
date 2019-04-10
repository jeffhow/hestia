"""

hestia URL Configuration

"""

from django.contrib import admin
from django.urls import include, path
#from . import views

urlpatterns = [
    path('', include('inspections.urls') ),   # inspections App
    path('admin/', admin.site.urls),        # Admin App
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
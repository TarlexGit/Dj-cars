from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.routers import urlpatterns as mr

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include((mr, "main"), namespace="instance_name")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

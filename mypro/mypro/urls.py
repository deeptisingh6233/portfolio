from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # ← add this

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portpo.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])  # ← add this
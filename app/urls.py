from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import app.core.views

urlpatterns = [
    path('', app.core.views.home, name='home'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

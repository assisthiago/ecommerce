from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import app.core.views

urlpatterns = [
    path("", app.core.views.home, name="home"),
    path("sign-in", app.core.views.sign_in, name="sign-in"),
    path("sign-up", app.core.views.sign_up, name="sign-up"),
    path("sign-out", app.core.views.sign_out, name="sign-out"),
    path("recover-password", app.core.views.recover_password, name="recover-password"),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

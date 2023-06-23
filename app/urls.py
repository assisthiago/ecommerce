from django.contrib import admin
from django.urls import path

import app.core.views

urlpatterns = [
    path('', app.core.views.home, name='home'),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path('acc/', include('django.contrib.auth.urls'))
]

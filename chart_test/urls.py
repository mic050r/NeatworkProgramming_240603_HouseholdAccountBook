from django.contrib.auth import admin
from django.urls import path, include

app_name = 'chart_test'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chart_test/', include('chart_test.urls')),
]
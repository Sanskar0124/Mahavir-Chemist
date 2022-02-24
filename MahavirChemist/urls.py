from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
#     admin:
#     username = sanskar
#     password = 0124
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', views.index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Mahavir Chemist Admin"
admin.site.index_title = "Welcome to Mahavir Chemist Dashboard"
admin.site.site_title = "Mahavir Chemist Admin Pannel"

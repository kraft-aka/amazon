
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from applications.products.views import MainPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main-page'),
    path('categories/', include('applications.categories.urls')),
    path('products/', include('applications.products.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
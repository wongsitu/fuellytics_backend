from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from cars import views as CarsViews
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('cars', CarsViews.Cars, basename='cars')

urlpatterns = [
    path('health-check/', include('health_check.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/accounts/', include('accounts.urls')),
    path('api-auth', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

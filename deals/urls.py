from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from . import views
router = DefaultRouter()
router.register(r'deals', views.DealsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

# for swagger setting
from .swagger import swagger_urlpatterns

# for media setting
from django.conf.urls.static import static
from . import settings

from main.views import BookAPIViewSet

router = DefaultRouter()
router.register('book', BookAPIViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

# add media urls to urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# add to main urlpatterns swagger_urlpatterns
urlpatterns += swagger_urlpatterns
# end adding
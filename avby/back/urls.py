from rest_framework.routers import DefaultRouter
from back.views.views import ViewTransportMark
from django.urls import path, include

router = DefaultRouter()
router.register(r'mark', ViewTransportMark, basename='transport_mark')

urlpatterns = [
    path('', include(router.urls)),
]

from back.views.views import ViewTransportMark, ViewTransportModel, ViewTransportAd
from django.urls import path, include
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register(r'mark', ViewTransportMark, basename='mark')
router.register(r'ad', ViewTransportAd, basename='ad')

model_router = routers.NestedSimpleRouter(router, r'mark', lookup='mark')
model_router.register(r'model', ViewTransportModel, basename='mark-model')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(model_router.urls))
]

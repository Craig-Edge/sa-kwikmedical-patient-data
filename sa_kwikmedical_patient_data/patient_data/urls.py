from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientCallOutViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'patient-callouts', PatientCallOutViewSet, basename='patientcallout')

urlpatterns = [
    path('api/patients/', PatientViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/patients/<int:pk>/', PatientViewSet.as_view({'get': 'retrieve'})),
    path('api/', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    # ... other URL patterns ...

    # Map the custom list function to the URL pattern
    path('api/patients/', PatientViewSet.as_view({'get': 'list', 'post': 'create'})),

    # Map the custom retrieve function to the URL pattern
    path('api/patients/<int:pk>/', PatientViewSet.as_view({'get': 'retrieve'})),
]

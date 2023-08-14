from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'dob']
    search_fields = ['first_name', 'last_name', 'dob']    
    
    def get_queryset(self):
        queryset = Patient.objects.all()

        # Filter by first_name query parameter
        first_name = self.request.query_params.get('first_name', None)
        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)

        # Filter by last_name query parameter
        last_name = self.request.query_params.get('last_name', None)
        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)

        # Filter by dob query parameter
        dob = self.request.query_params.get('dob', None)
        if dob is not None:
            queryset = queryset.filter(dob=dob)

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)           

    # Custom GET method to retrieve a single patient
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        patient = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(patient)
        return Response(serializer.data)
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
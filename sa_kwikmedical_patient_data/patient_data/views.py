from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient, PatientCallOut
from .serializers import PatientSerializer, PatientCallOutSerializer
from rest_framework.decorators import action
from rest_framework import status

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'dob']
    search_fields = ['first_name', 'last_name', 'dob']    
    
    def get_queryset(self):
        queryset = Patient.objects.all()

        first_name = self.request.query_params.get('first_name', None)
        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)

        last_name = self.request.query_params.get('last_name', None)
        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)
            
        nhs_number = self.request.query_params.get('nhs_number', None)
        if nhs_number is not None:
            queryset = queryset.filter(nhs_number__icontains=nhs_number)

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)           

  
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


class PatientCallOutViewSet(viewsets.ModelViewSet):
    serializer_class = PatientCallOutSerializer

    def get_queryset(self):
        nhs_number = self.request.query_params.get('nhs_number', None)
        most_recent = self.request.query_params.get('most_recent', False)
        status = self.request.query_params.get('status', None)

        queryset = PatientCallOut.objects.all()

        if nhs_number:
            queryset = queryset.filter(nhs_number=nhs_number)
            
            if status:
                queryset = queryset.filter(status=status)

            if most_recent:
                queryset = queryset.order_by('-datetime')[:1]

        return queryset

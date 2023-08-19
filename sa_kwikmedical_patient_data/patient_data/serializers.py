from rest_framework import serializers
from .models import Patient, PatientCallOut

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientCallOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCallOut
        fields = '__all__'
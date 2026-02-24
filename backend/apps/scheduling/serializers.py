from rest_framework import serializers
from datetime import timedelta
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.get_full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.get_full_name', read_only=True)
    
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 
                 'scheduled_date', 'duration', 'status', 'symptoms', 'notes', 
                 'diagnosis', 'prescription', 'follow_up_required', 'follow_up_date', 
                 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'scheduled_date', 'duration', 'symptoms']
    
    def validate(self, data):
        # Check if doctor is available at the scheduled time
        doctor = data['doctor']
        scheduled_date = data['scheduled_date']
        duration = data.get('duration', 30)
        
        # Check for overlapping appointments
        overlapping = Appointment.objects.filter(
            doctor=doctor,
            scheduled_date__lt=scheduled_date + timedelta(minutes=duration),
            scheduled_date__gt=scheduled_date - timedelta(minutes=30),  # Assuming 30 min buffer
            status__in=['scheduled', 'confirmed', 'in_progress']
        ).exists()
        
        if overlapping:
            raise serializers.ValidationError("Doctor is not available at this time.")
        
        return data

class AppointmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['status', 'notes', 'diagnosis', 'prescription', 'follow_up_required', 'follow_up_date']

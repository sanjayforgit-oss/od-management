from rest_framework import serializers
from .models import ODRequest

class ODRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ODRequest
        fields = '__all__'
        read_only_fields = ['id', 'student', 'created_at', 'updated_at']

class ODRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ODRequest
        fields = ['register_no', 'name', 'program', 'section', 'reason', 'from_date', 'to_date', 'start_time', 'end_time']

from rest_framework import serializers
from .models import LoanPrediction

class LoanPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPrediction
        fields = '__all__'
        read_only_fields = ('credit_score', 'risk_level', 'created_at')
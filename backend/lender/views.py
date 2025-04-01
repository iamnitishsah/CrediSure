from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import LoanPredictionSerializer
from .models import LoanPrediction
from .ml_model import predict_risk
from rest_framework.permissions import IsAuthenticated

class PredictView(generics.GenericAPIView):
    serializer_class = LoanPredictionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        prediction = predict_risk(data)

        data['credit_score'] = prediction['credit_score']
        data['risk_level'] = prediction['risk_level']

        loan_prediction = LoanPrediction.objects.create(**data)
        return Response(LoanPredictionSerializer(loan_prediction).data, status=status.HTTP_201_CREATED)

class PredictionListView(generics.ListAPIView):
    serializer_class = LoanPredictionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LoanPrediction.objects.all()

class PredictionDetailView(generics.RetrieveAPIView):
    serializer_class = LoanPredictionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return LoanPrediction.objects.all()
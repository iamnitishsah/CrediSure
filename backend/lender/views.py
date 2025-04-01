from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import LoanPredictionSerializer
from .models import LoanPrediction
from .ml_model import predict_risk

class PredictView(generics.GenericAPIView):
    serializer_class = LoanPredictionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # Get prediction from ML model
        prediction = predict_risk(data)

        # Add prediction results to data
        data['credit_score'] = prediction['credit_score']
        data['risk_level'] = prediction['risk_level']

        # Save to database
        loan_prediction = LoanPrediction.objects.create(**data)
        return Response(LoanPredictionSerializer(loan_prediction).data, status=status.HTTP_201_CREATED)

class PredictionListView(generics.ListAPIView):
    serializer_class = LoanPredictionSerializer

    def get_queryset(self):
        return LoanPrediction.objects.all()

class PredictionDetailView(generics.RetrieveAPIView):
    serializer_class = LoanPredictionSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return LoanPrediction.objects.all()
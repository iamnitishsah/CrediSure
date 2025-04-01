from django.urls import path
from .views import PredictView, PredictionListView, PredictionDetailView

urlpatterns = [
    path('predict/', PredictView.as_view(), name='predict'),
    path('predictions/', PredictionListView.as_view(), name='prediction_list'),
    path('predictions/<int:id>/', PredictionDetailView.as_view(), name='prediction_detail'),
]
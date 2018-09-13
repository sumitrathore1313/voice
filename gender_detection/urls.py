from django.urls import path
from .views import GenderDetectionView

urlpatterns = [
    path('gender_detection', GenderDetectionView.as_view())
]
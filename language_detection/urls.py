from django.urls import path
from .views import LanguageDetectionView

urlpatterns = [
    path('language_detection', LanguageDetectionView.as_view())
]
from django.urls import path
from .views import SpeakerRecognitionView

urlpatterns = [
    path('speaker_recognition', SpeakerRecognitionView.as_view())
]
from django.urls import path
from .views import TextView, LogoView

urlpatterns = [
    path('channel', TextView.as_view()),
    path('logo', LogoView.as_view())
]
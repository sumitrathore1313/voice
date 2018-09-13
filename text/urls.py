from django.urls import path
from .views import TextView

urlpatterns = [
    path('text', TextView.as_view())
]
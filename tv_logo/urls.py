from django.urls import path
from .views import TextView

urlpatterns = [
    path('logo', TextView.as_view())
]
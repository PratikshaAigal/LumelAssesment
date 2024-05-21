from django.urls import path
from . import views

urlpatterns = [
    path('customer_analysis', views.CustomerAnalysis.as_view()),
]
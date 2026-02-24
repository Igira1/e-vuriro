from django.urls import path
from . import views

urlpatterns = [
    # Example route
    path('predict/', views.predict_view, name='predict'),
]
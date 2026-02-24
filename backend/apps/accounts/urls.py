from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('doctors/', views.DoctorListView.as_view(), name='doctor-list'),
]

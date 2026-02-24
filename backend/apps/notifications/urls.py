from django import path
from . import views
urlpatterns = [
    # Example route for notifications
    path('send/', views.send_notification, name='send_notification'),
    path('list/', views.list_notifications, name='list_notifications'),
]
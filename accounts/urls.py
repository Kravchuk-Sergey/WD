from django.urls import path
from .views import register, profile, activate

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
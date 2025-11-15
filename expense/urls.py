from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    # Add this line:
    path('register/', views.RegisterView.as_view(), name='register'),
# 2. Add this line to include all built-in auth views
    path('', include('django.contrib.auth.urls')),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]

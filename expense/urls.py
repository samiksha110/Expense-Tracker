from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in views
from expense.views import (
    RegisterView, 
    DashboardView, 
    TransactionCreateView, 
    TransactionListView, 
    GoalCreateView, 
    export_transactions
)

urlpatterns = [
    # 1. Authentication Paths
    path('register/', RegisterView.as_view(), name="register"),
    # Recommended: Add login/logout paths
    path('login/', LoginView.as_view(template_name='expense/registration/login.html'), name='login'), 
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # 2. Core App Paths
    path('', DashboardView.as_view(), name="dashboard"),

    # 3. Transaction Paths (Consistent Naming)
    path('transactions/add/', TransactionCreateView.as_view(), name='transaction_create'), # Changed name from transaction_add
    path('transactions/', TransactionListView.as_view(), name='transaction_list'), 
    
    # 4. Goal Paths (Consistent Naming)
    path('goals/add/', GoalCreateView.as_view(), name='goal_create'), # Changed path from goal/add/ and name from goal_add
    
    # 5. Utility Path
    path('report/generate/', export_transactions, name='export_transactions'), # Changed path for clarity
]
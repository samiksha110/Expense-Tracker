from django.shortcuts import render, redirect
from django.views import View
from expense.forms import RegisterForm, TransactionForm, GoalForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, Goal
from django.db.models import Sum
from django.contrib import messages

# --- Register View ---
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        # Corrected template path
        return render(request, 'expense/register.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
        # Corrected template path
        return render(request, 'expense/register.html', {'form':form})

# --- Dashboard View ---
class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(user = request.user)
        goals = Goal.objects.filter(user = request.user)

        # Calculate total income and expenses
        total_income = Transaction.objects.filter(user = request.user, transaction_type='Income').aggregate(Sum('amount'))['amount__sum'] or 0

        total_expense = Transaction.objects.filter(user = request.user, transaction_type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0

        net_savings = total_income - total_expense

        remaining_savings = net_savings

        goal_progress = []
        # Calculate goal progress
        for goal in goals:
            if remaining_savings >= goal.target_amount:
                goal_progress.append({'goal':goal, 'progress': 100})
                remaining_savings -= goal.target_amount
            elif remaining_savings > 0:
                progress = (remaining_savings / goal.target_amount) * 100
                goal_progress.append({'goal': goal, 'progress': progress})
                remaining_savings = 0
            else:
                goal_progress.append({'goal': goal, 'progress': 0})

        context = {
            'transactions': transactions,
            'total_income': total_income,
            'total_expense': total_expense,
            'net_savings': net_savings,
            'goal_progress': goal_progress,
        }
        # Corrected template path
        return render(request, 'expense/dashboard.html', context)
    
# --- Transaction Create View ---
class TransactionCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TransactionForm()
        # Corrected template path
        return render(request, 'expense/transaction_form.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, 'Transaction added successfully!')
            return redirect('dashboard')
        # Corrected template path
        return render(request, 'expense/transaction_form.html', {'form':form})
    
# --- Transaction List View ---
class TransactionListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(user = request.user)
        # Corrected template path
        return render(request, 'expense/transaction_list.html', {'transactions':transactions})
    
# --- Goal Create View ---
class GoalCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = GoalForm()
        # Corrected template path
        return render(request, 'expense/goal_form.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Goal created successfully!')
            return redirect('dashboard')
        # Corrected template path
        return render(request, 'expense/goal_form.html', {'form':form})

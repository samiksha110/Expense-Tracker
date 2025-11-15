from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from expense.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'expense/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')   # <-- redirect to login page
        return render(request, 'expense/register.html', {'form': form})


# Login View
def login_user(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')   # homepage

    return render(request, 'registration/login.html', {'form': form})
class DashboardView(LoginRequiredMixin, View):
    login_url = 'login'
    
      # Redirect to login page if not authenticated
    def get(self, request, *args, **kwargs):
        return render(request, 'expense/dashboard.html')

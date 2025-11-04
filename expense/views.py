from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from expense.forms import RegisterForm
#

# Class Based View
class RegisterView(View):
    def get(self,request,*args, **kwargs):
        form = RegisterForm()
        return render (request, 'expense/register.html',
        {'form':form})
    def post(self,request,*args, ** kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user)
           redirect('')
       
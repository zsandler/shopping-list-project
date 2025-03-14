from django.shortcuts import render, redirect
from .models import Grocery

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin

# class Grocery:
#     def __init__(self, name, quantity):
#         self.name = name
#         self.quantity = quantity

# groceries = [
#     Grocery('Apple', 1),
#     Grocery('Pear', 3),
#     Grocery('Junk Food', 4),
# ]

class Home(LoginView):
    template_name = 'home.html'

class GroceryCreate(LoginRequiredMixin, CreateView):
    model = Grocery 
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/groceries/'

class GroceryUpdate(LoginRequiredMixin, UpdateView):
    model = Grocery
    fields = ['quantity']
    success_url = '/groceries/'

class GroceryDelete(LoginRequiredMixin, DeleteView):
    model = Grocery
    success_url = '/groceries/'


# def home(request):
#     return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('groceries-index')
        else:
            error_message = "invalid sign up - try again!"
    form = UserCreationForm()
    return render(request, 'sign-up.html', {'form' : form, 'error_message' : error_message})


def signin(request):
    return render(request, 'groceries-index.html')

def grocery_index(request):
    groceries = Grocery.objects.all()
    return render(request, 'groceries/index.html', {'groceries' : groceries})


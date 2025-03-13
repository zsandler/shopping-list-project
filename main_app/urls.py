from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('groceries/', views.grocery_index, name='groceries-index'),
    path('accounts/signup/', views.signup, name='sign-up'),
]


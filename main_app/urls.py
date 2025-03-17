from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.signup, name='sign-up'),
    path('groceries/', views.grocery_index, name='groceries-index'),
    path('groceries/create/', views.GroceryCreate.as_view(), name='grocery-create'),
    path('groceries/<int:pk>/update/', views.GroceryUpdate.as_view(), name='grocery-update'),
    path('groceries/<int:pk>/delete/', views.GroceryDelete.as_view(), name='grocery-delete'),
]


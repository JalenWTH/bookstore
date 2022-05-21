from django.urls import path
from bookstore import views

urlpatterns = [
    path('home/', views.Home, name='Home'),
    path('login/', views.Login, name='Login'),
    path('signup/', views.Signup, name='Signup'),
    path('order/<int:book_id>', views.Order, name='Order'),
    path('checkout/<int:book_id>', views.Checkout, name='Checkout'),
]
    
from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.home , name = 'home'),
    path('logout/' , views.logout_user , name = 'logout'),
    path('register/' , views.register_user , name = 'register'),
    path('customer_record/<int:pk>' , views.expense_record , name = 'expense_record'),
    path('delete/<int:pk>' , views.delete_record , name = 'delete'),
    path('add/' , views.add_record , name= 'add'),
    path('update/<int:pk>' , views.update , name= 'update')
]

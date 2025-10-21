from django.urls import path,include
from  crudapp1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('details/<int:pk>',views.details,name='details'),
    path('create',views.create,name='create'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name = 'delete')
]











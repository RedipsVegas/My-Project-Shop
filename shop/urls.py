from django.urls import path, re_path
from . import views


app_name = 'shop'

urlpatterns = [
    re_path('register/', views.RegisterFormView.as_view(), name='register'),
    re_path('login/', views.LoginView.as_view(), name='login'),
    re_path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_filtered'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]


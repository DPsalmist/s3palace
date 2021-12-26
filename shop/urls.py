from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
path('h/', views.home, name='home'),
path('contact/', views.contact, name='contact'),
path('about/', views.about, name='about'),
path('products/', views.product_list, name='product_list'),
path('', views.home_list, name='home_list'),
path('<int:id>/<slug:slug>/', views.suit_detail,name='suit_detail'),
path('<slug:category_slug>/', views.category_list,name='product_list_by_category'),
path('<slug:category_slug>/', views.product_list,name='product_list_by_category'),
#path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
]
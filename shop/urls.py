from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
path('contact/', views.contact, name='contact'),
path('about/', views.about, name='about'),
path('search/', views.search, name='search'),
path('', views.home_list, name='home'),
path('<int:id>/<slug:slug>/', views.suit_detail,name='suit_detail'),
path('<slug:category_slug>/', views.category_list,name='product_list_by_category'),
#path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
]
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('product_single/<int:id>/<slug:slug>', views.product_single, name='product_single'),
    path('category_product/<int:id>/<slug:slug>',views.category_product, name='category_product'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('c_product/', views.c_product, name='c_product'),
    path('Ordeer/', views.Ordeer, name='Ordeer')
]
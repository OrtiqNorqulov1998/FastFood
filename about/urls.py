from django.urls import path
from about import views





urlpatterns = [
    path('about/', views.about, name='about'),
    path('chef/<int:id>', views.chef, name='chef'),
]

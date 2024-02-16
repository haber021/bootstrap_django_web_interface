from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='expenses'),
    path('add-exp', views.add_exp, name='add-exp')  # Corrected function name
]

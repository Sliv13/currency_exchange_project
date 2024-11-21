from django.urls import path
from . import views

urlpatterns=[
    path('currencies/',views.Currencies.as_view(),name='get_currencies'),
    path('currencies/<str:base>/<str:target>/',views.Get_Exchange_Rates.as_view(),name='get_rates'),
    
]